sum_even = 0
count_even = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
        count_even += 1

average = sum_even / count_even
print("საშუალო ლუწების:", average)
