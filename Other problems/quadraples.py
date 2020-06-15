from itertools import combinations
li=list(map(int,input().split()))
output=[list(item) for item in combinations(li,4) if sum(item)==2]
output.sort() #used as the given output is in sorted.
print(output)
