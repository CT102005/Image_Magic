gammarayzerocount = 0
gammarayonecount = 0

with open("./data/input-day3.txt") as f:
    gammarays = []
    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        gammarays.append(line.strip())

for row in range(len(gammarays[0])):
    gammarayzerocount = 0
    gammarayonecount = 0
    for gammaray in gammarays:
        if gammaray[row] == "1":
            gammarayonecount += 1
        if gammaray[row] == "0":
            gammarayzerocount += 1
    if gammarayonecount > gammarayzerocount:
        print("1")
    if gammarayzerocount > gammarayonecount:
        print ("0")

#print(gammaray[0])
#print(f"1 count: {gammarayonecount}")
#print(f"0 count: {gammarayzerocount}")

print(1174 * 2921)