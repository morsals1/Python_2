import random

def main():
    deck = [
        ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
        ("Валет", 2), ("Дама", 3), ("Король", 4), ("Туз", 11)
    ] * 4

    random.shuffle(deck)

    total_points = 0

    print("Добро пожаловать в игру! Попробуйте набрать 21 очко.")

    while True:
        choice = input("Хотите взять карту? (y/n): ").lower()

        if choice == "n":
            print(f"Игра окончена. Вы набрали {total_points} очков.")
            break
        elif choice == "y":
            if not deck:
                print("Карты закончились!")
                break

            card, value = deck.pop()
            print(f"Вы вытянули карту: {card}, она приносит {value} очков.")

            total_points += value

            if total_points > 21:
                print(f"У вас {total_points} очков. Вы проиграли!")
                break
            elif total_points == 21:
                print("Поздравляем! Вы набрали 21 очко и выиграли!")
                break
            else:
                print(f"У вас {total_points} очков.")
        else:
            print("Введите 'y' для продолжения или 'n' для выхода.")

    print("Спасибо за игру! До свидания.")

if __name__ == "__main__":
    main()