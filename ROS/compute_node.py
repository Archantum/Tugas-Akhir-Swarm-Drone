#!/usr/bin/env python

from swarm.msg import control, coords, compute
from math import radians, cos, sin, asin, sqrt
import math


pub=rospy.Publisher('/compute',compute,queue_size=10)
def callback1(msg):
    hdg1=msg.hdg1 //heading
    hdg2=msg.hdg2
    hdg3=msg.hdg3
    alt1=msg.alt1 //altitutde Z
    alt2=msg.alt2
    alt3=msg.alt3
    lat1=radians(msg.lat1) //latitude X
    lat2=radians(msg.lat2)
    lat3=radians(msg.lat3)
    lon1=radians(msg.lon1) //longitude Y
    lon2=radians(msg.lon2)
    lon3=radians(msg.lon3)

    r = 6371
    a12 = sin(lat2-lat1 / 2)**2 + cos(lat1) * cos(lat2) * sin(lon2-lon1 / 2)**2 
    c12 = 2 * asin(sqrt(a))
    d12= c12*r //d = jarak atar drone

    a23 = sin(lat2-lat3 / 2)**2 + cos(lat3) * cos(lat2) * sin(lon2-lon3 / 2)**2 
    c23 = 2 * asin(sqrt(a))
    d23= c23*r

    X12 = cos(lat2)*sin(lon2-lon1)
    Y12 = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(lon2-lon1)
    B1 = math.atan2(X,Y)
    B12 = B1*180/math.pi //B = Sudut Bearing (menghadap)

    X23 = cos(lat3)*sin(lon3-lon2)
    Y23 = cos(lat2)*sin(lat3) - sin(lat2)*cos(lat3)*cos(lon3-lon2)
    B2 = math.atan2(X,Y)
    B23 = B2*180/math.pi

    alt12 = alt2-alt1
    alt23 = alt2-alt3
    hdg12 = hdg2-hdg1
    hdg23 = hdg2-hdg3
    dat=compute();
    dat.d12=d12
    dat.d23=d23
    dat.b12=b12
    dat.b23=b23
    dat.alt12=alt12
    dat.alt23=alt23
    dat.hdg12=hdg12
    dat.hdg23=hdg23
    dat.hdg2=hdg2
    pub.publish(dat)
        
    
def main():
    rospy.init_node('Compute_node')
    rospy.Subscriber("/coords", coords, callback1)

    rospy.spin()

if __name__ == '__main__':
    main()
