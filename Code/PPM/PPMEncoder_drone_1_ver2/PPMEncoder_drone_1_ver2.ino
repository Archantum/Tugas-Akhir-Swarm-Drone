#include "PPMEncoder.h"
#include <ros.h>
#include <swarm/move1.h>
#define OUTPUT_PIN 10
int mode, ch1, ch2, ch3, ch4, ch5, ch6, move11, move12, move13, move14;
ros::NodeHandle nh;

void messageCb( const swarm::move1& cont_msg){
  mode = cont_msg.mode;
  ch1 = cont_msg.ch1;
  ch2 = cont_msg.ch2;
  ch3 = cont_msg.ch3;
  ch4 = cont_msg.ch4;
  ch5 = cont_msg.ch5;
  ch6 = cont_msg.ch6;
  move11 = cont_msg.move11;
  move12 = cont_msg.move12;
  move13 = cont_msg.move13;
  move14 = cont_msg.move14;
    if(mode== 0) {
      //PITCH CH1
      if(move11=0){
        ppmEncoder.setChannel(0, 1399); //kiri
      }
      else if (move11=1){
        ppmEncoder.setChannel(0, 1639); //kanan
        }
      else if (move11=2){
        ppmEncoder.setChannel(0, 1503); //hold
        }
      //ROLL CH2
      if(move12=0){
        ppmEncoder.setChannel(1, 1399); //mundur
        }
      else if (move12=1){
        ppmEncoder.setChannel(1, 1639); //maju
      }
      else if (move12=2){
        ppmEncoder.setChannel(1, 1503); //hold
      }
      //THROTTLE CH3
      if(move13=0){
        ppmEncoder.setChannel(2, 1399);//turun
      }
      else if (move13=1){
        ppmEncoder.setChannel(2, 1639); //naik
      }
      else if (move13=2){
        ppmEncoder.setChannel(2, 1503); //hold
      }
      //YAW CH4
      if(move14=0){
        ppmEncoder.setChannel(3, 1639); //kiri
      }
      else if (move14=1){
        ppmEncoder.setChannel(3, 1399); //kanan
      }
      else if (move14=2){
        ppmEncoder.setChannel(3, 1503); //hold
      }
    }
  if(mode == 2){
    
    ppmEncoder.setChannel(0, ch1);
    ppmEncoder.setChannel(1, ch2);
    ppmEncoder.setChannel(2, ch3);
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
  }
  delay(1);
}

ros::Subscriber<swarm::move1> sub("move1_cmd", &messageCb );

void setup() {
  ppmEncoder.begin(OUTPUT_PIN);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {

  nh.spinOnce();
  delay(1);
}
