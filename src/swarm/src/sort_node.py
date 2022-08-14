#!/usr/bin/env python

import rospy
from swarm.msg import control, channels
from std_msgs.msg import String
output = 0 

pub=rospy.Publisher('/Sort',control,queue_size=10)
def callback1(msg):
    mode = msg.data
    global output
    rospy.loginfo('mode = {}'.format(mode))
    if mode == "Swarm" :
    	output = 0
    else:
        output = 1
    return output

def callback2(msg):
    ch6 = msg.data6
    global output
    if output == 0:
    	output = 0
    elif output == 1:
    	if ch6<1000:
    	    output = 2
	elif 1000<ch6<2000:
	    output = 3
	elif ch6>2000:
	    output = 4
    chan = control();
    chan.mode = output
    chan.ch1 = msg.data1
    chan.ch2 = msg.data2
    chan.ch3 = msg.data3
    chan.ch4 = msg.data4
    chan.ch5 = msg.data5
    chan.ch6 = msg.data6
    pub.publish(chan)

def main():
    rospy.init_node('Sort')
    rospy.Subscriber("/FlightMode",String,callback1)
    rospy.Subscriber("/chatter", channels, callback2)
    rospy.spin()

if __name__ == '__main__':
    main()
