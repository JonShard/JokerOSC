import argparse
import random
import time

from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

parser = argparse.ArgumentParser(
    description="JokerOSC sends a on liner joke read from file every 60 seconds (by default) to your chat box in VRChat")
parser.add_argument("--timer-seconds", default="60", help="The number of seconds waited between each joke")
parser.add_argument("--input-file", default="jokes.txt", help="The file from which to read the jokes")
args = parser.parse_args()

with open(args.input_file, encoding="utf8") as jokes_file:
    jokes = jokes_file.readlines()

while True:
    joke = jokes[random.randrange(0, len(jokes))]
    print("Funny joke: " + joke)
    client.send_message("/chatbox/input", [joke, True])
    print("Sent, wating " + args.timer_seconds + " seconds")
    time.sleep(int(args.timer_seconds))