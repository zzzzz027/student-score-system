def show_student():
    name = input("请输入学生姓名：")
    score = float(input("请输入学生成绩："))
    sid = input("请输入学生学号：")

    print(f"学生姓名：{name}")
    print(f"学生成绩：{score}")
    print(f"学生学号：{sid}")


if __name__ == "__main__":
    show_student()
