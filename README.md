# Sealybord
Sealybord is een Python spel gebaseerd op ganzenbord.

## Installatie
Sealybord hoeft niet geïnstalleerd te worden, maar is wel afhankelijk van enkele Python modules.
```bash
git clone https://github.com/DylanSealy/Ganzenbord.git 
pip install keyboard
pip install Pillow
pip install pygame
Voer ganzenbord.py uit
```

## Gebruik
Het gebruik van dit spel spreekt over het algemeen voor zichzelf. Hieronder echter enkele aanwijzingen voor het gebruik van het programma.
* Druk op enter om te gooien.
* Druk op escape om opnieuw te beginnen of om te stoppen.

## Spelregels
* Er wordt random gekozen wie er moet beginnen.
* Wanneer een speler vanaf start 4 & 5 gooit dan moet de speler naar het vakje 53.
* Wanneer een speler vanaf start 3 & 6 gooit dan moet de speler naar het vakje 26.
* Op een cookie vakje moet je het gegooide aantal ogen nog een keer naar voren. Als je terug gaat vanaf 63 dan moet je op een cookie vakje ook terug.
* Als een speler op het vakje 6 komt dan moet de speler naar het vakje 12.
* Als een speler op het vakje 19 komt dan moet de speler een beurt overslaan.
* Als een speler op het vakje 31 komt dan moet een andere speler je niet bevrijden. Is dit niet mogelijk dan moet je een beurt overslaan.
* Als een speler op het vakje 42 komt dan moet de speler naar het vakje 39.
* Als een speler op het vakje 58 komt dan moet een andere speler je niet bevrijden. Is dit niet mogelijk dan moet je een beurt overslaan.
* Je moet precies op het vakje 63 terechtkomen. 

** Licentie 
Dit project is gelicentieerd onder de MIT licentie. Zie het [LICENSE.md](LICENSE.md) bestand voor meer details. 