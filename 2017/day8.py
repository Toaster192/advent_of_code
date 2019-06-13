import parse
import pdb


with open('day8-input') as f:
    input_data = f.read()

# pdb.set_trace()

data = input_data.split('\n')
data = [line for line in data if line.strip()]

registers = {}
totalMax = 0

for line in data:
    parsed_data = parse.parse(
            "{changing} {operation} {by:d} if "
            "{condRegister} {condOperation} {condValue:d}",
            line)
    value = registers.get(parsed_data['condRegister'], 0)
    operation = parsed_data['condOperation']
    if operation == "==":
        if value != parsed_data['condValue']:
            continue
    elif operation == "!=":
        if value == parsed_data['condValue']:
            continue
    elif operation == ">=":
        if value < parsed_data['condValue']:
            continue
    elif operation == "<=":
        if value > parsed_data['condValue']:
            continue
    elif operation == ">":
        if value <= parsed_data['condValue']:
            continue
    elif operation == "<":
        if value >= parsed_data['condValue']:
            continue
    else:
        print("Error 1")

    registers[parsed_data['changing']] = registers.get(
              parsed_data['changing'], 0)
    if parsed_data['operation'] == "inc":
        registers[parsed_data['changing']] += parsed_data['by']
    elif parsed_data['operation'] == "dec":
        registers[parsed_data['changing']] -= parsed_data['by']
    else:
        print("Error 2")

    if registers[parsed_data['changing']] > totalMax:
        totalMax = registers[parsed_data['changing']]


max = 0
for key, value in registers.items():
    if value > max:
        max = value

print(max)
print(totalMax)
