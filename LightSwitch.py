#!/usr/bin/python

import time
import pigpio
from phue import Bridge

b = Bridge("192.168.1.79")


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

def cbf(GPIO, level, tick):
   global u
   global d 
   diff = pigpio.tickDiff(last[GPIO], tick)
   print("G={} l={} t={} d={}".format(GPIO, level, tick, diff)) 
   last[GPIO] = tick
   if diff > 5000:
      if GPIO == 5:
         if level == 1:
            d = d + 1
            print("DOWN Release", d)
            pi.write(2,1)
            pi.write(3,0)
            pi.write(4,0)
            b.set_group(11,"on",False) #15 downstairs
            #b.run_scene("Hallway", "Bright")

      if level == 0:
            print("DOWN")
            pi.write(2,0)
            pi.write(3,1)
            pi.write(4,0)
      if GPIO == 6:
         if level == 1:
            u = u + 1 
            print("UP Release ",u)
            pi.write(3,0)
            pi.write(4,1)
            pi.write(2,0)
            
            #b.set_group(11,"on", True)
            #b.run_scene("Hallway", "Nightlight")

            #b.run_scene("Downstairs", "Normal")
         if level == 0:
            print("UP")
            pi.write(2,0)
            pi.write(3,1)
            pi.write(4,0)
            b.set_group(11,"on", True)

   


cb.append(pi.callback(5, pigpio.EITHER_EDGE, cbf))
cb.append(pi.callback(6, pigpio.EITHER_EDGE, cbf))

try:
   while True:
      time.sleep(60)
except KeyboardInterrupt:
   print("\nTidying up")
   for c in cb:
      c.cancel()

pi.stop()

