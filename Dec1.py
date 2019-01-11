fName = "C:\\Users\\rob\\source\\Atom\\AOC2018\\day1input.txt"
file = open(fName)
data = file.readlines()

#            part 1
#  parse through the file  and sum all the frequency changes starting at 0
# to find the resulting frequency
val = 0
for line in data:
    val += int(line)
print("The resulting frequency is "+str(val))

# part 2
# continously loop through the frequency chagnes to find the first frequency
# result that occurs twice
freq = {}  # a dictionary of all the resulting values
index = 0
val = 0
while True:
    val += int(data[index])  # modify the resulting value
    if val in freq.keys():  # if the frequency is already in the dictionary
        # we can break because this is the first duplicate
        break
    else:
        freq[val] = 1  # otherwise add the key to the dictionary
    index += 1
    index = (index) % (len(data))  # increment index and modulo based on size
print(str(val))  # print the resulting duplicate frequency
