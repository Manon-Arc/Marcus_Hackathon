import time
import machine

broche_sortie = machine.Pin(4, machine.Pin.OUT)
pwm = machine.PWM(broche_sortie)



pwm.duty(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)


pwm.duty(512)
time.sleep(0.75)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.75)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.75)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)


pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)
pwm.duty(512)
time.sleep(0.3)
pwm.duty(0)
broche_sortie.value(0)
time.sleep(0.3)