from RPi_AS3935 import RPi_AS3935

import RPi.GPIO as GPIO

import time

from datetime import datetime

import mysql.connector

GPIO.setmode(GPIO.BCM)

def insertVariblesIntoTable(sen,sen1,id):
        connection = mysql.connector.connect(host='10.206.4.149',
                                             database='sensor',
                                             user='trainee_504',
                                             password='12345')
        cursor = connection.cursor()
        mySql_insert_query = """UPDATE data SET lightning = %s,state= %s WHERE id =%s """

        recordTuple = (sen,sen1,id)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

## Rev 1 Raspberry Pi: bus=0

## Rev 2 and later Raspberry Pi: bus=1

## All: address=<i2c add>



sensor = RPi_AS3935(address=0x03, bus=1)



## Uncomment to reset all registers to factory default values.

## sensor.reset()



sensor.calibrate(tun_cap=0x0d)

time.sleep(0.002)

sensor.set_indoors(True)

sensor.set_noise_floor## uncomment/set to filter out false positives

sensor.set_min_strikes(1)



def log_raw_data(data):

    # need to pass time as parameter and convert to UTC here

    utcnow = datetime.utcnow()

    version = 01

    timestamp = utcnow.strftime("%Y-%m-%d %H:%M:%S.%f")

    outstring = str(version)+" "+str(timestamp)+" "+str(data)+" "+str(min_strikes)+" "+str(noise_floor)+"\n"

    print(outstring)

    f.write(outstring)

    f.flush



def handle_interrupt(channel):

    time.sleep(0.003)

    global sensor

    reason = sensor.get_interrupt()

    if reason == 0x01:

        print("Noise level too high - adjusting")

        sen=sensor.raise_noise_floor()
        insertVariblesIntoTable(sen ,"Online",1)
    elif reason == 0x04:

        print("Disturber detected - masking")

        sensor.set_mask_disturber(True)
        insertVariblesIntoTable("Disturber detected - masking","Online",1)
    elif reason == 0x08:

        now = datetime.now()

        distance = sensor.get_distance()

        if 0 < distance < 63:

            log_raw_data(distance)
            insertVariblesIntoTable( log_raw_data(distance),Online,1)

        if distance == 1:

            print("Overhead lightning detected - distance = " + str(distance) + " km at %s ") % now.strftime("%H:%M:%S.%f")[:-3],now.strftime("%Y-%m-%d")
            insertVariblesIntoTable( log_raw_data(distance),"online",1)
        elif 40 < distance < 63:

            print("Distant lightning detected - distance = " + str(distance) + " kms at %s") % now.strftime("%H:%M:%S.%f")[:-3],now.strftime("%Y-%m-%d")
            insertVariblesIntoTable( "Distant lightning detected - distance = " + str(distance) + " kms at %s","Online",1)
        elif 2 <= distance <= 40:

            print("Lightning detected - distance = " + str(distance) + " kms at %s") % now.strftime("%H:%M:%S.%f")[:-3],now.strftime("%Y-%m-%d")
            insertVariblesIntoTable("Lightning detected - distance = " + str(distance) + " kms at %s", "Online",1)
        else:

            print("Invalid data; distance out of range.")



irq_pin = 22

cs_pin = 24



GPIO.setup(irq_pin, GPIO.IN)

GPIO.add_event_detect(irq_pin, GPIO.RISING, callback=handle_interrupt)



def read_settings():

    global min_strikes, noise_floor

    min_strikes = sensor.get_min_strikes()

    noise_floor = sensor.get_noise_floor()



def print_settings():

    print("Minimum allowed strikes is " + str(min_strikes))

    print("Current noise floor is " + str(noise_floor))



running = True



try:

    print("Lightning Detection Monitor Script - v0.1")

    print("  Monitor Status: ONLINE")

    print("")
    insertVariblesIntoTable("Lightning Detection Monitor", "Online",1)
    ## log raw data to file

    #f=open('AS3935-data.txt','a')

    #read_settings()



    while running:

        time.sleep(1.0)



except KeyboardInterrupt:

    print("  Monitor Status: OFFLINE")

    #print_settings()

    print("")



finally:

    GPIO.cleanup() # clean up GPIO on CTRL+C exit

    #f.close()
