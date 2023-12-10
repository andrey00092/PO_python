list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

Num_of_players = len(list_players)

border = int(Num_of_players/2)

First_team = list_players[:border]
Second_team = list_players[border:]

print(First_team)
print(Second_team)
