import random

count = 0
dict = {}

with open('vocabulary.txt', 'r', encoding="UTF-8") as f:
    for line in f :
        line = line.strip()
        line_split = line.split(": ")
        dict[count] = {"en" : line_split[0], "kor" : line_split[1]}
        count += 1

anser = 'a'

while anser != 'q' :
    random_int = random.randint(0,count - 1)
    anser = input(f"{dict[random_int]['kor']}: ")
    if anser == 'q' :
        break
    elif anser == dict[random_int]['en'] :
        print('맞았습니다!\n')
    else :
        print(f'틀렸습니다. 정답은 {dict[random_int]["en"]}입니다.\n')