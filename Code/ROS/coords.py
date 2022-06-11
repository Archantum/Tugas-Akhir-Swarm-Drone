#!/usr/bin/env python

import rospy
from swarm.msg import control, channels, coords
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix

pub=rospy.Publisher('/coords',coords,queue_size=10)
def callback1(msg):
    global hdg1
    hdg1 = msg.data
def callback2(msg):
    global hdg2
    hdg2 = msg.data
def callback3(msg):
    global hdg3
    hdg3 = msg.data
def callback4(msg):
    global alt1,lat1,lon1
    alt1 = msg.altitude
    lat1 = msg.latitude
    lon1 = msg.longitude
def callback5(msg):
    global alt2,lat2,lon2
    alt2 = msg.altitude
    lat2 = msg.latitude
    lon2 = msg.longitude
def callback6(msg):
    global alt1,lat1,lon1, alt2, lat2, lon2, hdg1, hdg2, hdg3
    alt3 = msg.altitude
    lat3 = msg.latitude
    lon3 = msg.longitude
    dat = coords();
    dat.hdg1 = hdg1
    dat.hdg2 = hdg2
    dat.hdg3 = hdg3
    dat.alt1 = alt1
    dat.alt2 = alt2
    dat.alt3 = alt3
    dat.lat1 = lat1
    dat.lat2 = lat2
    dat.lat3 = lat3
    dat.lon1 = lon1
    dat.lon2 = lon2
    dat.lon3 = lon3
    pub.publish(dat)

def main():
    rospy.init_node('Coords')
    rospy.Subscriber("/mavros1/mavros/global_position/compass_hdg", Float64, callback1)
    rospy.Subscriber("/mavros2/mavros/global_position/compass_hdg", Float64, callback2)
    rospy.Subscriber("/mavros3/mavros/global_position/compass_hdg", Float64, callback3)
    rospy.Subscriber("/mavros1/mavros/global_position/global", NavSatFix, callback4)
    rospy.Subscriber("/mavros2/mavros/global_position/global", NavSatFix, callback5)
    rospy.Subscriber("/mavros3/mavros/global_position/global", NavSatFix, callback6)


    rospy.spin()

if __name__ == '__main__':
    main()
