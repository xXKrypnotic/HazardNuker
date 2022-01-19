# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Hazard
from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def StatusChanger(token, Status):
    #change status 
    CustomStatus = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=CustomStatus)
        print_slow(f"\n{Fore.GREEN}Status changed to {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()