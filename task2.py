x = int(input("Введите время в секундах "))
hours = x // 3600
minutes = (x - hours * 3600) // 60
seconds = x - (hours * 3600 + minutes * 60)
print(f"Время чч:мм:сс   {hours} : {minutes} : {seconds}")