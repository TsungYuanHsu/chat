# 3.txt split practice

# read 3.txt
def read_file(filename):
    input_list = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            input_list.append(line.strip())
        return input_list

# split time and date
def convert(input_list):
    new = []
    new2 = []
    for item in input_list:
    	new.append(item.split(' ', 1))
    for item in new:
    	time = item[0][:5]
    	name = item[0][5:]
    	new2.append(time + ' ' + name + ': ' + item[1])


        # if 'Allen' in item:
        #     new.append(item[0:5] + ' ' + item[5:10] + ':' + item[10:])
        # elif 'Viki' in item:
        #     new.append(item[0:5] + ' ' + item[5:9] + ':' + item[9:])
    return new2

# write into new txt
def write(filename, new2):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for msg in new2:
            f.write(msg + '\n')

def main():
    input_list = read_file('3.txt')
    print(input_list)
    new2 = convert(input_list)
    print(new2)
    write('3_output.txt', new2)

main()
