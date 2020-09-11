import math
def InputData():
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    c = float(input("Nhập số c: "))
    return a,b,c
# --------------------------------
def SolveEqual(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Vô số nghiệm")
            else:
                print("Vô nghiệm")    
        else:
            print("Nghiệm x = ",-c/b)
    else:
        denta =b*b - 4*a*c
        if denta<0:
            print("Phương trình vô nghiệm")
        elif denta == 0:
            print("Phương trình có nghiêmh kép x1 = x2 = ",-b/2*a)
        else:
            x1 =(-b + math.sqrt(denta))/(2*a)          
            x2 =(-b - math.sqrt(denta))/(2*a)          
            print("Nghiệm x1 = ", x1)
            print(" & ")
            print("Nghiệm x2 = ", x2)

def main():
    a,b,c = InputData()
    SolveEqual(a,b,c)
if __name__ == "__main__":
    main()

