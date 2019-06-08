import serial
import MySQLdb
port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
data=[]
d1 = ['\x01','\x01','\x06','\x06']
name = "Device 1"
while True:
    while(port.inWaiting()):
        ch = port.read(1)
        data.append(ch)
    if (len(data)>30):
        #print received data to console
        print(data)
        # or store the data to database for remote access of status
        #here only change in status of device is stored to database
        if ((data[5:9]== d1) and (data[19:20]=='\x40') and (data[26:27]=='\x81')):
            try:#Open database connection
                db = MySQLdb.connect("IP_address","Database_Username","Database_Password","database_name" )
                #prepare a cursor object using cursor() method
                cursor = db.cursor()
                #execute SQL query using execute() method.
                cursor.execute('INSERT INTO '"table_name"' VALUES("%s",current_date())'%(name))
                db.commit()
            except:
                continue
            finally:
                db.close()
        data =[]       # delete all received data
    elif (len(data)<6):
        data=[]
