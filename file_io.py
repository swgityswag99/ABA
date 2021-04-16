

import json

# as requested in comment
tester = {"one": 1, "two": 2}

with open('file.txt', 'w') as file1:
     file1.write(json.dumps(tester)) # use `json.loads` to do the reverse

with open('file.txt', 'r') as file2:
    test1 = json.loads(file2.readline())
# test1 = json.loads('file.txt')
print(test1)
print(test1['one'])