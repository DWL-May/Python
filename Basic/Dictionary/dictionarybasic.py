empty_dict = {}
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star','circle',9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict alos has {!s} elements".format(len(another_dict)))

#dictionary 복사
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

#정렬하기
dict_copy = a_dict.copy()
#딕셔너리 내 키를 기준으로 오름차순으로 딕셔너리의 키-값 쌍을 정렬한다
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120 (order by keys): {}".format(ordered_dict1))

#값을 기준으로 정렬
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
#오름차순
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: item[1], reverse=False)

#내림차순
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: item[1], reverse=True)
