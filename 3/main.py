r = 0
c = 0
ans = 1
coordinates = [(3,1)] #Part 1
coordinates = [(1,1),(3,1),(5,1),(7,1),(1,2)] #Part 2
G = []
f = open("pattern.txt", "r")
pattern = f.read()
rows = pattern.split("\n")

for row in rows:
    G.append(list(row.strip()))
    
for (dc,dr) in coordinates:
    r = 0
    c = 0
    trees = 0 
    while r+1 < len(G):
        c += dc
        r += dr
        if G[r][c%len(G[r])] == "#":
            trees += 1
    ans *= trees

print("> Day 3 - Toboggan Trajectory")
print(ans)

