str1 = "Python is a fun programming language"
words = str1.split()
res = ""

for word in words:
    if len(word) > len(res):
        res = word        
print (res)

