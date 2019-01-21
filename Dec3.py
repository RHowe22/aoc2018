grid = [[0 for x in range(1000)] for y in range(1000)]
# crete a grid for all the spaces that could be occupied

fName = "C:\\Users\\rob\\source\\Atom\\AOC2018\\day3input.txt"
file = open(fName)
data = file.readlines()
# read in the data

conflict = 0  # variable to count all conflicting indexes
good = {}
for x in range(len(data)):
    good[x] = True
# create a list of all the ids and set true to say they have no conflicts

for lines in data: # read in all the lines of data and collect information
    id = int(lines[lines.find('#') + 1: lines.find('@')])  # get the id of the claim
    xoff = int(lines[lines.find('@') + 1: lines.find(',')]) # get x-axis offset
    x = int(lines[lines.find(':') + 1: lines.find('x')])   # get the width of the claim
    y = int(lines[lines.find('x') + 1:])    # get the height of the claim
    yoff = int(lines[lines.find(',') + 1: lines.find(':')]) # get the y-axis offset
    # gather the id of the claim its x and y offests and the height and width of the fabric

    # fill in the grid with the claims and if their is a conflict add it to the
    # conflict count and mark the ids of the conflicting claims as false
    for width in range(x):
        for height in range(y):
            if grid[xoff+width][yoff+height] == 0:
                grid[xoff+width][yoff+height] = id
            elif grid[xoff+width][yoff+height] != -1:
                good[id-1] = False
                if grid[xoff+width][yoff+height] in good:
                    good[(grid[xoff+width][yoff+height])-1] = False
                grid[xoff+width][yoff+height] = -1
                conflict += 1

print(conflict)
# print conflict count and the id of the claim with no conflict
for x in range(len(good)):
    if good[x]:
        print(x+1)
        break
