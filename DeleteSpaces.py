# DeleteSpaces.py
# dH 9/23/23

file = open("C:\\2023fall\\python\\dataFiles\\animalNames.txt", "r")
f = file.readlines()
print(f)

new_list = []
for line in f:
    line = line.strip()
    new_list.append(line)
print(new_list)
# Remove the empty lines
newer_list = []
for i in new_list:
    if (i != ''):
        newer_list.append(i)
print(newer_list)
# create four lists of names
hyena_names = []
lion_names = []
bear_names = []
tiger_names = []

element_num = 0
for i in newer_list:
    if i == "Hyena Names:":
        print("\n Hyena Names found!")
        # Move to the next element, where the Hyena names are.
        print(newer_list[element_num+1])
        # get the hyena names into hyena_names.
        hyena_names = newer_list[element_num+1].split(",")
        # print hyena_names
        print(hyena_names)
        # print the fourth name, should be Zig
        print(hyena_names[3])


