from datetime import datetime
import re

input = set(open("input.txt").readlines())

events = []

for i in input:
    r = re.search(r"\[(.*)\] (.*)", i)
    events.append({"time": datetime.strptime(
        r.group(1), "%Y-%m-%d %H:%M"), "event": r.group(2)})
events.sort(key=lambda event: event["time"])

currentguard = ""
guards = []

sleepstart = ""

for e in events:
    if e["event"].startswith("Guard"):
        currentguard = re.search(r"\d{1,}", e["event"]).group(1)
        guards.add(currentguard)
    elif e["event"].startswith("falls"):
