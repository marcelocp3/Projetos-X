import datetime

today_date = datetime.datetime.now.strftime("%d/%m/%Y")
print(today_date)

new_today_date = today_date.strftime("%d/%m/%Y")

print(new_today_date)