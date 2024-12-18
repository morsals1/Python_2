import random

print("Отгадай число")
number = random.randint(0, 15)
index = 0

while True:
    a = int(input())
    if(a == int(number)): 
        index += 1
        print("Отгадал!!!", number, " ", index) 
        break
    elif(a != int(number)): 
        if(a > int(number)): 
            print("загаданное число меньше твоего")
        elif(a < int(number)):
            print("загаданное число больше твоего")
        print("попробуй еще раз")
        index += 1
