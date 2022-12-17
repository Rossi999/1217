def main():
    math=int(input())
    isPass(math)
    english=int(input())
    isPass(english)
    chinese=int(input())
    isPass(chinese)

    sum=math+english+chinese
    average=sum/3
    print("總平均:",average)
    isPass(average)

def isPass(score):
    if score>=60 and score<=100:
        print("恭喜")
        return True
    elif score<60:
        print("重修舊好")
        return False

main()

