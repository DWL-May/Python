from random import randint

numbers = []

while len(numbers) < 3:
    newNumber = randint(0, 9)

    while newNumber in numbers:
        newNumber = randint(0, 9)
    numbers.append(newNumber)

print(numbers)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
is3S = False
count = 1
while not is3S:
    strike = 0
    ball = 0
    inputAnswer = []
    print("세 수를 하나씩 차례대로 입력하세요.")

    while len(inputAnswer) < 3:
        temp = input("%d번째 수를 입력하세요: " % (len(inputAnswer) + 1))
        inputAnswer.append(int(temp))

    i = 0
    while len(inputAnswer) > i:
        if inputAnswer[i] == numbers[i]:
            strike += 1
        elif inputAnswer[i] in numbers:
            ball += 1
        i += 1

    if strike == 3:
        Is3S = True
        print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)
    else:
        print("%dS %dB" % (strike, ball))
        count += 1
