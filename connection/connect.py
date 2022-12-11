import sys
import glob
import serial
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    
        print("{}: {} [{}]".format(port, desc, hwid))
        desc = desc[:-8]
        x = hwid.find("PID")
        hwid = hwid[x+4:x+8]

        if hwid == "2341":
            ser=serial.Serial(port, 9600)
            break

while True:
    s = ser.readline()
    s = s.decode()
    s = s[:-2]
    s = s.split("|")
    print(s)



"""

def serial_ports():
    
    Lists all COM ports names

    #:raises EnvironmentalError:
        On unsupported platforms
    #:returns:
        A list of all uvailable ports
    
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

print(serial_ports())


ser=serial.Serial('COM14', 9600)

while True:
    s = ser.readline()
    s = s.decode()
    s = s[:-2]
    s = s.split("|")
    print(s)

"""