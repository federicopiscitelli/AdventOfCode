
print("> Day 4 - Passport Processing")
f = open("passports.txt", "r")
passports = f.read()
rows = passports.split("\n\n")
required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
optional_fields = ["cid"]
ro_fields = required_fields + optional_fields
required_fields.sort()
ro_fields.sort()

#Part 1
count_valid = 0
for passport in rows:
    field_list = []
    formatted_passport = passport.replace("\n"," ")
    for field in formatted_passport.split(" "):
        field_list.append(field.split(":")[0])
    field_list.sort()
    if (field_list == required_fields) or (field_list == ro_fields):
        count_valid += 1
print(count_valid)

#Part 2
count_valid = 0
eye_colors = ["amb","blu","brn","gry","grn","hzl","oth"]
hex_values = ["#","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
for passport in rows:
    field_list = []
    formatted_passport = passport.replace("\n"," ")
    for field in formatted_passport.split(" "):
        field_attr = field.split(":")[0]
        field_value = field.split(":")[1]
        if field_attr == "byr" and int(field_value)>=1920 and int(field_value)<=2002:
            field_list.append(field_attr)
        if field_attr == "iyr" and int(field_value)>=2010 and int(field_value)<=2020:
            field_list.append(field_attr)
        if field_attr == "eyr" and int(field_value)>=2020 and int(field_value)<=2030:
            field_list.append(field_attr)
        if field_attr == "hgt":
            if field_value.find("cm")>0:
                if int(field_value.replace("cm",""))>=150 and int(field_value.replace("cm",""))<=193:
                    field_list.append(field_attr)
            elif field_value.find("in")>0:
                if int(field_value.replace("in",""))>=59 and int(field_value.replace("in",""))<=76:
                    field_list.append(field_attr)
        if field_attr == "hcl" and field_value[0]=="#":
            valid = True
            for letter in field_value:
                if valid and (letter in hex_values):
                    valid = True
                else:
                    valid = False
            if valid:
                field_list.append(field_attr)
        if field_attr == "ecl" and field_value in eye_colors:
            field_list.append(field_attr)
        if field_attr == "pid" and len(field_value)==9:
            field_list.append(field_attr)
        if field_attr == "cid":
            field_list.append(field_attr)
    field_list.sort()
    print(field_list)
    if (field_list == required_fields) or (field_list == ro_fields):
        count_valid += 1    
print(count_valid)