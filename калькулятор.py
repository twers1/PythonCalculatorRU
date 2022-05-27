#ДЕБИЛЬНЫЙ КАЛЬКУЛЯТОР ПЕРВАЯ ПРОГА

from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK)
print (Back.GREEN)
what = input("Что делаем? (+, -, /): ")
print(Back.CYAN)

a = float(input("Введи любое первое  число:"))
b= float(input("Введи любое второе число:"))
print(Back.YELLOW)
if what == "+":
    c = a+b
    print("Результат: " +str(c))

elif what == "-":
    c = a- b
    print("Результат:" +str(c))
elif what == "/":
    c = a/b
    print("Результат:" +str(c))
else:
    print("Выбрана неверная операция")
