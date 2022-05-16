import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 16
GPIO_ECHO = 18
BUZZER_PIN = 40

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.output(BUZZER_PIN,True)
buzzer = GPIO.PWM(BUZZER_PIN,0.1)
buzzer.start(1)

def measure_distance():
    print("Start measuring...")
    GPIO.output(GPIO_TRIGGER,True)
    print("Settling sensor")
    time.sleep(1)
    GPIO.output(GPIO_TRIGGER,False)

    while (GPIO.input(GPIO_ECHO) == 0):
        pulse_start = time.time()
    while (GPIO.input(GPIO_ECHO) == 1):
        pulse_end = time.time()
        
    duration = pulse_end - pulse_start
    distance = round(duration*17000,2)
    print("Measure done")
    return distance

def define_frequency(distance):
    if distance > 16:
        return 0.25
    elif distance > 12:
        return 0.5
    elif distance>8:
        return 1
    elif distance > 4:
        return 2
    elif distance >= 0:
        return 3

try:
    while 1 :
        distance = measure_distance()
        print(f"Distance : {distance} cm")
 
        frequency = define_frequency(distance)
        buzzer.ChangeFrequency(frequency)
        if frequency == 0.25:
            print("Place the object")
        time.sleep(3)
except KeyboardInterrupt:
        GPIO.cleanup()
        buzzer.stop()



