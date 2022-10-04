# Chat 2 calculate specific information

# read input
def read_input(filename):
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        input_list = [] 
        for line in f:
            input_list.append(line.strip())
    return input_list    

# split time, name, and chat
def split(input_list):
    input_list_split = []
    for item in input_list:
        input_list_split.append(item.split(' ', 2))
    return input_list_split

# calculate how many words in total Allen and Viki typed
# Calculate how many 貼圖 and 圖片 in total Allen and Viki have sent
def calculate(input_list_split):
    wordcount_allen = 0
    wordcount_viki = 0
    emoji_allen = 0
    emoji_viki = 0
    pic_allen = 0
    pic_viki = 0
    for item in input_list_split:
        if item[1] == 'Allen':
            if item[2] != '貼圖' and item[2] != '圖片':  
                wordcount_allen += len(item[2])
            elif item[2] == '貼圖':
                emoji_allen += 1
            elif item[2] == '圖片':
                pic_allen += 1
        elif item[1] == 'Viki':
            if item[2] != '貼圖' and item[2] != '圖片':
                wordcount_viki += len(item[2])
            elif item[2] == '貼圖':
                emoji_viki += 1
            elif item[2] == '圖片':
                pic_viki += 1
    print('Allen typed', wordcount_allen, 'words in total', 'and sent 貼圖', emoji_allen, 'times and 圖片', pic_allen, 'times')
    print('Viki typed', wordcount_viki, 'words in total', 'and sent 貼圖', emoji_viki, 'times and 圖片', pic_viki, 'times' )

def main():
    input_list = read_input('LINE-Viki.txt')
    input_list_split = split(input_list)
    print(input_list_split)
    calculate(input_list_split)

main()