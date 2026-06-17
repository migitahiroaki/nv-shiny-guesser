from typing import Any

from requests import get

BASE_URL = "https://app.neverland.money/api/leaderboard"


# def fetch_all_addresses(
#     current_tide: int, page_num: int, page_size: int = DEFAULT_PAGE_SIZE
# ) -> list[str]:
#     addresses: list[str] = []
#     offset = page_num * page_size
#     addresses.extend(_fetch_addresses(current_tide, DEFAULT_PAGE_SIZE, offset))
#     return addresses


# def _fetch_addresses(epoch: int, limit: int, offset: int) -> list[str]:
#     url = f"{BASE_URL}?epoch={epoch}&limit={limit}&offset={offset}"
#     response: dict[str, Any] = get(url).json()
#     stats: list[dict[str, Any]] = response["UserEpochStats"]
#     return [u["user_id"] for u in stats]


def fetch_addresses(epoch: int, page_num: int, page_size: int) -> list[str]:
    url = f"{BASE_URL}?epoch={epoch}&limit={page_size}&offset={page_size * page_num}"
    print(f"GET {url}")
    response: dict[str, Any] = get(url).json()
    stats: list[dict[str, Any]] = response["UserEpochStats"]
    return [u["user_id"] for u in stats]
