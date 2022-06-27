#!/usr/bin/env python

import rospy
from swarm.msg import control, coords, compute
from math import radians, cos, sin, asin, sqrt, atan2
import math


pub=rospy.Publisher('/itung',compute,queue_size=10)
def callback1(msg):
    hdg1=msg.hdg1
    hdg2=msg.hdg2

    alt1=msg.alt1
    alt2=msg.alt2

    lat1=radians(msg.lat1)
    lat2=radians(msg.lat2)

    lon1=radians(msg.lon1)
    lon2=radians(msg.lon2)


    r = 6371
    dlat1=lat2-lat1
    dlon1=lon2-lon1
    a12 = sin(dlat1 / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon1 / 2)**2 
    #>>>> DIUBAH >>> c12 = 2 * asin(sqrt(a12))
    c12 = 2 * atan2(sqrt(a12), sqrt(1 - a12))
    d12= c12*r
    #d12= 0.003


    X12 = cos(lat2)*sin(lon2-lon1)
    Y12 = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(lon2-lon1)
    B1 = atan2(X12,Y12)
    #>>>TRY THIS>>> B1 = atan2(Y12,X12)
    B12 = B1*180/math.pi
    #>>>TRY THIS>>> B1 = math.degrees(B1)
    #>>>TRY THIS>>> B12 = (B1 + 360) % 360
    #B12 = 90

    alt12 = (alt2)-alt1
    #alt23 = alt2-alt3
    hdg12 = (hdg2)-hdg1
    #hdg23 = hdg2-hdg3
    dat=compute();
    dat.d12=d12
    #dat.d23=d23
    dat.b12=B12
    #dat.b23=B23
    dat.alt12=alt12
    #dat.alt23=alt23
    dat.hdg12=hdg12
    #dat.hdg23=hdg23
    dat.hdg2=hdg2
    pub.publish(dat)

    #rospy.loginfo('\nd12:{}, d23:{}\nalt12:{}, alt23:{}\nhdg12:{}, hdg23:{}, hdg2:{}\n'.format(dat.d12,dat.d23,dat.b12,dat.b23,dat.alt12,dat.alt23,dat.hdg12,dat.hdg23,dat.hdg2))
    rospy.loginfo('\nd12:{}\nb12:{}\nalt12:{}\nhdg12:{}, hdg2:{}\n'.format(dat.d12,dat.b12,dat.alt12,dat.hdg12,dat.hdg2))

def main():
    rospy.init_node('Itung')
    rospy.Subscriber("/coords", coords, callback1)

    rospy.spin()

if __name__ == '__main__':
    main()
