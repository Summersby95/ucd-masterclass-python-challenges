s = "ababdba"

def NonRepeating(string):
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if (string[i] == string[j]) & (i != j):
                count += 1
        
        if count == 0:
            return i
    
    return -1

print(NonRepeating(s))