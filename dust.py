import serial,time
import mysql.connector


def insertVariblesIntoTable(sen,sen1,id):
        connection = mysql.connector.connect(host='10.206.4.149',
                                             database='sensor',
                                             user='trainee_504',
                                             password='12345')
        cursor = connection.cursor()
        mySql_insert_query = """UPDATE data SET pm25 = %s,pm10 = %s WHERE id =%s """

        recordTuple = (sen,sen1,id)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

ser = serial.Serial()
ser.baudrate = 9600
ser.port= '/dev/ttyUSB0'
ser.open()

while True:
    data=[]
    for index in range(0,10):
        datum=ser.read()
        data.append(datum)
    pmtwofive =int.from_bytes(b''.join(data[2:4]), byteorder='little')/10
    print(pmtwofive)
    pmten=int.from_bytes(b''.join(data[4:6]), byteorder='little')/10
    print(pmten)
    insertVariblesIntoTable(pmtwofive,pmten,1)
    time.sleep(2)
