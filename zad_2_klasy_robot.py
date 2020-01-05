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