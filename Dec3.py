grid = [[0 for x in range(1000)] for y in range(1000)]

fName = "C:\\Users\\rob\\source\\Atom\\AOC2018\\day3input.txt"
file = open(fName)
data = file.readlines()
conflict = 0
good = {}
for x in range(len(data)):
    good[x] = True
for lines in data:
    id = int(lines[lines.find('#') + 1: lines.find('@')])
    xoff = int(lines[lines.find('@') + 1: lines.find(',')])
    yoff = int(lines[lines.find(',') + 1: lines.find(':')])
    x = int(lines[lines.find(':') + 1: lines.find('x')])
    y = int(lines[lines.find('x') + 1:])
    # gather the id of the claim its x and y offests and the height and width of the fabric
    for width in range(x):
        for height in range(y):
            if grid[xoff+width][yoff+height] == 0:
                grid[xoff+width][yoff+height] = id
            elif grid[xoff+width][yoff+height] != -1:
                print(id)
                good.pop(id)
                if grid[xoff+width][yoff+height] in good:
                    del good[grid[xoff+width][yoff+height]]
                grid[xoff+width][yoff+height] = -1
                conflict += 1

print(conflict)
print(good)
