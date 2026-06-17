from typing import Any

from requests import post

BASE_URL = "https://app.neverland.money/api/vedust/batch"


def check_has_shiny(ids: list[str]) -> bool:
    json = {"tokenIds": ids}
    print(f"POST {BASE_URL}, {json=}")
    response = post(BASE_URL, json={"tokenIds": ids})
    assignments: dict[str, dict[str, Any]] = response.json()["assignments"]
    results: list[bool] = [a["isShiny"] for a in assignments.values()]
    return any(results)
