from aiohttp import ClientSession
from match.headers import headers


async def find_match(match_teams: str):
    match_url = f"https://hiddentreasure.icu/LiveFeed/Web_SearchZip?text={match_teams}&strict=true"
    session = ClientSession()

    try:
        response = await session.get(match_url, headers=headers)
        match_json = await response.json()
        id: int = match_json["Value"][0]["I"]
        return id

    except:
        return None

    finally:
        await session.close()
