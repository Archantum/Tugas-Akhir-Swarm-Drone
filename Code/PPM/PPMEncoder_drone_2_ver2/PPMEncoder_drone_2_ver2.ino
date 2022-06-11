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
    ppmEncoder.setChannel(2, ch3);
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
    }
  if(mode == 3){
    
    ppmEncoder.setChannel(0, ch1);
    ppmEncoder.setChannel(1, ch2);
    ppmEncoder.setChannel(2, ch3);
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, ch5);
    ppmEncoder.setChannel(5, ch6);
  }
  delay(1);
}

ros::Subscriber<swarm::control> sub("FlightMode", &messageCb );

void setup() {
  ppmEncoder.begin(OUTPUT_PIN);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();

  delay(1);
}
