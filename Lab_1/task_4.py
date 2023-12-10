users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

logs = {'Общее количество': 0, 'Уникальные посещения': 0}

unic_users = []

for i in users:
    if i not in unic_users:
        unic_users.append(i)

logs['Общее количество'] = len(users)
logs['Уникальные посещения'] = len(unic_users)

print(logs)
