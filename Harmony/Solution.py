music_list = list(map(int, input().split())) # 입력값 리스트에 넣기

ans =0
for num in range(len(music_list)-1):
    if music_list[num] > music_list[num+1]:
        ans += 1
    else:
        ans -= 1
        
if ans == len(music_list)-1:
    print("descending")
elif ans == -(len(music_list)-1):
    print("ascending")
else:
    print("mixed")
