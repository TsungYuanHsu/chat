# Chat 1 input to output

# read input
def read_input(filename):
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        input_list = [] 
        for line in f:
            input_list.append(line.strip())
    return input_list    

# convert to output form
def convert(input_list):
    convert_list = []
    for item in input_list:
        if item == 'Allen':
            person = 'Allen'
            continue
        elif item == 'Tom':
            person = 'Tom'
            continue
        convert_list.append(person + ': ' + item)
    return convert_list      

# write to output
def write_output(filename, convert_list):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for item in convert_list:
            f.write(item + '\n')

def main():
    input_list = read_input('input.txt')
    print(input_list)
    convert_list = convert(input_list)
    print(convert_list)
    write_output('output.txt', convert_list)

main()