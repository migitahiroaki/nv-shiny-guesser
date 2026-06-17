FILE_PATH = "addresses.txt"


def append_address(address: str) -> None:
    with open(FILE_PATH, "a") as f:
        f.write(f"{address}\n")


def restore_addresses() -> list[str]:
    with open(FILE_PATH, "r") as f:
        return [line.strip() for line in f.readlines()]
