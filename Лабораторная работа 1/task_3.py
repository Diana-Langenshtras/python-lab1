list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players)
first_team = list_players[:count_of_players//2]
second_team = list_players[count_of_players//2:]

print(first_team)
print(second_team)
