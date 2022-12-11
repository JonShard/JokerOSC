# JokerOSC
A python program that sends a one liner jokes read from file to your chat box in VRChat.

## Installation 
### Use latest release
Run JokerOSC without python by downloading the latest release.  
Make sure to download both `JokerOSC.exe` and `jokes.txt`. Store them in the same location.  
You can find the [latest release here](https://github.com/JonShard/JokerOSC/releases)

### Running the application with python
You need python installed to run the JokerOSC this way.  
It can be downloaded at [their offical website](https://www.python.org/downloads/).

JokerOSC uses [Python-osc](https://github.com/attwad/python-osc) by attwad to send the message.  
It can be downloaded using pip, run `pip install python-osc` in your windows command promt.

Download this repository as a zip file and extract it somewhere.

## Usage
Start the program by clicking the start.bat. A command promt will appear and will start logging that it's sending jokes.
```
C:\Users\Jone\Desktop\joker\/joker.py --timer-seconds 180 --input-file jokes.txt
Funny joke: Don’t you hate it when someone answers their own questions? I do.

Sent, wating 180 seconds
```

The time in between the jokes can be adjusted by changing the `--timer-seconds 180` flag in the start.bat file to a different number.
