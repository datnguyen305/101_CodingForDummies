input = [1,1,4,4,2,4,2,1,3,4,2,3,3,2,3]
S = 15

def remove_consecutive_duplicates(input, S):
    curr = 0 
    prev = 0
    final = []
    for i in range(S):
        curr  = input[i]
        if curr == prev:
            continue
        else: 
            final.append(curr)
            prev = curr
    return final

test = remove_consecutive_duplicates(input, S)
print(test)