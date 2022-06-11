unsigned long int a,b,c;
int x[15],ch1[15],ch[7],i,chn1,chn2,chn3,chn4,chn5,chn6;
//specifing arrays and variables to store values 

void setup() {
Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), read_me, FALLING);
  // enabling interrupt at pin 2
}

void loop() {
read_rc();

chn1 = ch[1]+999;Serial.print(ch[1]);Serial.print("\t");
chn2 = ch[2]+999;Serial.print(ch[2]);Serial.print("\t");
chn3 = ch[3]+999;Serial.print(ch[3]);Serial.print("\t");
chn4 = ch[4]+999;Serial.print(ch[4]);Serial.print("\t");
chn5 = ch[5]+999;Serial.print(ch[5]);Serial.print("\t");
chn6 = ch[6]+999;Serial.print(ch[6]);Serial.print("\n");


delay(100);
}


void read_me()  {
 //this code reads value from RC reciever from PPM pin (Pin 2 or 3)
 //this code gives channel values from 0-1000 values 
 //    -: ABHILASH :-    //
a=micros(); //store time value a when pin value falling
c=a-b;      //calculating time inbetween two peaks
b=a;        // 
x[i]=c;     //storing 15 value in array
i=i+1;       if(i==15){for(int j=0;j<15;j++) {ch1[j]=x[j];}
             i=0;}}//copy store all values from temporary array another array after 15 reading  
void read_rc(){
int i,j,k=0;
  for(k=14;k>-1;k--){if(ch1[k]>5000){j=k;}}  //detecting separation space 10000us in that another array                     
  for(i=1;i<=6;i++){ch[i]=(ch1[i+j]-1000);}}     //assign 6 channel values after separation space
