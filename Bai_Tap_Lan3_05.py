def check ():
    while True:
        number =  int(input("Mời nhập số từ 0 đến 9: "))
        if number.isdigit() and 0 >= number <= 9:
            print(f"Ban da nhap dung chu so: {number}")
            break
        else:
            print("Ban nhap sai!!!")
check()