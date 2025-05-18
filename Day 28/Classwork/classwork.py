age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age < 18:
    if age < 14:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No discount")
