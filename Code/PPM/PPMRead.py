#!/usr/bin/env python

# PPM_to_servo.py
# 2019-10-09
# Public Domain

import time
import pigpio # http://abyz.me.uk/rpi/pigpio/python.html

IN_GPIO=4 # the PPM input GPIO

start_of_frame = False
last_tick = None
arr =[]
count = 0
def cbf(gpio, level, tick):
   global start_of_frame, channel, last_tick, arr
   if last_tick is not None:
      diff = pigpio.tickDiff(last_tick, tick)
      if diff > 5000: # start of frame
         start_of_frame = True
      else:
         if start_of_frame:
            if len(arr) == 8:
               print arr
               arr = []
            else:
               arr.append(count)
                          
            #start_of_frame = False
            #last_tick = None
   last_tick = tick
   
pi = pigpio.pi()
if not pi.connected:
   exit()

pi.set_mode(IN_GPIO, pigpio.INPUT)

cb = pi.callback(IN_GPIO, pigpio.RISING_EDGE, cbf)

time.sleep(60)

#cb.cancel()

pi.stop()
