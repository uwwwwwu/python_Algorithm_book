n = input()
n_list = input().split()

idx = [1,1]
result = [1,1]

for i in n_list :
    if 'R' == i : 
        idx[1] += 1
    elif 'L' == i : 
        idx[1] -= 1
    elif 'U' == i : 
        idx[0] -= 1
    elif 'D' == i : 
        idx[0] += 1
        
    if 1 <= int(idx[0]) and int(idx[0]) <= int(n) and  1 <= int(idx[1]) and int(idx[1]) <= int(n)  :
        result[0] = idx[0]
        result[1] = idx[1]

    else :
        idx[0] = result[0]
        idx[1] = result[1]
           
print(result)
    



