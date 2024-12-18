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
        print("попробуй еще раз")
        index += 1
