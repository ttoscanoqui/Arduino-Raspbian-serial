void setup()
{
  Serial.begin(9600);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
}


void loop()
{
  if (Serial.available() > 0){
  char c = Serial.read();
    if (c == 'H') {
      digitalWrite(12,HIGH);
      digitalWrite(13,HIGH);
     }else if (c == 'L') {
      digitalWrite(12,LOW);
      digitalWrite(13,LOW);
     }
  }
}
