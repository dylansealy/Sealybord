# Sealybord

Sealybord is een Python spel gebaseerd op ganzenbord.

## Installatie

Sealybord is te spelen op elk GUI gebaseerde besturingssysteem die ondersteund wordt door Python. Sealybord vereist enkele pip modules.

### Windows en OS X

* Download en installeer Python voor [Windows](https://www.python.org/downloads/windows/) of [OS X](https://www.python.org/downloads/mac-osx/). **De Windows Store versie van Python werkt niet!**
* Download of clone de repository.
* Installeer de [benodigde pip](#pip-modules) modules.

### Linux

```bash
sudo apt install python3
sudo apt install pip
git clone https://github.com/DylanSealy/Sealybord.git
```

Download en installeer de [benodigde pip](#pip-modules) modules.

### Pip modules

Installeer de benodigde pip modules.

```bash
cd Sealybord/
pip install -r requirements.txt
```

## Gebruik

Het gebruik van dit spel spreekt over het algemeen voor zichzelf. Hieronder echter enkele aanwijzingen voor het gebruik van het programma.

* Druk op spatie om te gooien.
* Druk op escape om opnieuw te beginnen of om te stoppen.

## Spelregels

* Er wordt random gekozen wie er moet beginnen.
* Wanneer een speler vanaf start 4 & 5 gooit dan moet de speler naar het vakje 53.
* Wanneer een speler vanaf start 3 & 6 gooit dan moet de speler naar het vakje 26.
* Op een cookie vakje moet je het gegooide aantal ogen nog een keer naar voren. Als je teruggaat vanaf 63 dan moet je op een cookie vakje ook terug.
* Als een speler op het vakje 6 komt dan moet de speler naar het vakje 12.
* Als een speler op het vakje 19 komt dan moet de speler een beurt overslaan.
* Als een speler op het vakje 31 komt dan moet een andere speler je bevrijden. Is dit niet mogelijk dan moet je een beurt overslaan.
* Als een speler op het vakje 42 komt dan moet de speler naar het vakje 39.
* Als een speler op het vakje 58 komt dan moet een andere speler je bevrijden. Is dit niet mogelijk dan moet je een beurt overslaan.
* Je moet precies op het vakje 63 terechtkomen.

## Bekende problemen

Kijk bij de [issue](https://github.com/DylanSealy/Ganzenbord/issues) sectie voor alle bekende problemen. Hier kun je ook nieuwe problemen toevoegen.

## Licentie

Dit project is gelicentieerd onder de GNU GPLv3-licentie. Zie het [LICENSE](LICENSE) bestand voor meer details.
