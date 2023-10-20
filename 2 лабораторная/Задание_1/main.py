money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

count_of_month = 0
while money_capital > 0:
    count_of_month += 1
    money_capital = money_capital + salary - spend
    spend = spend * 1.05

print("Количество месяцев, которое можно протянуть без долгов:", count_of_month - 1)