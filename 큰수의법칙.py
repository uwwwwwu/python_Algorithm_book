n,m,k = input().split()
n_list = list(map(int, input().split()))

n = int(n)
m = int(m)
k = int(k)

n_list.sort(reverse=True)
answer=0
k_n = 0

for i in range(m):
    if k_n == k:
         answer += n_list[1] 
         k_n=0
    else:
        answer += n_list[0]
        k_n += 1

    

print(answer)