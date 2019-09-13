day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

log = []

data.sort()

for line in data:
    words = line.split()
    date = int(words[0][1:].replace('-', ''))
    time = int(words[1][:-1].replace(':', ''))
    if words[2] == "falls":
        fromtime = time
    elif words[2] == "wakes":
        log.append({"date": date, "from": fromtime,
                    "to": time, "id": id_guard})
    else:
        id_guard = int(words[3][1:])

slept = {}

for line in log:
    if line["id"] in slept:
        slept[line["id"]] += line["to"] - line["from"]
    else:
        slept[line["id"]] = line["to"] - line["from"]

slept_max = 0
max_id = 0

for id_guard in slept:
    if slept[id_guard] > slept_max:
        slept_max = slept[id_guard]
        max_id = int(id_guard)

minutes = [0 for _ in range(60)]

for line in log:
    if line["id"] == max_id:
        for i in range(line["from"] % 100, line["to"] % 100):
            minutes[i] += 1

max_minute_count = 0
max_minute = 0

for i, minute in enumerate(minutes):
    if minute > max_minute_count:
        max_minute = i
        max_minute_count = minute


print(max_id * max_minute)

# part 2

slept = {}

for line in log:
    if line["id"] in slept:
        slept[line["id"]] += line["to"] - line["from"]
    else:
        slept[line["id"]] = line["to"] - line["from"]

max_minute_count = 0
max_minute = 0
max_id = 0

for current_id in slept:

    minutes = [0 for _ in range(60)]

    for line in log:
        if line["id"] == current_id:
            for i in range(line["from"] % 100, line["to"] % 100):
                minutes[i] += 1

    for i, minute in enumerate(minutes):
        if minute > max_minute_count:
            max_minute = i
            max_minute_count = minute
            max_id = current_id

print(max_id * max_minute)
