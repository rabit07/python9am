print("===================")
print("======computer bazar=============")
print("===================")

print("product list")
print("1.dell(20000) 2.toshiba(30000) 3.mac(50000)")
option=int(input("enter any number"))
qt=0
dell=20000
toshiba=30000
mac=50000
total=0
if option==1:
    qt+=int(input("enter quantity "))
    total+=qt*dell

elif option==2:
    qt+=int(input("enter quantity"))
    total+=qt*toshiba
elif option==3:
    qt+=int(input("enter quantity"))
    total+=qt*mac
else:
    print("invalid option")
    exit()

print(total)
print("1.home(1000) 2.pickup(free)")
opt=int(input("enter any option:"))
if opt==1:
    opt=total+1000
    print("home")
else:
    print("free")
    exit()
delivery_price=0
if opt==1:
    delivery_price+=1000
    print("select packing option")
    print("1.palstic bag (rs 500) 2.bag(rs 1000) 3.gift box(5000) 4.none")
    pq=int(input("enter any option"))
    packaging_price=0

if opt==1:
    packaging_price+=500
    print("plastic")
elif opt==2:
    packaging_price+=1000
    print("bag")
elif opt==3:
    packaging_price+=5000
    print("gift box")
else:
 packaging_price=0

print("select any location")
print("1. ktm (13%) 2. ltp (free) 3.bkt (free)")
lq=int(input("enter any optoin"))

tax_amount=0
if lq==1:
    tax_amount+=total*0.13
gt= total+tax_amount+packaging_price+delivery_price

print(f"total:{total}")
print(f"total qunatity:{qt}")
print(f"tax amount:{tax_amount}")
print(f"gt:{gt}")


