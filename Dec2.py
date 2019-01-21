# class to check  if a string contains the same pair or triple of a letter
class multiple:
    two = False # reflects if the class contains a duplicate of a char
    three = False # reflects in the class contains 3 of the same chars

    # method that checks if a given string contains and duplicates or triples
    def find_multiples(self, string):
        index = 0
        while index < (len(string)):
            if string.count(string[index]) == 2:
                self.two = True
            elif string.count(string[index]) == 3:
                self.three = True
            index += 1

    def reset(self):
        self.two = False
        self.three = False

fName = "C:\\Users\\rob\\source\\Atom\\AOC2018\\day2input.txt"
file = open(fName)
data = file.readlines()
# collect data from the text file
twocount = 0 # count the total number of duplicates and triples
threecount = 0
temp = multiple()
# creates a multiple object to check all the strings in the data file

for lines in data:  #use the multiple object to counnt all the duplicates and triples
    temp.find_multiples(lines)
    if temp.two:
        twocount += 1
    if temp.three:
        threecount += 1
    temp.reset()
print("twos: " + str(twocount) + " threes: " + str(threecount))

# compare all the string to find the pair that only differ by one char
i = 0
numdiff = 0
while numdiff != 1:  # all strings are checked until the strings at index i and j differ by only one char
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

#  produce the a string that is all the shared chars between the two strings from the last section
index = 0
string = ""
while index < len(data[i-1]):
    if(data[i-1][index] == data[j-1][index]):
        string = string.__add__(data[i-1][index])
    index += 1

# print the resulting string
print(string)
