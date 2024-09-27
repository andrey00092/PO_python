money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = money_capital + salary
months = 1

while budget - spend > 0:
    if months == 1:
        budget = budget - spend
    else:
        spend = spend + spend * increase
        budget = budget + salary - spend

    months = months + 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
