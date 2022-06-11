#!/usr/bin/env python

import rospy
from swarm.msg import channels
from std_msgs.msg import Int16

pub=rospy.Publisher('/ceks',Int16,queue_size=10)

def callback2(msg):
    ch4 = msg.data4
    rospy.loginfo("data:{}".format(ch4))
    pub.publish(ch4)


def main():
    rospy.init_node('cek')
    rospy.Subscriber("/chatter", channels, callback2)
    rospy.spin()

if __name__ == '__main__':
    main()
