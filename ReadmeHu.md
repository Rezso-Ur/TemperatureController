# Feladat lépései
0. projekt forráskódja: `projekt2023/TemperatureController/TemperatureController.py`
1. állapotok (bal kapcsoló): `actualRoom`
    - `room1`(red), `room2`(white), `room3`(green)
    - A kapcsoló nyomogatásával váltunk az állapotok között
    - A megfelelő színű led gyúlad ki
    - Az állapot a képernyőre is kiíródik
2. hőmérséklet határállító(jobb kapcsoló): `tempSet`
    - határ: 20...25 1fok lépésekben
    - A határ a képernyőre is kiíródik

3. Hőmérséklet mérés
    - Hőmérők azonosítása  
    - [párhuzamos hőmérők](https://www.hackster.io/vinayyn/multiple-ds18b20-temp-sensors-interfacing-with-raspberry-pi-d8a6b0)  
    - hőmérséklet kiolvasása

4. A képernyőre a megfelelő szoba hőmérséklete kerüljön ki

5. A kijelzőre is kikerüljön a hőmérséklet

6. A határnak megfelelően ki/be kapcsoljon a kályha
    - kék led jelzi hogy a kályha fűt vagy sem