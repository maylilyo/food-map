import except_list_of_place
import re
hangul = re.compile("[^ !?가-힣]+")

with open("/home/sehan/git/food-map/datas/samples/kakao_questions.txt", 'r') as file:
    lines = file.read().split('\n')
    lines = list(set(lines))

processed_lines = []
for line in lines:
    processed_lines.append(hangul.sub(" ", line))

processed_lines.sort(key=len)

with open("/home/sehan/git/food-map/datas/samples/kakao_questions_2.txt", 'w') as file:
    for i in range(len(processed_lines)):
        # file.write(processed_lines[i] + '\n')
        file.write("2018. 11. 29. 오후 1:14, 옹" + str(i) + " : " + processed_lines[i] + '\n')