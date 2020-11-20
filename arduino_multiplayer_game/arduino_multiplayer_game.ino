int VRx = A0;
int VRy = A1;
int SW = 2;

byte xPosition = 0;
byte yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP);
}

void loop()
{
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);

  /*
  Serial.print(xPosition);
  Serial.print("||||");
  Serial.println(yPosition);
  */

  SW_state = digitalRead(SW);

  mapX = map(xPosition, 0, 1023, 0, 1023);
  mapY = map(yPosition, 0, 1023, 0, 1023);

  Serial.print("X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);

  delay(100);
}
