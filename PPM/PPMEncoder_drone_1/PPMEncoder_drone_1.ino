#include "PPMEncoder.h"
#include <ros.h>
#include <swarm/control.h>
#define OUTPUT_PIN 10
int mode, ch1, ch2, ch3, ch4, ch5, ch6;
ros::NodeHandle nh;

void messageCb( const swarm::control& cont_msg){
  mode = cont_msg.mode;
  ch1 = cont_msg.ch1;
  ch2 = cont_msg.ch2;
  ch3 = cont_msg.ch3;
  ch4 = cont_msg.ch4;
  ch5 = cont_msg.ch5;
  ch6 = cont_msg.ch6;
    if(mode== 0) {
    ppmEncoder.setChannel(0, ch1);
    ppmEncoder.setChannel(1, ch2);
    
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
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

ros::Subscriber<swarm::control> sub("Sort", &messageCb );

void setup() {
  ppmEncoder.begin(OUTPUT_PIN);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {

  // Min value
  //ppmEncoder.setChannel(3, 1000);
  //ppmEncoder.setChannel(3, PPMEncoder::MIN);
  //ppmEncoder.setChannelPercent(2, 0);
  //delay (3000);
  //ppmEncoder.setChannel(2, 2000);
  //delay (3000);
  // Max value
  //ppmEncoder.setChannel(3, 2000);
  //ppmEncoder.setChannel(3, PPMEncoder::MAX);
  //ppmEncoder.setChannelPercent(2, 100);
  //delay(3000);
  nh.spinOnce();
  if(mode== 0) {
    ppmEncoder.setChannel(0, ch1);
    ppmEncoder.setChannel(1, ch2);
    
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
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
