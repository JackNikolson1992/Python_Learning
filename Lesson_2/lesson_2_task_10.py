def bank(x,y):
    for each_year in range(y):
        x = (x * 1.1)
    return x
 
x=float(input("Сколько денег вкладываем? "))
 
y=int(input("На сколько лет? "))
 
print(bank(x, y))
# комент