#!/usr/bin/env python

from logging import shutdown
import rospy
from swarm.msg import coords
from std_msgs.msg import Float64, String
import time

hdg1=0
hdg2=0
hdg3=0
alt1=0
alt2=0
alt3=0
lat1=0
lat2=0
lat3=0
lon1=0
lon2=0
lon3=0

if rospy is not shutdown:
    f = open("flight_log.txt", "w")
    def callback1(msg):
        global alt1,lat1,lon1, alt2, lat2, lon2, hdg1, hdg2, hdg3
        f.write("Drone 1\n")
        hdg_1 = "hdg : %s \n" % hdg1()
        f.write(hdg_1)
        alt_1 = "alt : %s \n" % alt1()
        f.write(alt_1)
        lat_1 = "alt : %s \n" % lat1()
        f.write(lat_1)
        lon_1 = "alt : %s \n" % lon1()
        f.write(lon_1)
        f.write("\n")

        f.write("Drone 2\n")
        hdg_2 = "hdg : %s \n" % hdg2()
        f.write(hdg_2)
        alt_2 = "alt : %s \n" % alt2()
        f.write(alt_2)
        lat_2 = "alt : %s \n" % lat2())
        f.write(lat_2)
        lon_2 = "alt : %s \n" % lon2()
        f.write(lon_2)
        f.write("\n")
        
        time.sleep(3)


def main():
    rospy.init_node('Record')
    rospy.Subscriber('/coords',coords, callback1)

    rospy.spin()

if __name__ == '__main__':
    main()
