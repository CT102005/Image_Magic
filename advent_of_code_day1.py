# Advent of Code 2021 Day 1
num_inputs = 2001
increases = 0
decreases = 0
# To open the file
with open("./data/input-day1.txt") as f:
    depths = []
    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        depths.append(int(line))

class Input:
    """Represents the depth of the water of the ocean on a certain day"""

# print(depths)
for i in range(1, len(depths)):
    difference = int(depths[i-1]) - int(depths[i])
    if difference < 0:
        increases += 1
    if difference > 0:
        decreases -= 1


print(f"Increases: {increases}")
print(f"Decreases: {abs(decreases)}")