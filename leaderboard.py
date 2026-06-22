from typing import Any

from requests import get

BASE_URL = "https://app.neverland.money/api/leaderboard"


def fetch_addresses(epoch: int, page_num: int, page_size: int) -> list[str]:

    url = f"{BASE_URL}?epoch={epoch}&limit={page_size}&offset={page_size * page_num}"
    print(f"GET {url}")
    response: dict[str, Any] = get(url).json()
    try:
        stats: list[dict[str, Any]] = response["UserEpochStats"]

        # filter Multiplier > 1x
        return [u["user_id"] for u in stats if u["lastAppliedMultiplierBps"] > 10000]
    except KeyError:
        print(f"Invalid Response\n{response}")
        return []
