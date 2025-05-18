positive_numbers = 0
negative_numbers = 0

for i in range(5):
    num = int(input("Please enter a number: "))

    if num > 0:
        positive_numbers = positive_numbers + 1
    elif num < 0:
        negative_numbers = negative_numbers + 1

print("Positive numbers count: " + str(positive_numbers))
print("Negative numbers count: " + str(negative_numbers))