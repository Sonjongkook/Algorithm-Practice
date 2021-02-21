import copy

def recursive(array, n):

  # base case
  if len(array)==n:
    #array를 변수로 공유하기때문에 null이 되므로 deepcopy 이용
    operator_list.append(copy.deepcopy(array))
    return
    
  # 총 경우수가 많지 않으므로 모든 경우수를 나열하는 리스트를 recursive로 구현
  array.append(" ")
  recursive(array, n)
  array.pop()

  array.append("+")
  recursive(array, n)
  array.pop()

  array.append("-")
  recursive(array, n)
  array.pop()
  
test_case = int(input())

for _ in range(test_case):
  operator_list = []
  n = int(input())

  recursive([], n-1)

  integer_list = [i for i in range(1, n+1)]

  for operator in operator_list:

    string = ""
    for i in range(n-1):
      string += str(integer_list[i]) + operator[i]
    # 마지막 숫자 경우수는 따로 포함
    string += str(integer_list[-1])

    if eval(string.replace(" ", "")) == 0:
      print(string)
  print()
