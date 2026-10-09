import random

try:
    while True:

        counts = input("需要我给你几次机会？：")
        counts = int(counts)
        answer = random.randint(1,100)

        while counts > 0:
            temp = input("来猜一下我心中的数吧：")
            guess = int(temp)

            if guess == answer:
                print("猜到了呢~")
                print("游戏结束,主人好厉害~")
                break
            elif 101 > guess > answer:
                print("高估我了")
                counts = counts - 1
            elif 0 < guess < answer:
                print("小看我了")
                counts = counts - 1
            else:
                print("请输入1~100之间的数字")
                print("哼~这次就不给你算了")
            if counts > 0:
                print("你还有"+ str(counts) +"次机会")    

        if guess != answer:
            print("失败了呢，这点事都做不好，真是一个杂鱼~")
            print("答案是"+ str(answer) +"哦~")
            temp = input("想再来一次吗杂鱼先生？想来的话就打1，不想就打0:")
            guess = int(temp)

            if guess == 1:
                print("好吧杂鱼先生，那就再给你一次机会吧")
            elif guess == 0:
                print("哼哼，很没出息的跑走了呢，真是没用的杂鱼~")
                break
            else:
                print("输入1或0啊！白痴！")
                while True:
                    temp = input("想来就打1，不想就打0:")
                    guess = int(temp)
                    
                    if guess == 1:
                        print("哎~好吧笨笨先生，那就再给你一次机会吧")
                        break
                    elif guess == 0:
                        print("嗨呀~这是谁家的笨蛋跑掉了？")
                        raise StopIteration
                    else:
                        print("……")
        else:
            temp = input("你想再来一次吗？想来的话就打1，不想就打0:")
            guess = int(temp)

            if guess == 1:
                print("好耶!")
            elif guess == 0:
                print("好吧，那就再见了，期待下次见面！")
                break
            else:
                print("不对哦，是数入1或0哦，主人不要分心喽~")
                while True:
                    temp = input("主人想再来一次吗？想来的话就打1，不想就打0:")
                    guess = int(temp)

                    if guess == 1:
                        print("好的主人，这次可不要粗心了哦~")
                        break
                    elif guess == 0:
                        print("好吧，那就再见喽~期待与主人的下次见面！")
                        raise StopIteration
                    else:
                        print("请输入1或0，不要粗心~")
except StopIteration:
    pass
