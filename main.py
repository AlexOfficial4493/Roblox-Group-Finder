import os 
import threading
import requests, random
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Aleks Group Finder")


def groupfinder():
    try:
        id = random.randint(1000000, 1150000)
        r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}", timeout=30)
        if 'owned' not in r.text:
            re = requests.get(f"https://groups.roblox.com/v1/groups/{id}", timeout=30)
            if re.status_code != 429:
                if 'errors' not in re.json():
                    if 'isLocked' not in re.text and 'owner' in re.text:
                        if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                            hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                            print(f"[+] Hit: {id}")
                        else:
                            print(f"[-] No Entry Allowed: {id}")
                    else:
                        print(f"[-] Group Locked: {id}")
            else:
                print(f"[-] Group API Rate Limited")
        else:
            print(f"[-] Group Already Owned: {id}")
    except:
        pass


print("""


____ _    ____ _  _ ____    ____ ____ ____ _  _ ___  
|__| |    |___ |_/  [__     | __ |__/ |  | |  | |__] 
|  | |___ |___ | \_ ___]    |__] |  \ |__| |__| |    
                                                     
____ _ _  _ ___  ____ ____ 
|___ | |\ | |  \ |___ |__/ 
|    | | \| |__/ |___ |  \ 
                           
""")

#your webhook
hook = (https://discord.com/api/webhooks/1229803225503502419/mJrel-WOAhUy4eG248mqLd3-SfuxScptjXXeaP_6scw4tfG2TVJ2fs1ZeTEQLZJxTrIs)
#number of threads
threads = int(input(18))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
