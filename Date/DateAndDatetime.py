from datetime import date,time,datetime,timedelta


#오늘의 날자와 년,월,일 요소들을 출력하기

today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

#timedelta 함수를 이용하여 새로운 날짜 계산하기
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print(eight_hours)
print("Outputv#47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

#date 객체를 특정 형식의 문자열로 만들기 - strtime
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))