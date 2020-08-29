void setup() {
  Serial.begin(9600); // set the baud rate
}
char incoming;
void loop() {
  if(Serial.available() > 0){ // only send data back if data has been sent
    incoming = Serial.read(); // read the incoming data
    Serial.println(incoming); // send the data back in a new line so that it is not all one long line
  }

}
