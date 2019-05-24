import RPi.GPIO as GPIO
import time

#initialize port
backMotorInput1 = 7
backMotorInput2 = 11
frontMotorInput1 = 13
frontMotorInput2 = 15
backMotorEn = 12
frontMotorEn = 16
speed = 30

#initialize model
GPIO.setmode(GPIO.BOARD)

#set output port
GPIO.setup(backMotorInput1, GPIO.OUT)
GPIO.setup(backMotorInput2, GPIO.OUT)
GPIO.setup(frontMotorInput1, GPIO.OUT)
GPIO.setup(frontMotorInput2, GPIO.OUT)
GPIO.setup(frontMotorEn, GPIO.OUT)
GPIO.setup(backMotorEn, GPIO.OUT)
backMotorPWM = GPIO.PWM(backMotorEn, 100)
backMotorPWM.start(0)


def carMoveForward():
	GPIO.output(backMotorEn, GPIO.HIGH)
	GPIO.output(backMotorInput1, GPIO.HIGH)
	GPIO.output(backMotorInput2, GPIO.LOW)
	backMotorPWM.ChangeDutyCycle(speed)


def carMoveBackward():
	GPIO.output(backMotorEn, GPIO.HIGH)
	GPIO.output(backMotorInput1, GPIO.LOW)
	GPIO.output(backMotorInput2, GPIO.HIGH)
	


def carTurnRight():
	GPIO.output(frontMotorEn, GPIO.HIGH)
	GPIO.output(frontMotorInput1, GPIO.LOW)
	GPIO.output(frontMotorInput2, GPIO.HIGH)
	


def carTurnLeft():
	GPIO.output(frontMotorEn, GPIO.HIGH)
	GPIO.output(frontMotorInput1, GPIO.HIGH)
	GPIO.output(frontMotorInput2, GPIO.LOW)
	
def carStop():
	GPIO.output(frontMotorInput1, GPIO.HIGH)
	GPIO.output(frontMotorInput2, GPIO.HIGH)
	GPIO.output(backMotorInput1, GPIO.HIGH)
	GPIO.output(backMotorInput2, GPIO.HIGH)

def carTurnStraight():
	GPIO.output(frontMotorEn, GPIO.LOW)

def cleanGPIO():
	GPIO.cleanup()
	backMotorPWM.stop()

carTurnLeft()
time.sleep(2)
cleanGPIO()