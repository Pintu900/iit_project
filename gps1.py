import serial,time
import mysql.connector

ser = serial.Serial('/dev/ttyACM0')
def insertVariblesIntoTable(sen,id):
        connection = mysql.connector.connect(host='10.206.4.149',
                                             database='sensor',
                                             user='trainee_504',
                                             password='12345')
        cursor = connection.cursor()
        mySql_insert_query = """UPDATE data SET log= %s WHERE id =%s """

        recordTuple = (sen,id)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")
while True:
    line=ser.readline()
    if line.startswith(b'$G'):
        var=line.decode('utf-8')
        insertVariblesIntoTable(var,1)
        print(var)
        time.sleep(1)
        
        

