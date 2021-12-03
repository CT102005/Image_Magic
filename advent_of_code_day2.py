# Advent of Code 2021 Day 2
horizontal_position = 0
vertical_position = 0

with open("./data/input-day2.txt") as f:
    commands = []
    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        commands.append(line.strip().split(" "))


# def convert(list):
#     return ([i for item in list for i in item.split()])
#
#
# list = [f"{commands}"]
# list = ['"forward 5"]

for command in commands:
    direction = command[0]
    magnitude = int(command[1])
    if command[0] == "forward":
        horizontal_position += int(command[1])
    if command[0] == "down":
        vertical_position[0] -= int(command[1])
    if command[0] == "up":
        vertical_position += int(command[1])
    #print(f"[{direction}, {magnitude}]")
    # print(magnitude)



