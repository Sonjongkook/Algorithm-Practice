def solution(phone_book):
    phone_book.sort()
    #string 정렬을 해놓은 상태라 바로 뒤 숫자가 해당이 안된다면 그 뒤 숫자들은 불가능
    for i in range(len(phone_book)-1):
      num = phone_book[i]
      if num == phone_book[i+1][:len(num)]:
          return False

    return True
