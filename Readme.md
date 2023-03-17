# Steps
0. Sourcecode of the project: `projekt2023/TemperatureController/TemperatureController.py`

1. Status (Left button): `actualRoom`
    - `room1`(red), `room2`(white), `room3`(green)
    - We can change the status by pressing the button    
    - The correct led will light up    
    - The status will also show up on the screen

2. Temperature limit setter (Right button): `tempSet`    
    - Limit: 20...25 in 1 celsius steps    
    - The limit will also show up on the screen

3.  Temperature measurement    
    - Thermometer identification    
    - [Paralell Thermometer](https://www.hackster.io/vinayyn/multiple-ds18b20-temp-sensors-interfacing-with-raspberry-pi-d8a6b0)    
    - Temperature check
4. The temperature of the appropriate room should be displayed on the screen

5. The temperature should also be displayed on the screen

6. The stove should turn on/off according to the limit    
    - The blue led shows if the stove is heating or not