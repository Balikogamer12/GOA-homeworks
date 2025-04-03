# რეგისტრაცია
email = input("შეიყვანეთ თქვენი ელექტრონული ფოსტა: ")
password = input("შეიყვანეთ პაროლი: ")

# ავტორიზაცია
if input("შეიყვანეთ თქვენი ელექტრონული ფოსტა ავტორიზაციისთვის: ") == email and input() == password:
    print("True")
else:
    print("False")
