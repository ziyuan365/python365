my_string=input("请输入一句话：")
new_string=my_string.split()        #分割句子并以列表的形式输出
WordsList=[list(word) for word in new_string]       #分割单词以二维列表的形式输出
for i in WordsList:
    for j in range(len(i)):
        if j==0:
            i.append(i[j]+"AY")
            del(i[j])
output_string = ""
for word_list in WordsList:
    # output_string += "".join(word_list) + " "       #将列表组合成单词
    output_string=output_string+"".join(word_list) +" "

# 去除末尾多余的空格并输出
print(output_string.strip())