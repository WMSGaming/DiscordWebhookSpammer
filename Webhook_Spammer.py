from dhooks import Webhook,file
import time

print("""
 __      __ __  __  ___       __      __      _     _               _          ___  _ __                                     
 \ \    / /|  \/  |/ __|      \ \    / / ___ | |__ | |_   ___  ___ | |__      / __|| '_ \ __ _  _ __   _ __   ___  _ _       
  \ \/\/ / | |\/| |\__ \       \ \/\/ / / -_)|  _ \|   \ / _ \/ _ \| / /      \__ \| .__// _` || '  \ | '  \ / -_)| '_|      
   \_/\_/  |_|  |_||___/        \_/\_/  \___||____/|_||_|\___/\___/|_\_\      |___/|_|   \__/_||_|_|_||_|_|_|\___||_|        

""")



spam = input("What would you like to spam? ")
avatarurl = input("What is your avatar url?")
webhooks = input("Enter webhook to spam:")
hook = Webhook(webhooks)


while True:
    hook.send(spam,avatar_url=avatarurl)
    time.sleep(0.8)
    print("Attacking Webhook server")


