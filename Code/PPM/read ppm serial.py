import serial

if __name__== '__main__':
    ser = serial.Serial ('com5', 9600, timeout=1)
    ser.flush
    
    while True :
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip().split("\t")
            print (line)
            if (len(line) < 6):
                continue
            else:
                ch1 = line[0]
                ch2 = line[1]
                ch3 = line[2]
                ch4 = line[3]
                ch5 = line[4]
                ch6 = line[5]
            
            
