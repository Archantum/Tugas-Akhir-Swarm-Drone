#!/usr/bin/env python

from swarm.msg import control, compute, move1

pub=rospy.Publisher('/move1',move1,queue_size=10)

def callback1(msg):
    global move11,move12,move13,move14
    d12=msg.d12
    b12=msg.b12
    alt12=msg.alt12
    hdg12=msg.hdg12
    hdg2=msg.hdg2
    if d12>0.0015:
        move11 = 1 #kanan
    elif d12<0.0015:
        move11 = 0 #kiri
    elif d12=0.0015:
        move11 = 2 #hold

    if b12>90 :
        move12 = 0 #mundur
    elif b12<90: 
        move12 = 1 #maju
    elif b12=90 :
        move12 = 2 #hold

    if alt12<0 :
        move13 = 0 #turun
    elif alt12>0 : 
        move13 = 1 #naik
    elif alt12=0 :
        move13 = 2 #hold

    if hdg12<180 and hdg12>0:
        move14 = 0  #kiri
    elif hdg12>180 or hdg12<0:
        move14 = 1 #kanan
    elif hdg12=0 :
        move14 = 2 #hold

def callback2(msg):
    global move11,move12,move13,move14
    ch1=msg.ch1
    ch2=msg.ch2
    ch3=msg.ch3
    ch4=msg.ch4
    ch5=msg.ch5
    ch6=msg.ch6
    mode=msg.mode

    cmd=move();
    cmd.ch1 = ch1
    cmd.ch2 = ch2
    cmd.ch3 = ch3
    cmd.ch4 = ch4
    cmd.ch5 = ch5
    cmd.ch6 = ch6
    cmd.mode = mode
    cmd.move11 = move11
    cmd.move12 = move12
    cmd.move13 = move13
    cmd.move14 = move14
    pub.publish(cmd)

def main():
    rospy.init_node('Move1_cmd')
    rospy.Subscriber("/compute", compute, callback1)
    rospy.Subscriber("/FlightMode",control,callback2)

    rospy.spin()

if __name__ == '__main__':
    main()
