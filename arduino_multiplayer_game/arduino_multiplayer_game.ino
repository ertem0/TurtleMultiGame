
int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
byte mapX = 0;
byte mapY = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP);
}

void loop()
{
  //Ler a posição do analogo
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);

  /*
  Serial.print(xPosition);
  Serial.print("||||");
  Serial.println(yPosition);
  */
  //detetar se o joystick esta a ser pressionado
  SW_state = digitalRead(SW);
  //map e uma função do arduino que permite associar valores (neste caso lidos no analogo) para um determinado intervalo de valores.
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
