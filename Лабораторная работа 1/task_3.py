list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players)//2
first_team = list_players[:count_of_players]
second_team = list_players[count_of_players:]

print(first_team)
print(second_team)
