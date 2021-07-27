print("Enter marks of 5 subjects")

nep=int(input())
eng=int(input())
mat=int(input())
sci=int(input())
pop=int(input())


tot=(nep+eng+mat+sci+pop)
print("total",tot)
per=(nep+eng+mat+sci+pop)/5
print("Percentage",per)

if per>=75 and per<=100:
    print("Top")
elif per>=60 and per<=75:
    print("First div")
elif per>=45 and per<=60:
    print("Second div")
elif per>=35 and per<=45:
    print("Third div")
else:
    print("Fail")


