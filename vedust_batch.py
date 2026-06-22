# Deprecated
from typing import Any

from requests import post

BASE_URL = "https://app.neverland.money/api/vedust/batch"
MAX_BATCH_SIZE = 100


def check_has_shiny(ids: list[str]) -> bool:
    # バッチの許容サイズごとに分割
    chunks = [ids[i : i + MAX_BATCH_SIZE] for i in range(0, len(ids), MAX_BATCH_SIZE)]

    for c in chunks:
        json = {"tokenIds": c}
        print(f"POST {BASE_URL}, {json=}")
        response = post(BASE_URL, json={"tokenIds": c}).json()
        try:
            assignments: dict[str, dict[str, Any]] = response["assignments"]
            results: list[bool] = [a["isShiny"] for a in assignments.values()]
            if any(results):
                return True
        except KeyError:
            print(f"Invalid Response\n{response}")

    return False
