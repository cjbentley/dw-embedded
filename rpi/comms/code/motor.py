from network import connect, command
import RPi.GPIO as GPIO
import time

s = connect()
left_pwm = 13
left_dir = 5
right_pwm=18
right_dir=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_pwm, GPIO.OUT)
GPIO.setup(left_dir, GPIO.OUT)
GPIO.setup(right_pwm, GPIO.OUT)
GPIO.setup(right_dir, GPIO.OUT)

motorL = GPIO.PWM(left_pwm,1000)
motorR = GPIO.PWM(right_pwm,1000)

motorL.start(0)
motorR.start(0)

while True:
	L, R = command(s)
	print(L,R)

	if L<0:
		GPIO.output(left_dir,0)
	else:
		GPIO.output(left_dir,1)
	if R<0:
		GPIO.output(right_dir,0)
	else:
		GPIO.output(right_dir,1)


	motorL.ChangeDutyCycle(abs(L))
	motorR.ChangeDutyCycle(abs(R))
	#time.sleep(0.01)




