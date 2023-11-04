tmp = []

with open("any_numbers.txt", "r") as filename:
    for i in filename.readlines():
        i = int(i.replace('\n', ''))
        tmp.append(i)

print(tmp)
