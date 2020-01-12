from random import randint

opportunity = 4
answer = randint(1,20)

while opportunity > 0:
    enterValue = input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:" % opportunity)
    if answer == int(enterValue):
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % opportunity)
    elif answer != int(enterValue):
        if opportunity == 1:
            print("아쉽습니다. 정답은 %d였습니다." % answer)
        elif answer > int(enterValue):
            print("Up")
        elif answer < int(enterValue):
            print("Down")
    opportunity -= 1