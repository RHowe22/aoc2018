class multiple:
    two = False
    three = False

    def find_multiples(self, string):
        index = 0
        while index < (len(string)):
            if string.count(string[index]) == 2:
                self.two = True
            elif string.count(string[index]) == 3:
                self.three = True
            index += 1


fName = "C:\\Users\\rob\\source\\Atom\\AOC2018\\day2input.txt"
file = open(fName)
data = file.readlines()

twocount = 0
threecount = 0
temp = multiple()
for lines in data:
    temp.find_multiples(lines)
    if temp.two:
        twocount += 1
    if temp.three:
        threecount += 1
    temp.two = False
    temp.three = False
print("twos: " + str(twocount) + " threes: " + str(threecount))
i = 0
numdiff = 0
while numdiff != 1:
    j = i + 1
    while j < len(data) and numdiff != 1:
        numdiff = 0
        index = 0
        while index < len(data[j]):
            if(data[i][index] != data[j][index]):
                numdiff += 1
            index += 1
        j += 1
    i += 1
index = 0
string = ""
while index < len(data[i-1]):
    if(data[i-1][index] == data[j-1][index]):
        string = string.__add__(data[i-1][index])
    index += 1
print(data[i-1])
print(data[j-1])
print(string)
