# JokerOSC
A python program that sends a one liner jokes read from file to your chat box in VRChat.

## Installation 
You need python to run the program.  
It can be downloaded at [their offical website](https://www.python.org/downloads/).

JokerOSC uses [Python-osc](https://github.com/attwad/python-osc) by attwad to send the message.  
It can be downloaded using pip, run `pip install python-osc` in your windows command promt.

Download this repositry as a zip file and extract it somewhere.

## Usage
Start the program by clicking the start.bat. A command promt will appear and will start logging that it's sending jokes.
```
C:\Users\Jone\Desktop\joker>python C:\Users\Jone\Desktop\joker\/joker.py --timer-seconds 180 --input-file jokes.txt
Funny joke: Don’t you hate it when someone answers their own questions? I do.

Sent, wating 180 seconds
```

The time in between the jokes can be adjusted by changing the `--timer-seconds 180` flag in the start.bat file to a different number.