from aiohttp import ClientSession
from match.headers import headers
from typing import NamedTuple


class Player(NamedTuple):
    name: str
    goal_count: int


class MatchValues(NamedTuple):
    time: int
    players: tuple[Player, Player]


def get_value(dict: dict, key: str):
    return dict.get(key, 0)


async def get_match_values(id: int) -> MatchValues:
    match_data_url = f"https://hiddentreasure.icu/LiveFeed/GetGameZip?id={id}&lng=ru"
    session = ClientSession()

    response = await session.get(match_data_url, headers=headers)
    match_data = await response.json()

    await session.close()

    match_values = match_data["Value"]
    first_player = match_values["O1"]
    second_player = match_values["O2"]
    time = match_values["SC"]["TS"]
    goal_count = match_values["SC"]["FS"]

    return MatchValues(
        time=time,
        players=(
            Player(name=first_player, goal_count=get_value(goal_count, "S1")),
            Player(name=second_player, goal_count=get_value(goal_count, "S2")),
        ),
    )
