from random import randint


def random_hit() -> int:
    return randint(1, 11)


def is_winner(pl: int, di: int) -> str:
    if pl == 21 or di > 21:
        return '\nПобедил Игрок'.upper()
    elif di == 21 or pl > 21:
        return '\nПобедил Дилер'.upper()
    elif di == pl:
        return '\nНичья'.upper()
    elif pl > di:
        return '\nПобедил Игрок'.upper()
    elif pl < di:
        return '\nПобедил Дилер'.upper()


player, diler = 0, 0
separator = '-' * 15
game_is_continues = True
print('Игра в 21'.upper())
while game_is_continues:
    print(f'У вас {player}\n{separator}\n'
          f'hit  - бросить кость\n'
          f'hold - остановться\n{separator}')
    answer = input()
    if answer == 'hold':
        while diler <= 16 and diler <= 21:
            diler += random_hit()
            print(f'У Дилера {diler}')
        else:
            print(is_winner(player, diler))
            game_is_continues = False
    elif answer == 'hit':
        player += random_hit()
        if player == 21:
            print(f'У вас {player}')
            print(is_winner(player, diler))
            game_is_continues = False
        if player > 21:
            print(f'У вас {player}')
            print(is_winner(player, diler))
            game_is_continues = False
