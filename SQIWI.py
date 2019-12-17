from SimpleQIWI import *
import time, os

phone = "-"

os.system('clear')
print("<//LYNEX TEAM//>")
print("[SQIWI / coded by p1mpus]")

token = input("Тoken QIWI: ")
api = QApi(token=token, phone=phone)
print("\nBalance QIWI: ")
print(api.balance)

a = input("\nQIWI account for transfer (phone number): ")
s = input("Amount of money to transfer: ")
c = input("Comment for transfer: ")
print("\nMoney transfer to your QIWI...")
api.pay(account=a, amount=s, comment=c)
time.sleep(5)
print("Money transfer to your QIWI [OK]")
print("Successfully!")
print("You Took: " + s + " Rubles")
print("Balance QIWI: ")
print(api.balance)
input("\nEnter...")
