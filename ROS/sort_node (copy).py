#!/usr/bin/env python

import rospy
from swarm.msg import control, channels
from std_msgs.msg import String, Float64
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
    global output,ch1,ch2,ch3,ch4,ch5,ch6
    if output == 0:
    	output = 0
    elif output == 1:
    	if ch6<1000:
    	    output = 2
	elif 1000<ch6<2000:
	    output = 3
	elif ch6>2000:
	    output = 4
   # chan = control();
   # mode = output
   # ch1 = msg.data1
   # ch2 = msg.data2
   # ch3 = msg.data3
   # ch4 = msg.data4
   # ch5 = msg.data5
   #ch6 = msg.data6
   # pub.publish(chan)

def callback3(msg):
    global hdg1
    hdg1 = msg.data

def callback4(msg):
    global hdg2
    hdg2 = msg.data

def callback5(msg):
    global hdg3
    hdg3 = msg.data

def callback6(msg):
    global alt1
    alt1 = msg.altitude

def callback7(msg):
    global alt2
    alt2 = msg.altitude


def callback8(msg):
    global alt3, alt2, alt1, hdg1, hdg2, hdg3, output
    alt3 = msg.altitude
    chan=control();
    chan.ch1=ch1
    chan.ch2=ch2
    chan.ch3=ch3
    chan.ch4=ch4
    chan.ch5=ch5
    chan.ch6=ch6
    chan.hdg1=hdg1
    chan.hdg2=hdg2
    chan.hdg3=hdg3
    chan.alt1=alt1
    chan.alt2=alt2
    chan.alt3=alt3
    pub.publish(chan)




def main():
    rospy.init_node('Sort')
    rospy.Subscriber("/FlightMode",String,callback1)
    rospy.Subscriber("/chatter", channels, callback2)
    rospy.Subscriber("/mavros1/mavros/global_position/compass_hdg", Float64, callback3)
    rospy.Subscriber("/mavros2/mavros/global_position/compass_hdg", Float64, callback4)
    rospy.Subscriber("/mavros3/mavros/global_position/compass_hdg", Float64, callback5)
    rospy.Subscriber("/mavros1/mavros/global_position/global", NavSatFix, callback6)
    rospy.Subscriber("/mavros2/mavros/global_position/global", NavSatFix, callback7)
    rospy.Subscriber("/mavros3/mavros/global_position/global", NavSatFix, callback8)

    rospy.spin()

if __name__ == '__main__':
    main()
