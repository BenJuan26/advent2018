from aoc import get_input

data = get_input(4)
lines = data.split("\n")

guards = {}
total_shifts = {}
current_guard = 0
sleep_time = 0

import re

for line in lines:
    m = re.search(r"\[(\d{4})-(\d\d)-(\d\d) (\d\d):(\d\d)\] (.*)", line)
    year, month, day, hour, minute, message = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), m.group(6)
    m = re.search(r"Guard #(\d+) begins shift", message)
    if m is not None:
        current_guard = int(m.group(1))
        if current_guard not in guards:
            guards[current_guard] = [0] * 60
        try:
            total_shifts[current_guard] += 1
        except KeyError:
            total_shifts[current_guard] = 1
        continue
    if message == "falls asleep":
        sleep_time = minute
        continue
    if message == "wakes up":
        i = sleep_time
        while i < minute:
            guards[current_guard][i] += 1
            i += 1
        continue
    print("Reached impossible message: {}".format(message))

current_guard = 0
current_minute = 0
current_percentage = 0.0
for guard, sleep in guards.items():
    percentages = [x / total_shifts[guard] for x in sleep]
    for i in range(60):
        if percentages[i] > current_percentage:
            current_percentage = percentages[i]
            current_minute = i
            current_guard = guard

print(current_guard * current_minute)