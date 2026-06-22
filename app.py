from time import sleep

from leaderboard import fetch_addresses
from user import check_has_shiny
from text_file import append_address, restore_addresses

PAGE_SIZE = 100
START_PAGE_NUM = 0
MAX_PAGE_NUM = 10
CURRENT_TIDE = 6
COOL_DOWN_SEC = 1

shiny_addresses = restore_addresses()

for p in range(START_PAGE_NUM, MAX_PAGE_NUM):
    print(f"page={p}")
    addresses = fetch_addresses(CURRENT_TIDE, p, PAGE_SIZE)
    unchecked_addresses = [a for a in addresses if a not in shiny_addresses]
    sleep(COOL_DOWN_SEC)
    for a in unchecked_addresses:
        sleep(COOL_DOWN_SEC)
        if check_has_shiny(CURRENT_TIDE, a):
            print(a)
            append_address(a)
    print("\n")
