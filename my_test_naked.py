from naked import *
from datetime import datetime

print("-----------------")
print("Starting \"my_test_naked.py\"")
print("Test for newly added asteroids")
print("-----------------")


mysql_config_mysql_user = config.get("mysql_config", "mysql_user")
mysql_config_mysql_pass = config.get("mysql_config", "mysql_pass")
mysql_config_mysql_host = config.get("mysql_config", "mysql_host")
mysql_config_mysql_db = config.get("mysql_config", "mysql_db")
connection = mysql.connector.connect(user=mysql_config_mysql_user,
                                     password=mysql_config_mysql_pass,
                                     host=mysql_config_mysql_host, 
                                     database=mysql_config_mysql_db)

assert connection.is_connected() == True

print("Successful connection to DB!")
print("-----------------")

cursor = connection.cursor()

# Total ammount of asteroids in DB
id_list = cursor.execute("select ID from ast_daily;")
id_list = cursor.fetchall()

last_id = id_list[-1][0] # Gets last asteroid ID

# Date in which the asteroid was added to the DB
added_ast_date = cursor.execute("select create_date from ast_daily;")
added_ast_date = cursor.fetchall()

# Getting todays date
todaysDate = datetime.today().strftime('%Y-%m-%d')

# Counts how many asteroids have been added today
added_ast_today = 0
for i in range(last_id):
  if todaysDate == added_ast_date[i][0]:
    added_ast_today += 1

if added_ast_today <= 0:
  print("No new asteroids added today!")
else:
  print("There have been",added_ast_today,"added asteroids added today.")
print("-----------------")

