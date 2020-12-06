print("> Day 5 - Binary Boarding")
f = open("boardings.txt", "r")
file_rows = f.read()
boardings = file_rows.split("\n")
seat_IDs = []
cols = [0,127]
rows = [0,7]
for boarding in boardings:
    cols_coordinates = boarding[:7]
    rows_coordinates = boarding[7:10]
    for value in cols_coordinates:
        if value == "F":
            cols[1] = int((cols[0]+cols[1])/2)
        else:
            cols[0] = round((cols[0]+cols[1])/2)
    col_seat = cols[0] if cols_coordinates[-1] == "F" else cols[1]
    for value in rows_coordinates:
        if value == "L":
            rows[1] = int((rows[0]+rows[1])/2)
        else:
            rows[0] = round((rows[0]+rows[1])/2)
    row_seat = rows[1] if rows_coordinates[-1] == "R" else rows[0]
    seat_ID = (col_seat*8) + row_seat
    #print("{boarding} - {seatid} - {col},{row}".format(boarding=boarding,seatid=seat_ID,col=col_seat,row=row_seat))
    seat_IDs.append(seat_ID)
    cols = [0,127]
    rows = [0,7]
seat_IDs.sort()
#Part 1
print(seat_IDs)

#Part 2
for i in range(55,907):
    if not(i in seat_IDs):
        print(i)