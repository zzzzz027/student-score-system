def save_record(name, score):
    with open("students.txt", "a", encoding="utf-8") as f:
        f.write(f"{name},{score}\n")
    print("已保存到 students.txt")