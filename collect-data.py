import serial
import time

###
# Part 1: Setup and open the serial port
###


#portName='/dev/cu.usbserial-14430'
portName='COM4'
baudRate = 9600

ser = serial.Serial(portName,baudRate)
print("Opening port "+ ser.name)

if ser.is_open==True:
    print("Success!")
else:
    print("Unable to open port :(")

###
# Part 2: Give the user a few seconds to get ready...
###
print("Get ready to press....Starting in five seconds....")
startTime = currentTime = int(time.time())
while abs(currentTime-startTime) < 5:

    # keep track of current time
    currentTime = int(time.time())

###
# Part 3: Read data from the serial port for a while. Write results to a file
###

#print("Running data collection for 2s...")
startTime = currentTime = int(time.time())

#create a file called mydata.csv and open it for writing (w)
my_file = open('mydata.csv','w')

#tell the user we're about to start
print("Press toe against sensor!!!")

#run this loop for 2 seconds
while abs(currentTime-startTime) < 2:

    ##read until line and strip out \r\n terminators
    bytes = ser.readline()
    #decode bytes into string
    line = bytes.decode('utf-8')
    line = line.replace('\r','').replace('\n','')

    #print out the line from the board
    print(line)

    #save the data to a list for future writing
    my_file.write(line+'\r')

    #keep track of current time
    currentTime=int(time.time())


print("Show's over. Close the port!")

#close the serial port
ser.close()

#close the file
my_file.close()

