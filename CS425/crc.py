import sys
filename = sys.argv[1]
# print(filename)
file = open(filename,'r')
raw_data = file.read()
# print(raw_data)
FLAG = '10101001'
ESC =  '10100101'
twenty = '00010100'
polynomial = '10000011'
j = 0
data = []
byte = []
for i in raw_data:
    if(i == '' or i == '\n'):
        continue
    if( j == 8):
        j = 1
        data.append(byte)
        byte = []
        byte.append(i)
    else:
        j = j + 1
        byte.append(i)

# print(data)
# print(len(data))

def is_equal(string1,string2):
    for i in range(len(string1)):
        if(string1[i] != string2[i]):
            return 0
    return 1

frame = []
frames = []
for i in range(len(data)):
    if(is_equal(data[i],FLAG)):
        j = i+1
        while(j < len(data) and not is_equal(data[j],FLAG)):
            frame.append(data[j])
            j = j + 1
        i = j+1
        # print(frame)
        if(len(frame)):
            frames.append(frame)
        frame = []
check_frames = []
frames_temp = []
for i in frames:
    for j in i:
        frames_temp = frames_temp + j
    check_frames.append(frames_temp)
    frames_temp = []

frames = check_frames

# print(frames)
print(len(frames))



# temp = raw_data.split(FLAG)
# frames = []
# # print(temp)


def xor(data_byte,salt):
    x = []
    for i in range(len(data_byte)):
        x.append(str(int(data_byte[i]) ^ int(salt[i])))
    return x


def convert_to_list(string):
    x = []
    for i in string:
        x.append(i)
    return x

def remove_zeroes(arr):
    for i in range(len(arr)):
        if(int(arr[i])):
            return arr[i:]
    return []
# print(remove_zeroes('0000100111'))
def is_divisable(divisor,dividend):
    if(len(divisor) == 0):
        return 1
    else:
        if(len(divisor) < len(dividend)):
            if(len(remove_zeroes(divisor)) != 0):
                return 0
            else:
                return 1
        # print(divisor)
        # print(dividend)
        for i in range(len(dividend)):
            # print((int(divisor[i]) ) ^ (int(dividend[i])))
            divisor[i] = ((int(divisor[i]) ) ^ (int(dividend[i])))
        # print(divisor)
        # print(dividend)
        divisor = remove_zeroes(divisor)
        # print(divisor)
        # print(dividend)
        return is_divisable(divisor,dividend)


def is_valid(divisor):
    # print(divisor)
    # print(divisor[:-1])
    divisor1 = divisor[:-1]
    # print(divisor)

    # print(divisor)
    if(is_divisable(divisor1,polynomial)):
        # print("answer = 1")
        return 1
    else:
        # print("answer  =  0")
        return 0

def characterise(data_byte):
    x = 0
    weight  = 1
    for i in range(8):
        # print(i)
        # print(data_byte)
        x = x + int(data_byte[7 - i])* weight
        weight = weight * 2
    return chr(x)

def decode(frame):
    if(len(frame) == 0):
        return ''
    if(characterise(frame[0:8]) != characterise(ESC)):
        print((characterise(frame[0:8])),end = '')
        # return str(characterise(frame[0:8]))+str(decode(frame[8:]))
        decode(frame[8:])
    else:
        print(characterise(xor(frame[8:16],twenty)),end = '')
        decode(frame[16:])
        # #we now have an escape character we may have an escape or a flag ahead
        # if(is_equal(xor(frame[8:16],twenty),ESC)):
        #     #we have another escape character ahead
        #     print((characterise(ESC)),end = '')
        #     # return str(characterise(ESC))+str(decode(frame[16:]))
        #     decode(frame[16:])
        # elif(is_equal(xor(frame[8:16],twenty),FLAG)):
        #     print((characterise(FLAG)),end = '')
        #     decode(frame[16:])
        #     # return str(characterise(FLAG))+str(decode(frame[16:]))

#
# for i in temp:
#     if(i != '' and i != '\n'):
#         frames.append(i)
#
# print(frames)
# frame_number = len(frames)
# # print(frame_number)
# frames_temp = []
# for i in frames:
#     frames_temp.append(convert_to_list(i[:-8]))
# frames = frames_temp
# todel = []
# valid_frame = []
# for j in range(len(frames)):
#     # print(frames[j].split(sep = None))
#     if(len(frames[j]) <8):
#         # print(j+1)
#         todel.append(j)
#         continue
#     valid_frame.append(frames[j])
#     # if(is_valid(frames[j])):
#         # print(j+1)
#         # print(is_valid(frames[j]))
#
# frames = valid_frame
todel = []
for i in range (len(frames)):
    if(is_valid(frames[i]) == 0):
        todel.append(i+1)
        # print(i+1)
# print(len(frames))
for i in range(len(todel)-1):
    print(todel[i],end = ',')
if(len(todel)):
    print(todel[-1])
else:
    print('\n',end = '')
data = ""
for i in range(len(frames)):
    # print(i)
    # print(decode(i))
    if((i+1) in todel):
        continue

    x = decode(frames[i][:-8])
    # data = data + str(x)
# print(data)
# print("Hi")
# y = str(decode(frames[-1]),"utf-8")
# print((characterise(xor(frames[-1][16:24],twenty))))
# print(frames[-2])


# arr1 = ['1','1','1','1','0','0','1']
# arr2 = ['1','0','1','1']
# print(is_divisable(arr1,arr2))
