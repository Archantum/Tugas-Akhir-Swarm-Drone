#!/usr/bin/env python

import rospy
from swarm.msg import channels, control
from std_msgs.msg import Int16

pub=rospy.Publisher('/FlightMode',control,queue_size=10)
def callback(msg):
    ch1 = msg.data1
    ch2 = msg.data2
    ch3 = msg.data3
    ch4 = msg.data4
    ch5 = msg.data5
    ch6 = msg.data6

    rospy.loginfo('ch1:{},ch2:{},ch3:{},ch4:{},ch5:{},ch6:{}'.format(ch1,ch2,ch3,ch4,ch5,ch6))
    if ch5 > 1000:
    	mode = 0
    elif:
        if ch6<1000:
    	    mode = 2
	elif 1000<ch6<2000:
	    mode = 3
	elif ch6>2000:
	    mode = 4
    dat = control();
    dat.ch1=ch1
    dat.ch2=ch2
    dat.ch3=ch3
    dat.ch4=ch4
    dat.ch5=ch5
    dat.ch6=ch6
    dat.mode=mode
    pub.publish(dat)


def main():
    rospy.init_node('CekMode')
    rospy.Subscriber("/chatter",channels,callback)
    rospy.spin()

if __name__ == '__main__':
    main()
