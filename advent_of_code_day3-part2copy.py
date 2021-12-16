gammarayzerocount = 0
gammarayonecount = 0
gammarayzerocount2 = 0
gammarayonecount2 = 0
gammarayzerocount3 = 0
gammarayonecount3 = 0
gammarayzerocount4 = 0
gammarayonecount4 = 0
gammarayzerocount5 = 0
gammarayonecount5 = 0
gammarayzerocount6 = 0
gammarayonecount6 = 0
gammarayzerocount7 = 0
gammarayonecount7 = 0
gammarayzerocount8 = 0
gammarayonecount8 = 0
gammarayzerocount9 = 0
gammarayonecount9 = 0
gammarayzerocount10 = 0
gammarayonecount10 = 0
gammarayzerocount11 = 0
gammarayonecount11 = 0
gammarayzerocount12 = 0
gammarayonecount12 = 0



row = 6
with open("./data/input-day3.txt") as f:
    gammarays = []
    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        gammarays.append(line.strip())





new_gammaray = [gammaray for gammaray in gammarays if gammaray[0] == "1"]
for gammaray in new_gammaray:
    if gammaray[0] == "1":
        gammarayonecount += 1
    if gammaray[0] == "0":
        gammarayzerocount += 1

new_gammaray2 = [gammaray for gammaray in new_gammaray if gammaray[1] == "1"]
for gammaray in new_gammaray2:
    if gammaray[1] == "1":
        gammarayonecount2 += 1
    if gammaray[1] == "0":
        gammarayzerocount2 += 1

new_gammaray3 = [gammaray for gammaray in new_gammaray2 if gammaray[2] == "1"]
for gammaray in new_gammaray3:
    if gammaray[2] == "1":
        gammarayonecount3 += 1
    if gammaray[2] == "0":
        gammarayzerocount3 += 1

new_gammaray4 = [gammaray for gammaray in new_gammaray3 if gammaray[3] == "1"]
for gammaray in new_gammaray4:
    if gammaray[3] == "1":
        gammarayonecount4 += 1
    if gammaray[3] == "0":
        gammarayzerocount4 += 1

new_gammaray5 = [gammaray for gammaray in new_gammaray4 if gammaray[4] == "1"]
for gammaray in new_gammaray5:
    if gammaray[4] == "1":
        gammarayonecount5 += 1
    if gammaray[4] == "0":
        gammarayzerocount5 += 1

new_gammaray6 = [gammaray for gammaray in new_gammaray5 if gammaray[5] == "1"]
for gammaray in new_gammaray6:
    if gammaray[5] == "1":
        gammarayonecount6 += 1
    if gammaray[5] == "0":
        gammarayzerocount6 += 1

new_gammaray7 = [gammaray for gammaray in new_gammaray6 if gammaray[6] == "1"]
for gammaray in new_gammaray7:
    if gammaray[6] == "1":
        gammarayonecount7 += 1
    if gammaray[6] == "0":
        gammarayzerocount7 += 1

new_gammaray8 = [gammaray for gammaray in new_gammaray7 if gammaray[7] == "1"]
for gammaray in new_gammaray8:
    if gammaray[7] == "1":
        gammarayonecount8 += 1
    if gammaray[7] == "0":
        gammarayzerocount8 += 1

# new_gammaray9 = [gammaray for gammaray in new_gammaray8 if gammaray[8] == "0"]
# for gammaray in new_gammaray8:
#     if gammaray[7] == "1":
#         gammarayonecount8 += 1
#     if gammaray[7] == "0":
#         gammarayzerocount8 += 1

#new_gammaray9 = [gammaray for gammaray in new_gammaray8 if gammaray[8] != "0"]
#new_gammaray10 = [gammaray for gammaray in new_gammaray9 if gammaray[9] != "0"]
#new_gammaray11 = [gammaray for gammaray in new_gammaray10 if gammaray[10] != "0"]
#new_gammaray12 = [gammaray for gammaray in new_gammaray11 if gammaray[11] != "0"]

#
# for gammaray in new_gammaray:
#     if gammaray[row] == "1":
#         gammarayonecount += 1
#     if gammaray[row] == "0":
#         gammarayzerocount += 1

# for i in range(len(gammarays)):
#     if gammaray[i][0] == "0":
#         del gammaray[i]
#         print(gammarays)

print(new_gammaray)
print(new_gammaray2)
print(new_gammaray3)
print(new_gammaray4)
print(new_gammaray5)
print(new_gammaray6)
print(new_gammaray7)
print(new_gammaray8)


if gammarayonecount > gammarayzerocount:
    print("1")
if gammarayzerocount > gammarayonecount:
    print ("0")
if gammarayonecount2 > gammarayzerocount2:
    print("1")
if gammarayzerocount2 > gammarayonecount2:
    print ("0")
if gammarayonecount3 > gammarayzerocount3:
    print("1")
if gammarayzerocount3 > gammarayonecount3:
    print ("0")
if gammarayonecount4 > gammarayzerocount4:
    print("1")
if gammarayzerocount4 > gammarayonecount4:
    print ("0")
if gammarayonecount5 > gammarayzerocount5:
    print("1")
if gammarayzerocount5 > gammarayonecount5:
    print ("0")
if gammarayonecount6 > gammarayzerocount6:
    print("1")
if gammarayzerocount6 > gammarayonecount6:
    print ("0")
if gammarayonecount7 > gammarayzerocount7:
    print("1")
if gammarayzerocount7 > gammarayonecount7:
    print ("0")
if gammarayonecount8 > gammarayzerocount8:
    print("1")
if gammarayzerocount8 > gammarayonecount8:
    print ("0")


print(4082 * 1362)

# if gammaray[1] == "1"