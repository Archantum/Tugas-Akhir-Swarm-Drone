#!/usr/bin/env python

from swarm.msg import control, compute, move

pub=rospy.Publisher('/move3',move,queue_size=10)

def callback1(msg):
    global move31,move32,move33,move34
    d23=msg.d23
    b23=msg.b23
    alt23=msg.alt23
    hdg23=msg.hdg23
    hdg2=msg.hdg2
    if d23>0.0015:
        move31 = 0 #kiri
    elif d23<0.0015:
        move31 = 1 #kanan
    elif d23=0.0015 :
        move31 = 2 #hold

    if b23>90 :
        move32 = 1 #maju
    elif b23<90: 
        move32 = 0 #mundur
    elif b23 = 90 :
        move32 = 2 #hold

    if alt23<0 :
        move33 = 0 #turun
    elif alt23>0 :
        move33 = 1 #naik
    elif alt23 = 0 :
        move33 = 2 #hold

    if hdg23<180 and hdg23>0:
        move34 = 0  #kiri
    elif hdg23>180 or hdg23<0:
        move34 = 1 #kanan
    elif hdg23 = 0 :
        move34 = 2 #hold

def callback2(msg):
    global move31,move32,move33,move34
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
    cmd.move31 = move31
    cmd.move32 = move32
    cmd.move33 = move33
    cmd.move34 = move34
    pub.publish(cmd)

def main():
    rospy.init_node('Move3_cmd')
    rospy.Subscriber("/compute", compute, callback1)
    rospy.Subscriber("/FlightMode",control,callback2)

    rospy.spin()

if __name__ == '__main__':
    main()
