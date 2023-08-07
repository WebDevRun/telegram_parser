from aiohttp import ClientSession
from .headers import headers


async def find_match(match_teams: str) -> int | None:
    match_url = f"https://leon.ru/api-2/betline/search?q={match_teams}&flags=reg,urlv2"
    session = ClientSession()

    try:
        response = await session.get(match_url, headers=headers)
        match_json = await response.json()

        if len(match_json) == 0:
            return None

        id: int = match_json[0]["id"]
        return id

    except:
        return None

    finally:
        await session.close()


if __name__ == "__main__":
    import asyncio

    match = input("Введите название матча:\n")
    id = asyncio.run(find_match(match))
    print("match id", id)
