def func(rules, allowed_colors, color_to_find):
    for rule in rules:
        rule_txt = rule.split("contain")
        if rule.find(color_to_find) > 0:
            allowed_colors.append(rule_txt[0].strip())
            func(rules, allowed_colors, rule_txt[0].replace("bags","").strip())
    return allowed_colors


def func2(rules,color_to_find,tot_bags):
    for rule in rules:
        rule_txt = rule.split("contain")
        container_bag = rule_txt[0]
        internal_bags = rule_txt[1].split(",")
        if container_bag.find(color_to_find) == 0:
            print(internal_bags)
            for bag in internal_bags:
                formatted_bag = bag.strip().replace(".","").replace("bags","").replace("bag","")
                print(formatted_bag)
                number_of_bags = formatted_bag.split(" ")[0]
                next_color = formatted_bag.replace(number_of_bags,"").strip()
                if next_color != "other":
                    tot_bags += +(func2(rules,next_color,tot_bags)*int(number_of_bags))+int(number_of_bags)
                    print("Total bags: "+str(tot_bags)+" - Number of bags: "+number_of_bags)
                else:
                    tot_bags += 0
    return tot_bags     
                


print("> Day 7 - Handy Haversacks")
f = open("rules.txt", "r")
file_rows = f.read()
rules = file_rows.split("\n")
#Part 1 
colors_available = func(rules, [], "shiny gold")
print(len(list(dict.fromkeys(colors_available))))

#Part 2 
total_number = func2(rules, "shiny gold",0)
print(total_number)
#print(len(list(dict.fromkeys(colors_available))))