import serial 

class device:
    import serial
    
    def __init__(self,port):
        self.port = port
        self.speed = 115200
        self.timeout = 2
        self.serial = serial.Serial(self.port, self.speed, timeout=self.timeout)
        print("Connected to: " + self.serial.portstr)

    def closePort(self):
        self.serial.close()

    def send(self,command):
        #print("Command to send")
        #print(command)
        #print('\n')
        try:
            self.serial.write(command)
        except:
            self.serial.close()
        #print("Command sent: ")
        #print(command)
    
    def read(self):
        from textwrap import wrap   
        #print("Receiving")
        try:
            received = (self.serial.readline().hex()) 
        except: 
            print("Exception happend")
            self.serial.close()

        #print("Received:")
        #print(received)
        aux = wrap(received,2)

        aux1 = bytearray()

        for item in aux:
            aux1.append(int(item,16))

        return aux1


