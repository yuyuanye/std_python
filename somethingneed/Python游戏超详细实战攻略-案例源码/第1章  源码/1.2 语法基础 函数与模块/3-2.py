【例3-2】输入学生的成绩score，按分数输出其等级：score≥90为优，90>score≥80为良，80>score≥70为中等，70>score≥60为及格，score<60为不及格。
score=int(input("请输入成绩"))      #int()转换字符串为整型
if score >= 90: 
    print("优")
elif  score >= 80: 
    print("良") 
elif  score >= 70:
    print("中")
elif  score >= 60: 
    print("及格")
else :
    print("不及格")


