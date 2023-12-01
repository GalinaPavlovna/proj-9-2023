import random

def welcome_message():
    print('Добро пожаловать в игру угадай число!')
    print('Нажмите Enter, чтобы продолжить…')
    input()

def game_start():
    rounds = int(input('Введите количество раундов, которые вы хотите сыграть(например, 5): '))
    return rounds

def game_round(round_number):
    print(f'Раунд {round_number}:')
    hidden_number = random.randint(1, 3)
    user_choice = int(input('Введите одно из трех чисел, или введите 0 для выхода: '))

    if user_choice == 0:
        return False
    elif user_choice == hidden_number:
        return True
    else:
        print('Попытка не удалась!')



def main():
    welcome_message()
    rounds = game_start()

    for round_number in range(1, rounds + 1):
        if not game_round(round_number):
            print("Выход из игры.")
            break
        elif round_number < rounds:
            play_again = input("Вы хотите продолжить игру? Введите'да' или 'нет': ")
        if play_again.lower() == 'нет':
            break
        if round_number == rounds:
            print("Поздравляем! Вы успешно прошли все раунды!")


main()

