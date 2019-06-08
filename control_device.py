import serial
port=serial.Serial("/dev/ttyAMA0", baudrate=9600,write_timeout=None)
port.flushOutput()
if (port.isOpen()):  # To check port status
    print "True"
else:
    print "False"
# store controlling digits to bytes
# digits under square brackets may vary according to one's need
x1=serial.to_bytes([10])
x2=serial.to_bytes([ 01])
x3=serial.to_bytes([ 01])
x4=serial.to_bytes([ 06])
x5=serial.to_bytes([ 06])
x6=serial.to_bytes([ 04])
x7=serial.to_bytes([ 03])
x8=serial.to_bytes([ 02])
x9=serial.to_bytes([ 100])
x10=serial.to_bytes([ 00])
values=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10
#print values
port.write(values)  #sending bytes
port.flush()
#print "done"
port.close()

