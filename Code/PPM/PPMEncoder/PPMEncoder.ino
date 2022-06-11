#include "PPMEncoder.h"
#include <ros.h>
#include <std_msgs/Int16.h>
#define OUTPUT_PIN 10
int ch4;
ros::NodeHandle nh;

void messageCb( const std_msgs::Int16& cont_msg){
  ch4 = cont_msg.data;
  ppmEncoder.setChannel(0, 1000);
  ppmEncoder.setChannel(1, 1000);
  ppmEncoder.setChannel(2, 1000);
  ppmEncoder.setChannel(3, ch4);
  ppmEncoder.setChannel(4, 1000);
  ppmEncoder.setChannel(5, 1000);
    delay(100);
}

ros::Subscriber<std_msgs::Int16> sub("ceks", &messageCb );

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
   // if(mode==0 || mode == 3) {
   
  
  nh.spinOnce();
    ppmEncoder.setChannel(0, 1000);
    ppmEncoder.setChannel(1, 1000);
    ppmEncoder.setChannel(2, 1000);
    ppmEncoder.setChannel(3, ch4);
    ppmEncoder.setChannel(4, 1000);
    ppmEncoder.setChannel(5, 1000);
  delay(100);
}
