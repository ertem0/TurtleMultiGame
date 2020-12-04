int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup()
{
  Serial.begin(115200);

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
  SW_state = !digitalRead(SW);
  //map e uma função do arduino que permite associar valores (neste caso lidos no analogo) para um determinado intervalo de valores.
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, 512, -512);

  //assim conseguimos passar os valores do arduino para o python.
  Serial.println((String)mapX + "|" + (String)mapY + "|" + (String)SW_state);

  delay(100);
}
