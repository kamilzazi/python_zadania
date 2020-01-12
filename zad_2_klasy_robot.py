"""2. Wyobraźmy sobie robota, który może poruszać się naprzód i obracać w lewo lub prawo.
Napisz klasę Robot, która będzie przechowywała informację o położeniu robota na płaszczyźnie oraz
kierumku w jakim jest zwrócony (N - północ, S - południe, E - wschód, W - zachód).
Klasa powinna udostępniać metodę wykonaj() przyjmującą jako argument ciąg instrukcji złożony z liter
N, P, L oznaczających odpowiednio: Naprzód, Prawo, Lewo.
Znaczenie instrukcji:
    - Naprzód - przemieszcza robota krok w kierunku, w którym obecnie jest zwrócony (przykładowo krok na wschód
        powoduje zmianę współrzędnych z (x, y) na (x + 1, y)
    - Prawo - obraca robota o 90 stopni w prawo
    - Lewo - obraca robota o 90 stopni w lewo
Wywołanie metody wykonaj() powinno przemieścić robota zgodnie z przekazanymi instrukcjami.
Przykład:
początkowe położenie robota: (0, 0), zwrot: N
ciąg instrukcji: NNPNLNPP
końcowe położenie robota: (1, 3), zwrot: S"""


class Robot:
    def __init__(self):
        self.zwrot = 'N'
        self.x = 0
        self.y = 0

    def __str__(self):
        return f'Polozenie robota: {self.x, self.y}. Zwrot robota: {self.zwrot}'

    def wykonaj(self, instrukcje):
        for litera in instrukcje:
            if litera in 'LP':
                if litera == 'P':
                    if self.zwrot == 'N':
                        self.zwrot = "E"
                    elif self.zwrot == 'E':
                        self.zwrot = "S"
                    elif self.zwrot == 'S':
                        self.zwrot = "W"
                    elif self.zwrot == 'W':
                        self.zwrot = "N"
                elif litera == 'L':
                    if self.zwrot == 'N':
                        self.zwrot = "W"
                    elif self.zwrot == 'W':
                        self.zwrot = "S"
                    elif self.zwrot == 'S':
                        self.zwrot = "E"
                    elif self.zwrot == 'E':
                        self.zwrot = "N"
            elif litera == 'N':
                if self.zwrot == "N":
                    self.y += 1
                if self.zwrot == "E":
                    self.x += 1
                if self.zwrot == "S":
                    self.y -= 1
                if self.zwrot == "W":
                    self.x -= 1
        # return f'Położenie robota: {self.x, self.y}. Zwrot robota: {self.zwrot}.'
        return self.x, self.y, self.zwrot

x = Robot()
print(x)
y = x.wykonaj("PNNLNPNN")
print(f'Położenie robota: {y[0], y[1]}. Zwrot robota: {y[2]}')
