mX, mY = map(int, input().split())
x, y, v = map(int, input().split())
v_list = [0,1,2,3] #-1은 왼쪽방향

map_list = []
for i in range(mY):
    m_list = list(map(int, input().split()))
    map_list.append(m_list[0])

# 방향 돌리기
# 돌리면 왼쪽으로 가기
