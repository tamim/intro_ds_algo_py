n = input()
n = int(n)

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
print("n =", n, "count =", count)
