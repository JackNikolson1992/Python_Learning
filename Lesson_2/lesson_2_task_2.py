def is_year_leap(x):
    if (x % 4 == 0 and x % 100 !=0) or x % 400 ==0:
     print('год' ,x, ": True")
    else:
     print('год' ,x, ": False")

is_year_leap(2022)
    
