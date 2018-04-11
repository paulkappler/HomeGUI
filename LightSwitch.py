#!/usr/bin/python

import time
import pigpio
from phue import Bridge

b =  Bridge("192.168.1.79")

b2 = Bridge("192.168.1.78")

pi = pigpio.pi()

if not pi.connected:
   exit()


pi.set_mode(2, pigpio.OUTPUT)
pi.set_mode(3, pigpio.OUTPUT)
pi.set_mode(4, pigpio.OUTPUT)
u=0
d=0
cb = []
last = [0]*32
lastCommand = 0
down = False
up = False


pi.write(2,1)
pi.write(3,1)
pi.write(4,1)
 
def cbf(GPIO, level, tick):
   global down
   global up
   global u
   global d 
   global lastCommand
   #Diff is the time since the change in GPIO change
   diff = pigpio.tickDiff(last[GPIO], tick)
   print("G={} l={} t={} d={}".format(GPIO, level, tick, diff)) 
   last[GPIO] = tick

   #Only active if we have not seen a change in this pin recently
   if diff > 5000:
      commandDiff = pigpio.tickDiff(lastCommand, tick)
      lastCommand = tick
      if GPIO == 5:
         if level == 1:
            d = d + 1
            print("DOWN Release", d)
            down = False
            pi.write(2,1)
            pi.write(3,0)
            pi.write(4,0)
            if commandDiff > 2000000:
                b.run_scene("Downstairs", "Dim")
            else:
                #Downstairs Off
                b.set_group(15,"on",False)
                b2.set_group(0,"on",False)

      if level == 0:
            print("DOWN")
            down = True
            pi.write(2,0)
            pi.write(3,1)
            pi.write(4,0)
      if GPIO == 6:
         if level == 1:
            u = u + 1 
            print("UP Release ",u)
            up = False
            pi.write(3,0)
            pi.write(4,1)
            pi.write(2,0)
            

         if level == 0:
            print("UP")
            up = True
            pi.write(2,0)
            pi.write(3,1)
            pi.write(4,0)
            b.run_scene("Downstairs", "Normal")

   


cb.append(pi.callback(5, pigpio.EITHER_EDGE, cbf))
cb.append(pi.callback(6, pigpio.EITHER_EDGE, cbf))

try:
   while True:
      if down:
          time.sleep(0.1)
      else:
          time.sleep(1)
      tick = pi.get_current_tick()
      commandDiff = pigpio.tickDiff(lastCommand, tick)
      if down:
          if commandDiff > 2000000:
            pi.write(3,0)
            pi.write(4,1)
            pi.write(2,0)
except KeyboardInterrupt:
   print("\nTidying up")
   for c in cb:
      c.cancel()

pi.stop()

