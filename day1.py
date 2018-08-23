with open('day1-input') as f:
    input_data = f.read()

sum = 0
last = 0

for number in input_data:
    if number == last:
        sum += int(number)
    last = number

if last == input_data[0]:
    sum += int(last)

print(sum)

# Part two:

sum = 0
steps = len(input_data)//2

for i, number in enumerate(input_data):
    if number == input_data[(i + steps) % len(input_data)]:
        sum += int(number)

print(sum)
