salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0
for eche_month in range(1, 11):
    money_capital += (spend - salary)
    spend = spend * 1.03
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))