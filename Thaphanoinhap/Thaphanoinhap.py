def thaphanoi(n, coc1, coc2, coc3):
    if n == 1:
        print ("Chuyen tu", coc1, "sang", coc3)
    else:
        thaphanoi(n-1,coc1,coc3 ,coc2)
        print("Chuyen tu", coc1, "sang", coc3)
        thaphanoi(n-1,coc2,coc1, coc3)
def main():
    n = int(input("Nhập số đĩa cần chuyển "))
    print("trạng thái đầu: ")
    print(n,"đĩa ở cọc 1") 
    print("cọc 2 không có đĩa")
    print("cọc 3 không có đĩa")
    print()
    thaphanoi(n,"coc 1","coc 2","coc 3")
    print("chuyển xong \n")
if __name__ == "__main__":
    main()