num = [4, 2, 3, 1, 5]
target = 9

def TargetCheck(num, target):
    answer = []
    for i in range(len(num)):
        for j in range(len(num)):
            if (num[i] + num[j] == target) & (i != j):
                answer = [i, j]
    return answer

print(TargetCheck(num, target))
