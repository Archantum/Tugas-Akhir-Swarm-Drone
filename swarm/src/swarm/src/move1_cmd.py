#!/usr/bin/env python
import rospy
from swarm.msg import control, compute, move1, channels

pub=rospy.Publisher('/move1',move1,queue_size=10)

def callback1(msg):
    global move11,move12,move13,move14
    d12=msg.d12
    b12=msg.b12
    alt12=msg.alt12
    hdg12=msg.hdg12
    hdg2=msg.hdg2
    

    #roll
    if d12>0.0041:
        move11 = 1 #kanan
    elif d12<0.0024:
        move11 = 0 #kiri
    elif d12>0.0025 or d12<0.004: #harusnya 3 meter fix
        move11 = 2 #hold

    #pitch
    move12 = 2
    #if b12>96 :
    #    move12 = 0 #mundur
    #elif b12<84 :
    #    move12 = 1 #maju
    #elif b12>85 or b12<95 :
    #    move12 = 2 #hold

    #throttle
    if alt12 < -0.6 :
        move13 = 0 #turun
    elif alt12 > 0.6 : 
        move13 = 1 #naik
    elif alt12 > -0.5 or alt12 < 0.5 :
        move13 = 2 #hold

    #yaw - udah ok
    if hdg12 > 180 or hdg12 < -8:
        move14 = 0  #kiri
    elif hdg12 < 180 and hdg12 > 8:
        move14 = 1 #kanan
    elif hdg12 > -7 or hdg12 < 7 :
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

    cmd=move1()
    cmd.ch1 = ch1
    cmd.ch2 = ch2
    cmd.ch3 = ch3
    cmd.ch4 = ch4
    cmd.ch5 = ch5
    cmd.ch6 = ch6
    cmd.mode = mode
    cmd.move11 = move11 #roll
    cmd.move12 = move12 #pitch
    cmd.move13 = move13 #throttle
    cmd.move14 = move14 #yaw
    pub.publish(cmd)

    #all
    rospy.loginfo('\nch1:{}\nch2:{}\nch3:{}\nch4:{}\nch5:{}\nch6:{}\nmode:{}\nmove11:{}\nmove12:{}\nmove13:{}\nmove14:{}\n'.format(cmd.ch1,cmd.ch2,cmd.ch3,cmd.ch4,cmd.ch5,cmd.ch6,cmd.mode,cmd.move11,cmd.move12,cmd.move13,cmd.move14))
    
    #roll
    #rospy.loginfo('\nch1:{}\nch2:{}\nch3:{}\nch4:{}\nch5:{}\nch6:{}\nmode:{}\nmove11:{}\n'.format(cmd.ch1,cmd.ch2,cmd.ch3,cmd.ch4,cmd.ch5,cmd.ch6,cmd.mode,cmd.move11))
    
    #pitch
    #rospy.loginfo('\nch1:{}\nch2:{}\nch3:{}\nch4:{}\nch5:{}\nch6:{}\nmode:{}\nmove12:{}\n'.format(cmd.ch1,cmd.ch2,cmd.ch3,cmd.ch4,cmd.ch5,cmd.ch6,cmd.mode,cmd.move12))
    
    #throttle
    #rospy.loginfo('\nch1:{}\nch2:{}\nch3:{}\nch4:{}\nch5:{}\nch6:{}\nmode:{}\nmove13:{}\n'.format(cmd.ch1,cmd.ch2,cmd.ch3,cmd.ch4,cmd.ch5,cmd.ch6,cmd.mode,cmd.move13))
    
    #yaw
    #rospy.loginfo('\nch1:{}\nch2:{}\nch3:{}\nch4:{}\nch5:{}\nch6:{}\nmode:{}\nmove14:{}\n'.format(cmd.ch1,cmd.ch2,cmd.ch3,cmd.ch4,cmd.ch5,cmd.ch6,cmd.mode,cmd.move14))



def main():
    rospy.init_node('Move1_cmd')
    rospy.Subscriber("/compute", compute, callback1)
    rospy.Subscriber("/Sort",control,callback2)

    rospy.spin()

if __name__ == '__main__':
    main()
