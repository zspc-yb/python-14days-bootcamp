history = []

while True:
    print("1.加法 2.减法 3.乘法 4.除法 5.查看历史记录 6.退出")
    choice = int(input("请选择你的操作："))
    if choice == 6:
        break

    elif choice == 5:
        if history == []:
            print("没有历史记录。")
            continue
        else:
            print("历史记录：")
            for record in history:
                print(record)

    elif choice in [1,2,3,4]:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        if choice == 1:
            result = num1 + num2
            print("结果：", result)

        elif choice == 2:
            result = num1 - num2
            print("结果：", result)

        elif choice == 3:
            result = num1 * num2
            print("结果：", result)

        elif choice == 4:
            if num2 == 0:
                print("除数不能为零，请重新选择操作。")
                continue
            result = num1 / num2
            print("结果：", result)

        history.append(f"{num1} {'+' if choice == 1 else '-' if choice == 2 else '*' if choice == 3 else '/'} {num2} = {result}")

        print("是否继续操作？(y/n)")
        answer = input()
        if answer == 'n':
            break
        else:
            continue

