#!/usr/bin/env python

from codecs import latin_1_encode
from logging import shutdown
import time
import rospy
from swarm.msg import control, channels, coords, compute
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
d12=0
b12=0
alt12=0
hdg12=0


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
def callback7(msg):
    global d12, b12, alt12, hdg12
    d12 = msg.d12
    b12 = msg.b12
    alt12 = msg.alt12
    hdg12 = msg.hdg12
    


    rospy.loginfo('\nhdg1:{}\nalt1:{}\nlat1:{}\nlon1:{}\nhdg2:{}\nalt2:{}\nlat2:{}\nlon2:{}\n\nd12:{}\nb12:{}\nalt12:{}\nhdg12:{}\n'.format(hdg1,alt1,lat1,lon1,hdg2,alt2,lat2,lon2,d12,b12,alt12,hdg12))

    #outfile = open("tes.txt", 'w')

    
       

    #pub.publish(dat)

def main():
    rospy.init_node('FlightLog')
    #rate=rospy.Rate(1)
    pub=rospy.Publisher('/log',Float64,queue_size=10)
    heading = float()
    f = open('log.txt', 'w')

    f = open('log.txt', 'a')
    f.write("Drone1, Hdg1, Alt1, Lat1, Lon1, ")
    f.write("Drone2, Hdg2, Alt2, Lat2, Lon2, ")
    f.write("Count, Distance12, Bearing12, Altitude12, Heading12\n")

    counter = 0
    while not rospy.is_shutdown():
        rospy.Subscriber("/mavros1/mavros/global_position/compass_hdg", Float64, callback1)
        rospy.Subscriber("/mavros2/mavros/global_position/compass_hdg", Float64, callback2)
        #rospy.Subscriber("/mavros3/mavros/global_position/compass_hdg", Float64, callback3)
        rospy.Subscriber("/mavros1/mavros/global_position/global", NavSatFix, callback4)
        rospy.Subscriber("/mavros2/mavros/global_position/global", NavSatFix, callback5)
        #rospy.Subscriber("/mavros3/mavros/global_position/global", NavSatFix, callback6)
        rospy.Subscriber("/compute", compute, callback7)
        
       
        counter = counter + 1

        pub.publish(hdg2)
        
        f.write(str(counter)+", ")
        f.write(str(hdg1) + ", ")
        f.write(str(alt1) + ", ")
        f.write(str(lat1) + ", ")
        f.write(str(lon1) + ", ")
        f.write(str(counter)+", ")
        f.write(str(hdg2) + ", ")
        f.write(str(alt2) + ", ")
        f.write(str(lat2) + ", ")
        f.write(str(lon2) + ", ")
        f.write(str(counter)+", ")
        f.write(str(d12) + ", ")
        f.write(str(b12) + ", ")
        f.write(str(alt12) + ", ")
        f.write(str(hdg12) + "\n")
        #time.sleep(2)
        #rate.sleep()
        time.sleep(1)
        #rospy.spin()

if __name__ == '__main__':
    main()
