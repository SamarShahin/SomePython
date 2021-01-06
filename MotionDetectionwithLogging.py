from gpiozero import MotionSensor
from datetime import datetime
import RPi.GPIO as GPIO


pir = MotionSensor(23)
dateandtime=datetime.now()
dateandtimeofnomotion=datetime.now()
dateandtimeofnomotionintxt=str(dateandtimeofnomotion)
dateandtimeofstartdetect=datetime.now()
dateandtimeofstartdetectintxt=str(dateandtimeofstartdetect)
dateofnomotionintxt=str(dateandtimeofnomotion)
timeofnomotionintxt=str(dateandtimeofnomotion)

logfile="/home/pi/Desktop/Python Projects/MotionDetection/Motionlog.csv"
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 23

GPIO.setup(INPUT_PIN, GPIO.IN)
if (GPIO.input(INPUT_PIN) == True):
    print("starting at motion detected")
if (GPIO.input(INPUT_PIN) == False):
    print("starting at motion detected flag clear")

while True:
    
    
    
    pir.wait_for_motion() 
          
    dateandtime=datetime.now()
    dateandtimeintxt=dateandtime.strftime("%d%b-%Y_%Hh-%Mm-%Ss")    
    dateandtimeofstartdetect=dateandtime
    durationinnomotiondetectionstate=dateandtimeofstartdetect-dateandtimeofnomotion
    durationinnomotiondetectionstateinseconds=durationinnomotiondetectionstate.total_seconds()
    durationinnomotiondetectionstateintxt=str(durationinnomotiondetectionstateinseconds)
    
    startlogtext="0," + dateofnomotionintxt + ","+ timeofnomotionintxt+","+ durationinnomotiondetectionstateintxt+","+dateandtimeofnomotionintxt+"\n"
    dateandtimeofstartdetectintxt=str(dateandtime)#("%d-%m-%Y (%H:%M:%S)")
    dateofstartdetectintxt=dateandtime.strftime("%d-%m-%Y")
    timeofstartdetectintxt=dateandtime.strftime("%H:%M:%S")
    filewrite=open(logfile,"a")
    filewrite.write(startlogtext)
    filewrite.close()
    print("motion detected flag is high at: "+dateandtimeintxt)
          
    
    pir.wait_for_no_motion()
    
    dateandtimeofnomotion=datetime.now()    
    durationinmotiondetectionstate=dateandtimeofnomotion-dateandtimeofstartdetect
    durationinmotiondetectionstateinseconds=durationinmotiondetectionstate.total_seconds()
    durationinmotiondetectionstateintxt=str(durationinmotiondetectionstateinseconds)
    dateandtimeofnomotionintxt=str(dateandtimeofnomotion)    
    startlogtext="1," + dateofstartdetectintxt + ","+ timeofstartdetectintxt+","+ durationinmotiondetectionstateintxt+ ","+dateandtimeofstartdetectintxt+"\n"
    dateofnomotionintxt=dateandtimeofnomotion.strftime("%d-%m-%Y")
    timeofnomotionintxt=dateandtimeofnomotion.strftime("%H:%M:%S")
    print("motion detection flag cleared at: "+dateandtimeofnomotionintxt)
    filewrite=open(logfile,"a")
    filewrite.write(startlogtext)
    filewrite.close()
   


