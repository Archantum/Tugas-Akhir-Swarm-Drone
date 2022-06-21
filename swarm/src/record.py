#!/usr/bin/env python

from codecs import latin_1_encode
from logging import shutdown
import time
import rospy
from swarm.msg import control, channels, coords
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix
hdg1=0
alt1=0
lat1=0
lon1=0
hdg2=0
alt2=0
lat2=0
lon2=0

def callback1(msg):
    global hdg1
    hdg1 = msg.data
def callback2(msg):
    global hdg2
    hdg2 = msg.data
#def callback3(msg):
    #global hdg3
    #hdg3 = msg.data
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
#def callback6(msg):
    #global alt1,lat1,lon1, alt2, lat2, lon2, hdg1, hdg2, hdg3
    #alt3 = msg.altitude
    #lat3 = msg.latitude
    #lon3 = msg.longitude


    rospy.loginfo('\nhdg1:{}\nalt1:{}\nlat1:{}\nlon1:{}\nhdg2:{}\nalt2:{}\nlat2:{}\nlon2:{}\n'.format(hdg1,alt1,lat1,lon1,hdg2,alt2,lat2,lon2))

    #outfile = open("tes.txt", 'w')

    
       

    #pub.publish(dat)

def main():
    rospy.init_node('FlightLog')
    #rate=rospy.Rate(1)
    pub=rospy.Publisher('/log',Float64,queue_size=10)
    heading = float()
    f = open('data.txt', 'w')
    counter = 0
    while not rospy.is_shutdown():
        rospy.Subscriber("/mavros1/mavros/global_position/compass_hdg", Float64, callback1)
        rospy.Subscriber("/mavros2/mavros/global_position/compass_hdg", Float64, callback2)
        #rospy.Subscriber("/mavros3/mavros/global_position/compass_hdg", Float64, callback3)
        rospy.Subscriber("/mavros1/mavros/global_position/global", NavSatFix, callback4)
        rospy.Subscriber("/mavros2/mavros/global_position/global", NavSatFix, callback5)
        #rospy.Subscriber("/mavros3/mavros/global_position/global", NavSatFix, callback6)
        
       
        counter = counter + 1

        pub.publish(hdg2)
        f = open('data.txt', 'a')
        f.write("TimeStamp = "+str(counter)+"\n")
        f.write("=======Drone 1=======\n")
        f.write("Heading1 = ")
        f.write(str(hdg1) + "\n")
        f.write("Latitude1 = ")
        f.write(str(alt1) + "\n")
        f.write("Longitude1 = ")
        f.write(str(lat1) + "\n")
        f.write("Longitude1 = ")
        f.write(str(lon1) + "\n\n")
        f.write("=======Drone 2=======\n")
        f.write("Heading2 = ")
        f.write(str(hdg2) + "\n")
        f.write("Latitude2 = ")
        f.write(str(alt2) + "\n")
        f.write("Longitude2 = ")
        f.write(str(lat2) + "\n")
        f.write("Longitude2 = ")
        f.write(str(lon2) + "\n\n")
        #time.sleep(2)
        #rate.sleep()
        time.sleep(1)
        #rospy.spin()

if __name__ == '__main__':
    main()
