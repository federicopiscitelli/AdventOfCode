#Part 1
def is_valid(dict):
    istance_count = dict["psw"].count(dict["letter"])
    if istance_count>=int(dict["min"]) and istance_count<=int(dict["max"]):
        return True
    else:
        return False

#Part 2
def is_valid_second(dict):
    if bool(dict["psw"][int(dict["min"])-1] == dict["letter"]) ^ bool(dict["psw"][int(dict["max"])-1] == dict["letter"]): #xor
        return True
    else:
        return False



print("> Day 2 - Valid PSW")
f = open("psw.csv", "r")
entries = f.read()
entriesList = entries.split(";")
counter = 0
counter_second = 0
for string in entriesList:
    get_values = lambda string: {"min": string.split(' ')[0].split("-")[0], "max": string.split(' ')[0].split("-")[1],
                         "letter": string.split(' ')[1][:-1], "psw": string.split(' ')[2]}
    if is_valid(get_values(string)):
        counter += 1
    if is_valid_second(get_values(string)):
        counter_second += 1
print(counter)
print(counter_second)