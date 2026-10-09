import random

try:
    while True:

        counts = input("需要给您几次机会？：")
        counts = int(counts)
        answer = random.randint(1,100)

        while counts > 0:
            temp = input("来猜一下数吧：")
            guess = int(temp)

            if guess == answer:
                print("恭喜，回答正确。我方对您的判断力表示赞赏。")
                print("本局游戏圆满结束，恭喜您取得最终胜利。")
                break
            elif 101 > guess > answer:
                print("提示：您的估值偏高，建议适度下调预期。")
                counts = counts - 1
            elif 0 < guess < answer:
                print("提示：您的估值偏低，建议适度上调预期。")
                counts = counts - 1
            else:
                print("无效输入：请提供1至100之间的整数。")
                print("鉴于本次输入无效，特此免扣一次机会，请珍惜。")
            if counts > 0:
                print("您目前剩余" , str(counts) , "次机会，请合理安排。")

        if guess != answer:
            print("很遗憾，本次挑战未能成功。胜败乃兵家常事，请勿介怀。")
            print("现正式公布正确答案：" , str(answer) , "。")
            temp = input("想再来一次吗先生？想的话就打1，不想就打0:")
            guess = int(temp)

            if guess == 1:
                print("您的再挑战申请已获批准。新一轮即将开始。")
            elif guess == 0:
                print("已受理您的退出申请。感谢参与，期待下次合作。")
                break
            else:
                print("输入有误。请重新输入1或0，谢谢配合。")
                while True:
                    temp = input("想来就打1，不想就打0:")
                    guess = int(temp)
                    
                    if guess == 1:
                        print("您的再挑战申请已获批准。祝您本轮旗开得胜。")
                        break
                    elif guess == 0:
                        print("退出申请已受理。再见，感谢光临。")
                        raise StopIteration
                    else:
                        print("……（系统礼貌地保持了沉默）")
        else:
            temp = input("你想再来一次吗？想来的话就打1，不想就打0:")
            guess = int(temp)

            if guess == 1:
                print("申请已批准！新一轮挑战正式启动。")
            elif guess == 0:
                print("好的，本次服务到此结束。期待您下次光临。")
                break
            else:
                print("输入有误，请注意：请输入1或0。")
                while True:
                    temp = input("先生想再来一次吗？想来的话就打1，不想就打0:")
                    guess = int(temp)

                    if guess == 1:
                        print("申请已批准。新一轮开始，请集中注意力。")
                        break
                    elif guess == 0:
                        print("好的，本次服务结束。期待与您再次相见。")
                        raise StopIteration
                    else:
                        print("请输入1或0。请注意输入规范。")
except StopIteration:
    pass
