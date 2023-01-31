s1 = {i for i in input().lower().split()}
s2 = {i for i in input().lower().split()}
print(*sorted(s1|s2))
print(*sorted(s1&s2))