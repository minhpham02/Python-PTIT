import re

print('yes' if re.match("^([A-Z]|_)*.PY$",input().upper()) else 'no')