from aiohttp import ClientSession
from typing import NamedTuple
from .headers import headers


class Player(NamedTuple):
    name: str
    goal_count: int


class Time(NamedTuple):
    minutes: int
    seconds: int


class MatchValues(NamedTuple):
    time: Time
    players: tuple[Player, Player]


async def get_match_values(id: int) -> MatchValues:
    match_data_url = f"https://leon.ru/api-2/betline/event/all?ctag=ru-RU&eventId={id}"
    session = ClientSession()

    response = await session.get(match_data_url, headers=headers)
    match_data = await response.json()

    await session.close()

    first_player: str = match_data["competitors"][0]["name"]
    second_player: str = match_data["competitors"][1]["name"]
    score_str: str = match_data["liveStatus"]["score"]
    score = score_str.split(":")

    if match_data["liveStatus"]["stage"] == "Перерыв":
        minutes = 45
        seconds = 0
    else:
        minutes: int = match_data["liveStatus"]["fullProgress"]["time"]["minutes"]
        seconds: int = match_data["liveStatus"]["fullProgress"]["time"]["seconds"]

    return MatchValues(
        time=Time(minutes, seconds),
        players=(
            Player(name=first_player, goal_count=int(score[0])),
            Player(name=second_player, goal_count=int(score[1])),
        ),
    )


if __name__ == "__main__":
    import asyncio

    id = int(input("Введите id матча:\n"))
    match_values = asyncio.run(get_match_values(id))
    print(match_values)
