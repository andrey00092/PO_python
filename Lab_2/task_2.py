salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
balance = 0

for I in range(1, months+1):
    if I == 1:
        balance = salary - spend
    else:
        spend = spend + spend * increase
        debt = salary - spend
        balance = balance + debt

money_capital = -round(balance, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
