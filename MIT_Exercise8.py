s = input("enter sting: ")
i = len(s)
count = 0
for x in range(i):
    if (s[x] == 'a' or s[x] == 'e' or s[x] == 'i' or s[x] == 'o' or s[x] == 'u'):
        count += 1
print(count)
