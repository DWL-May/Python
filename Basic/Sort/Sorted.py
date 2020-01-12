my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
'''
이 예제는 sorted함수를 key함수와 결합하여 각 리스트에 있는 특정 인덱스에 있는 값에 다라 리스트를 정렬하는 방법을 보여준다.
key함수는 리스트를 정렬하기 위해 사용될 기준, 즉 키 key를 저장한다.이 예제에서 키는 람다 함수로써 
'인덱스 3에 위치한 값(즉 4번째 값)에 따라 정렬한다'를 의미한다.'

'''