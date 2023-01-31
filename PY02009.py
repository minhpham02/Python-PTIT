
from typing import Counter


for t in range(int(input())):
    a = Counter(sorted(int(input()) for i in range(int(input()))))
    print(a.most_common(1)[0][0])