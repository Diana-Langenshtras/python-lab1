users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений
statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count_of_users = len(users)
unique_visits = len(set(users))
statistics["Общее количество"] = count_of_users
statistics["Уникальные посещения"] = unique_visits
print(statistics)

