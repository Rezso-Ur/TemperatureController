import time
import RPi.GPIO as GPIO
import board
import busio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

from adafruit_ht16k33 import segments
i2c = busio.I2C(board.SCL, board.SDA)
display = segments.Seg7x4(i2c)
display.fill(0)

pinRed = 25
pinGreen = 18
pinWhite = 5
pinBlue = 12
pinSwitchState = 24
pinSwitchLimit = 23
direction = 1

GPIO.setup(pinRed, GPIO.OUT)
GPIO.setup(pinWhite, GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue, GPIO.OUT)
GPIO.setup(pinSwitchState, GPIO.IN)
GPIO.setup(pinSwitchLimit, GPIO.IN)

state="red" #melyik szoba/limit
tempMin = 19
temperature = tempMin # Aktuális hőmérséklet a kiválasztott szobában
tempMax = 26
tempDiff = 0.1
tempStep = 1 
tempLimit = tempMin
print(f"szoba: {state}")


        
GPIO.output(pinRed, 0)
GPIO.output(pinWhite, 0)
GPIO.output(pinGreen, 0)

# Kigyújtja a ledet
def setLed(state):
    GPIO.output(pinRed, 0)
    GPIO.output(pinWhite, 0)
    GPIO.output(pinGreen, 0)
    if state =="red":
        GPIO.output(pinRed, 1)
    elif state =="white":
        GPIO.output(pinWhite, 1)
    elif state =="green":
        GPIO.output(pinGreen, 1)
    

def stateRoom(channel):
    global state
    if state =="red":
        state="white"
    elif state =="white":
        state="green"
    elif state =="green":
        state="limit"
    elif state =="limit":
        state="red"    
    setLed(state)
    print(f"szoba: {state}")

def setLimit(channel):
    global direction
    global tempLimit
    if tempLimit > tempMax:
        direction = -1
    if tempLimit < tempMin:
        direction = 1 
    tempLimit = tempLimit+direction
    if state=="limit":
        tempDisplay(tempLimit * 1.00)
    

def heatingHandler(tempRed, tempWhite, tempGreen):
    
    if state =="red":
        temp = tempRed
    elif state =="white":
        temp = tempWhite
    elif state =="green":
        temp = tempGreen
    elif state =="limit":
        temp = tempLimit * 1.00   
    tempDisplay(temp)
        

        
def tempDisplay(temp):
    tempString = str(temp)[:5].ljust(5,"0")
    display.print(tempString)
    
def  heater():
    if temperature + tempDiff > tempLimit:
        #Kályha lekapcsol
        GPIO.output(pinBlue, 0)
    elif temperature - tempDiff < tempLimit:
        #Kályha bekapcsol
        GPIO.output(pinBlue, 1)

# Jobb kapcsoló: szaba váltó
GPIO.add_event_detect(pinSwitchState, GPIO.RISING, callback=stateRoom, bouncetime=300)

# Bal: hőmérséklet limit
GPIO.add_event_detect(pinSwitchLimit, GPIO.RISING, callback=setLimit, bouncetime=300)
setLed(state)
limit = tempLimit
def TempIn(color):
    global temperature 
    id="28-00000cac301d"
    if color=="green":
        id="28-00000caca712"
    if color=="white":
        id="28-00000cac301d"
    if color=="red":
        id="28-00000caca74d"
    tempfile = open(f"/sys/bus/w1/devices/{id}/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    return temperature


try:
    while True:

        tempRed=TempIn("red")
        tempGreen=TempIn("green")
        tempWhite=TempIn("white")

        heatingHandler(tempRed, tempWhite, tempGreen)
        print (f"limit: {tempLimit}°C (Aktuális Szoba: {state}: {TempIn(state)}°C) R: {tempRed}°C, W: {tempWhite}°C, G: {tempGreen}°C")
        heater() #Kályhakezelő
        time.sleep(0.1)

except KeyboardInterrupt:
    display.fill(0)
    GPIO.cleanup()
    print("program vége")
    

