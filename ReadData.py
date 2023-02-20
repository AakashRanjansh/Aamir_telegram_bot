import mysql.connector
import sendmessage as sm
import time


def fetch_all():
   conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tmgmt')
   cursor = conn.cursor()
   sql = '''SELECT * from sensordata'''
   cursor.execute(sql)
   all = cursor.fetchall()
   conn.close()
   return len(all)

first_count = fetch_all()

def send_telegram():
   conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tmgmt')
   cursor = conn.cursor()
   sql = '''SELECT * from sensordata'''
   cursor.execute(sql)
   all = cursor.fetchall()
   last_rfid = all[-1][0]
   user_data = '''SELECT VehicleId,Name,WalletBalance from users WHERE RFID=''' + str(last_rfid)
   cursor.execute(user_data)
   user_datasss = cursor.fetchall()
   date_time = '''SELECT Date from paymenthistories WHERE RFID=''' + str(last_rfid)
   cursor.execute(date_time)
   date_timesss = cursor.fetchall()
   conn.close()
   sm.send(str("Warning : Hello "+ str(user_datasss[-1][1])+", Your Vehicle no : " + str(user_datasss[-1][0]) + " has issued challan of Rs. 500 for Red light violation on "+ str(date_timesss[-1][0])+". Your Available Wallet Balance is " + str(user_datasss[-1][2])+"." ))


while True:
   time.sleep(1.4)
   A = fetch_all()
   if A > first_count:
      try:
         send_telegram()
         first_count = A
      except:
         pass
   
   