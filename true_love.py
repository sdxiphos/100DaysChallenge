#last update for loop
names=[]
sum=0
count_true = {'t':0,'r':0,'u':0,'e':0,'l':0,'o':0,'v':0}


first_name = input('Please give your name: ')
second_name = input("Please give your true lover's name: ")


names.append(first_name)
names.append(second_name)

for name in names:
    for item in name.lower():
        for char in count_true:
            if char==item:
                i = count_true[char]+1
                count_true[char] = i
                # print(count_true[char])


for i in range(4):
    if i == 3:
        forth = str(count_true['e']) + str(count_true['e'])
        sum += int(forth)
    else:
        other = str(count_true[list(count_true.keys())[i]])+str(count_true[list(count_true.keys())[i+4]])
        sum += int(other)


print(f'Love: %{sum}')