from dhooks import Webhook
import time

print("===================")
print("WMS Webhook Spammer")
print("===================")

spam = input("What would you like to spam? ")

webhooks = input("Enter webhook to spam:")
count = 1

hook = Webhook(webhooks)


while count > 0:
    hook.send(spam)
    time.sleep(0.8)


