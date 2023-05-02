from datetime import datetime as dt


date_time = dt.now()
print(date_time) # gives you preset date and time; 2023-05-02 15:54:31.672504
print(dt.date(date_time)) # prints the date; 2023-05-02

print(dt.ctime(date_time)) # Tue May  2 15:54:31 2023

date = dt.today()
print('Using today() function...', date) # 2023-05-02 15:57:34.364632

print()
