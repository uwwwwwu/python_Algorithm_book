n,m = input().split()


n = int(n)
m = int(m)
answer=[]

for i in range(n):
    m_list = list(map(int, input().split()))
    m_list.sort()
    answer.append(m_list[0])


print(max(answer))