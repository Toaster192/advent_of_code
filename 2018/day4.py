day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

log = []

data.sort()

for line in data:
    words = line.split()
    date = int(words[0][1:].replace('-', ''))
    time = int(words[1][:1].replace(':', ''))
    if words[2] == "falls":
        fromtime = time
    elif words[2] == "wakes":
        log.append({"date": date, "time": time, "from": fromtime,
                    "to": time, "id": id})
    else:
        id = int(words[3][1:])
