n = input()
my = [0,0]
list = ['a','b','c','d','e','f','g','h']
for i in range(len(list)):
    print(n[0])
    if str(n[0]) == list[i]:
        my[1]=i
        break

count = 0
my[0]= int(n[1])-1

#여기까지가 내 위치 바꿈 (org로 해도 괜찮을듯)

sum=[1,3,-1,3,1,-3,-1,-3,3,1,3,-1,-3,1,-3,-1]

my_list = my * 8

for j in range(0,len(sum),2):
    sum[j] = int(my_list[j]) + int(sum[j])
    sum[j+1] = int(my_list[j+1]) + int(sum[j+1])
    if int(sum[j]) < 0 or int(sum[j]) > 8 or int(sum[j+1]) < 0 or int(sum[j+1]) > 8 :
        count += 1

print(8-count)