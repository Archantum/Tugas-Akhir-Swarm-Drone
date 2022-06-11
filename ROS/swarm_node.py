#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix

def callback(msg):
    latm = msg.latitude
    lonm = msg.longitude
    altm = msg.altitude
    rospy.loginfo('latm :{}, lonm: {}, altm: {}'.format(latm, lonm, altm))
    lats = msg.latitude
    lons = msg.longitude
    alts = msg.altitude
    rospy.loginfo('lats :{}, lons: {}, alts: {}'.format(lats, lons, alts))

def main():
    rospy.init_node('coordinate')
    rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
    rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
    rospy.spin()

if __name__ == '__main__':
    main()



