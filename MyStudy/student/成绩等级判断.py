try:
    score = eval(input("请输入成绩:"))
    if score > 100 or score < 0:
        print("请输入0-100之间的分数")
    elif score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "E"
    print("输入成绩所属级别:{}".format(grade))
except:
    print("请输入整数!")
input("enter")
