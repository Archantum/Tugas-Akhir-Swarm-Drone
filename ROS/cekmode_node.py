#!/usr/bin/env python

import rospy
from swarm.msg import channels
from std_msgs.msg import String

pub=rospy.Publisher('/FlightMode',String,queue_size=10)
def callback(msg):
    ch1 = msg.data1
    ch2 = msg.data2
    ch3 = msg.data3
    ch4 = msg.data4
    ch5 = msg.data5
    ch6 = msg.data6

    rospy.loginfo('ch1:{},ch2:{},ch3:{},ch4:{},ch5:{},ch6:{}'.format(ch1,ch2,ch3,ch4,ch5,ch6))
    if ch5 > 1000:
    	mode = ('Swarm')
    else:
        mode = ('Manual')
    pub.publish(mode)

def main():
    rospy.init_node('CekMode')
    rospy.Subscriber("/chatter",channels,callback)
    rospy.spin()

if __name__ == '__main__':
    main()
