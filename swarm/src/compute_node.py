#!/usr/bin/env python

from time import time
import rospy
from swarm.msg import control, coords, compute
from math import radians, cos, sin, asin, sqrt
import math


pub=rospy.Publisher('/compute',compute,queue_size=10)
def callback1(msg):
    hdg1=msg.hdg1
    hdg2=msg.hdg2
    #hdg3=msg.hdg3
    alt1=msg.alt1
    alt2=msg.alt2
    #alt3=msg.alt3
    lat1=radians(msg.lat1)
    lat2=radians(msg.lat2)
    #lat3=radians(msg.lat3)
    lon1=radians(msg.lon1)
    lon2=radians(msg.lon2)
    #lon3=radians(msg.lon3)

    #ROLL
    r = 6371
    dlat1=lat2-lat1
    dlon1=lon2-lon1
    a12 = sin(dlat1 / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon1 / 2)**2 
    c12 = 2 * asin(sqrt(a12))
    d12= c12*r
    #d12= 0.003 #buat test

    #dlat2=lat2-lat3
    #dlon2=lon2-lon3
    #a23 = sin(dlat2 / 2)**2 + cos(lat3) * cos(lat2) * sin(dlon2 / 2)**2 
    #c23 = 2 * asin(sqrt(a23))
    #d23= c23*r

    #PITCH
    X12 = cos(lat2)*sin(lon2-lon1)
    Y12 = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(lon2-lon1)
    B1 = math.atan2(X12,Y12)
    B12 = B1*180/math.pi
    #B12 = 90 #buat test  

    #X23 = cos(lat3)*sin(lon3-lon2)
    #Y23 = cos(lat2)*sin(lat3) - sin(lat2)*cos(lat3)*cos(lon3-lon2)
    #B2 = math.atan2(X23,Y23)
    #B23 = B2*180/math.pi

    #THROTTLE
    alt12 = (alt2-2)-alt1 #tambahin kalo nilai alt beda di awal
    #alt12 = 0 #buat test

    #alt23 = alt2-alt3
    
    #YAW
    hdg12 = (hdg2)-hdg1
    #hdg12 = 0 #buat test

    #hdg23 = hdg2-hdg3
    dat=compute()
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
    rospy.init_node('Compute_node')
    rospy.Subscriber("/coords", coords, callback1)

    rospy.spin()

if __name__ == '__main__':
    main()
