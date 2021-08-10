nep = float(input("Enter nepali marks"))
if nep > 100:
    print("Invalid")
    exit()
    eng = float(input("enter eng marks"))
if eng > 100:
    print("Invalid")
    exit()
math = float(input("enter math marks"))
if math > 100:
    print("Invalid")
    exit()

sci = float(input("enter sci marks"))
pop = float(input("enter pop marks"))

total = nep + eng + math + sci + pop
per= nep+eng+math
