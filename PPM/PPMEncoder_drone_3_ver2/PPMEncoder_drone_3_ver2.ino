#include "PPMEncoder.h"
#include <ros.h>
#include <swarm/move3.h>
#define OUTPUT_PIN 10
int mode, ch1, ch2, ch3, ch4, ch5, ch6, move31, move32, move33, move34;
ros::NodeHandle nh;

void messageCb( const swarm::move3& cont_msg){
  mode = cont_msg.mode;
  ch1 = cont_msg.ch1;
  ch2 = cont_msg.ch2;
  ch3 = cont_msg.ch3;
  ch4 = cont_msg.ch4;
  ch5 = cont_msg.ch5;
  ch6 = cont_msg.ch6;
  move31 = cont_msg.move31;
  move32 = cont_msg.move32;
  move33 = cont_msg.move33;
  move34 = cont_msg.move34;
    if(mode== 0) {
      //PITCH CH1
      if(move31=1){
        ppmEncoder.setChannel(0, 1639); //KANAN
      }
      else if (move31=0){
        ppmEncoder.setChannel(0, 1399); //KIRI
        }
      else if (move31=2){
        ppmEncoder.setChannel(0, 1503); //hold
        }
      //ROLL CH2
      if(move32=0){
        ppmEncoder.setChannel(1, 1399); //mundur
        }
      else if (move32=1){
        ppmEncoder.setChannel(1, 1639); //maju
      }
      else if (move32=2){
        ppmEncoder.setChannel(1, 1503); //hold
      }
      //THROTTLE CH3
      if(move33=0){
        ppmEncoder.setChannel(2, 1399); // turun
      }
      else if (move33=1){
        ppmEncoder.setChannel(2, 1639); //naik
      }
      else if (move33=2){
        ppmEncoder.setChannel(2, 1503); //hold
      }
      //YAW CH4
      if(move34=0){
        ppmEncoder.setChannel(3, 1639); //kiri
      }
      else if (move34=1){
        ppmEncoder.setChannel(3, 1399); //kanan
      }
      else if (move34=2){
        ppmEncoder.setChannel(3, 1503); //hold
      }      
    }
  if(mode == 4){
    
    ppmEncoder.setChannel(0, ch1);
    ppmEncoder.setChannel(1, ch2);
    ppmEncoder.setChannel(2, ch3);
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
  }
  delay(1);
}

ros::Subscriber<swarm::move3> sub("move3", &messageCb );

void setup() {
  ppmEncoder.begin(OUTPUT_PIN);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
