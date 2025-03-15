def func_year(a , b ,c):
    if b < 6:
        day = a + b*31
    else:
        day = a + b*30 +6
    if day <=286:
        year = c+621
    else:
        year = c+622
    print(f"year is {year}")
    

def func_month(a,b,c):
    if b == 1:
        if a >= 12:
            month = 4
        else:
            month =3
    elif b == 2:
        if a <11:
            month = 4
        else :
            month = 5
    elif b ==3:
        if a<=10:
            month = 5
        else:
            month = 6
    elif b == 4:
        if a<=9:
            month =6
        else:
            month =7
    elif b == 5:
        if a<=9:
            month =7
        else:
            month =8
    elif b == 6:
        if a<=9:
            month =8
        else:
            month =9
    elif b == 7:
        if a<=8:
            month =9
        else:
            month =10
    elif b == 8:
        if a<=9:
            month =10
        else:
            month =11
    elif b == 9:
        if a<=9:
            month =11
        else:
            month =12
    elif b == 10:
        if a<=10:
            month =12
        else:
            month =1
    elif b == 11:
        if a<=11:
            month =1
        else:
            month =2
    elif b == 12:
        if a<=9:
            month =2
        else:
            month =3
    print(f"month is {month}")

def func_day(a,b,c):
    if b <=6:
        days = a + b*31
    else:
        days = a + b*30 +6
    if days in range(12,42):
        days -= 11
    elif days in range(42,73):
        days -= 41
    elif days in range(73,103):
        days -= 72
    elif days in range(103,134):
        days -=102
    elif days in range(134,165):
        days -=133
    elif days in range(165,195):
        days -=164
    elif days in range(195,226):
        days -=194
    elif days in range(226,256):
        days -=225
    elif days in range(256,287):
        days -=255
    elif days in range(287,318):
        days -=286
    elif days in range(318,346):
        days -=317
    elif days in range(346,366):
        days -=345
    elif days in range(1,12):
        days +=20
    print(f"days is {days}")



day_date =int(input("enter day:"))
month_date =int(input("enter month:"))
year_date =int(input("enter year:"))

func_year(day_date , month_date , year_date)
func_month(day_date , month_date , year_date)
func_day(day_date , month_date , year_date)
