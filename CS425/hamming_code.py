filename = "input.txt"
# print(filename)
file = open(filename,'r')
test_cases = file.readlines()
# print(test_cases)
# print(len(test_cases))
# raw_data = file.read()

def convert_to_list(string):
    x = []
    for i in string:
        if(i != '1' and i != '0'):
            continue
        x.append(int(i))
    return x

def characterise(data_byte):
    x = 0
    weight  = 1
    for i in range(8):
        # print(i)
        # print(data_byte)
        x = x + int(data_byte[7 - i])* weight
        weight = weight * 2
    # print(x)
    return chr(x)

def concat(nib1,nib2):
    # print("hihi")

    byte = []
    for i in nib1:
        byte.append(i)
    for i in nib2:
        byte.append(i)
    # print("hihi")
    c = characterise(byte)
    # print(c)
    return c

def is_nibble_correct(nib):
    # print(nib)
    p1 = nib[0]
    p2 = nib[1]
    d1 = nib[2]
    p3 = nib[3]
    d2 = nib[4]
    d3 = nib[5]
    d4 = nib[6]
    flag = 0
    if((p1+d1+d2+d4) % 2 != 0 ):
        flag = flag + 1
    if((p2+d1+d3+d4) % 2 != 0 ):
        flag = flag + 2
    if((p3+d3+d2+d4) % 2 != 0 ):
        flag = flag + 4
    return flag



def decode_nibble(nibble):
    flag = is_nibble_correct(nibble)
    word = []
    word.append(nibble[2])
    word.append(nibble[4])
    word.append(nibble[5])
    word.append(nibble[6])
    if(flag == 0):
        return word
    elif(flag == 1 or flag == 2 or flag == 4):
        return word
    elif(flag == 3):
        word[0] = 1 - word[0]
        return word
    elif(flag == 5):
        word[1] = 1 - word[1]
        return word
    elif(flag == 6):
        word[2] = 1 - word[2]
        return word
    else:
        word[3] = 1 - word[3]
        return word

numchar = 0

numerr = 0

def decode(data,num):
    # print(len(data))
    # print(data)
    if(len(data) == 0):
        return ''
    else:
        # print(concat(decode_nibble(data[:7]),decode_nibble(data[7:14])))
        if(is_nibble_correct(data[:7]) or is_nibble_correct(data[7:14])):
            num[0] = num[0] + 1
        num[1] = num[1] + 1
        # print(numchar,numerr)
        return concat(decode_nibble(data[:7]),decode_nibble(data[7:14]))+ decode(data[14:],num)

# while (True):
#     raw_data = file.readline()
test = []
for i in range(len(test_cases)):
    if(test_cases[i] == '\n'):
        continue
    else:
        test.append(test_cases[i])

test_cases = test

for itr in range(len(test_cases)-1):
    raw_data = test_cases[itr]
    if(raw_data == '\n'):
        continue
    # print(raw_data)
    num = [0,0]
    raw_data = convert_to_list(raw_data)
    # print(raw_data)
    # print(len(raw_data))

    if(len(raw_data) % 14 != 0):
        print("Invalid")
    else:
        print(decode(raw_data,num))

    percent = 0
    if(num[1] != 0):
        percent = num[0] / num[1]
    percent = int(percent * 100)
    print(percent,'%',sep = ' ')
    print('\n',end = '')

raw_data = test_cases[-1]
num = [0,0]
raw_data = convert_to_list(raw_data)
# print(raw_data)
# print(len(raw_data))

if(len(raw_data) % 14 != 0):
    print("Invalid")
else:
    print(decode(raw_data,num))

percent = 0
if(num[1] != 0):
    percent = num[0] / num[1]
percent = int(percent * 100)
print(percent,'%',sep = ' ',end = '')

# print("hihi")
