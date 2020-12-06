def list_from_string(string): 
    list1=[] 
    list1[:0]=string 
    return list1 


print("> Day 6 - Custom Customs")
f = open("responses.txt", "r")
file_rows = f.read()
responses = file_rows.split("\n\n")
num_responses = 0
for response in responses:
    list_response = list_from_string(response.replace("\n",""))
    list_no_duplicates = list(dict.fromkeys(list_response))
    num_responses += len(list_no_duplicates)
#Part 1
print(num_responses) 

matrix = []
for response in responses:
    rows = response.split("\n")
    local_list = []
    for row in rows:
        local_list.append(row)
    matrix.append(local_list)
print(matrix)
counter = 0
for list in matrix:
    if len(list) == 1:
        counter += len(list[0])
    else:
        print(list)
print(counter)
