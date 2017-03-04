def solution(N):
    
    string = bin(N)[2:]
    
    max = 0
    count = 0
    
    for i in string:
        if i=='0':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    
    return max