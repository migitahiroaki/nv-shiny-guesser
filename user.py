from typing import Any
from requests import get

BASE_URL = "https://app.neverland.money/api/user"


# Deprecated
def fetch_vedust_ids(epoch: int, address: str) -> list[str]:
    url = f"{BASE_URL}?address={address}&epoch={epoch}"
    print(f"GET {url}")
    response: dict[str, Any] = get(url).json()
    try:
        vedust_ids: list[str] = [t["id"] for t in response["DustLockToken"]]
        return vedust_ids
    except KeyError:
        print(f"Invalid Response\n{response}")
        return []


def check_has_shiny(epoch: int, address: str) -> bool:
    url = f"{BASE_URL}?address={address}&epoch={epoch}"
    print(f"GET {url}")
    response: dict[str, Any] = get(url).json()
    try:
        shiny_ids: list[str] = response["shinyTokenIds"]
        return len(shiny_ids) > 0
    except KeyError:
        print(f"Invalid Response\n{response}")
        return False
