from typing import Any
from requests import get

BASE_URL = "https://app.neverland.money/api/user"


def fetch_vedust_ids(epoch: int, address: str) -> list[str]:
    url = f"{BASE_URL}?address={address}&epoch={epoch}"
    print(f"GET {url}")
    response: dict[str, Any] = get(url).json()
    vedust_ids: list[str] = [t["id"] for t in response["DustLockToken"]]
    return vedust_ids
