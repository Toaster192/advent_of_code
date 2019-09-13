day = str(__file__).find("day") + 3

with open("input" + str(__file__)[day:-3], "r") as f:
    data = f.readlines()

data = data[0].strip().split()
data = [int(x) for x in data]
backup = data.copy()


def foo(data, total):
    nodes = data[0]
    entries = data[1]
    data = data[2:]

    for _ in range(nodes):
        data, total = foo(data, total)

    for i in range(entries):
        total += data[0]
        data = data[1:]

    return data, total


_, result = foo(data, 0)
print(result)

# part 2:

data = backup


def bar(data, total):
    nodes = data[0]
    entries = data[1]
    data = data[2:]

    totals = []
    for _ in range(nodes):
        data, subtotal = bar(data, total)
        totals.append(subtotal)

    indexes = data[:entries]
    data = data[entries:]
    for index in indexes:
        if nodes:
            if index <= len(totals) and index:
                total += totals[index - 1]
        else:
            total += index

    return data, total


_, result = bar(data, 0)
print(result)
