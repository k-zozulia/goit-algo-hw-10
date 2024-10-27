from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

model = LpProblem("Drink_Production_Optimization", LpMaximize)

x1 = LpVariable("Lemonade", lowBound=0, cat='Continuous')
x2 = LpVariable("FruitJuice", lowBound=0, cat='Continuous')

model += lpSum([x1, x2]), "Total_Production"

model += 2 * x1 + x2 <= 100, "Water_Constraint"
model += x1 <= 50, "Sugar_Constraint"
model += x1 <= 30, "LemonJuice_Constraint"
model += 2 * x2 <= 40, "FruitPuree_Constraint"

model.solve()

print("Status:", LpStatus[model.status])
print("Кількість виробленого Лимонаду:", value(x1))
print("Кількість виробленого Фруктового соку:", value(x2))
print("Загальна кількість вироблених напоїв:", value(model.objective))