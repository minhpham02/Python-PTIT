def isValid(n):
    s1 = n.count('A')
    s2 = n.count('B')
    s3 = n.count('C')
    if s1 > s2 or s2 > s3 or s1 == 0 or s2 == 0 or s3 == 0:
        return False
    return True

def backTrack(i, s, n, list):
    if i > n:
        return
    if isValid(s):   list += [s]
    if i < n:
        backTrack(i+1, s +'A', n, list)
        backTrack(i+1, s +'B', n, list)
        backTrack(i+1, s +'C', n, list)

list = []
n = int(input())
backTrack(0,'',n,list)
list.sort(key= lambda ele: (len(ele)))
print(*list, sep='\n')