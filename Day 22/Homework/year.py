year = int(input("შეიყვანე წელი: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("ეს წელი ნაკიანია")
else:
    print("ეს წელი არ არის ნაკიანი")
