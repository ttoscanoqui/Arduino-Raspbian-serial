void setup() {
  Serial.begin(9600);
  pinMode(11,OUTPUT);
}

void loop() {

int so = analogRead(0)/4;
  Serial.print(String(analogRead(A0)));
  Serial.print(",");      //its nedeed to separate variables from a comma, because raspberry need to read like 150,25
  Serial.println(String(so));
  delay(500);
}
