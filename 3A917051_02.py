import os
import json


def read_students_json(filename) -> dict:
    """讀取json檔"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_students_json(data, filename) -> None:
    """將資料寫入json檔"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dumps(data, file, indent=4, ensure_ascii=False)


def get_student_info(student_id) -> dict:
    """抓取學生資料"""
    for student in students_data:
        if student["student_id"] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到.")


def add_course(student_id, course_name, course_score) -> None:
    """添加一門課程成績"""
    for student in students_data:
        if student["student_id"] == student_id:
            student["courses"].append({"name": course_name,
                                       "score": course_score})
            return
    raise ValueError(f"學號 {student_id} 找不到.")
    assert course_name == "" or course_score == "", "=>其它例外: 課程名稱或分數不可空白."


def calculate_average_score(student_data) -> float:
    """計算學生平均成績"""
    c = student_data.get("courses", [])
    if not c:
        return 0.0
    t = sum(course["score"] for course in c)
    return t / len(c)


filename = "students.json"

if not os.path.isfile(filename):
    print("找不到學生資料檔案。")

students_data = read_students_json(filename)

while True:
    print("***************選單***************")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print("**********************************")
    choice = input("請選擇操作項目：")
    if choice == "1":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            print("=>學生資料:", json.dumps(student_info, indent=2,
                                        ensure_ascii=False))
        except ValueError as e:
            print("=>發生錯誤:", e)
    elif choice == "2":
        student_id = input("請輸入學號: ")
        course_name = input("請輸入要新增課程的名稱: ")
        course_score = input("請輸入要新增課程的分數: ")
        try:
            add_course(student_id, course_name, float(course_score))
            print("=>課程已成功新增。")
        except ValueError as e:
            print("=>發生錯誤:", e)
    elif choice == "3":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            average_score = calculate_average_score(student_info)
            print("=>各科平均分數:", average_score)
        except ValueError as e:
            print("=>發生錯誤:", e)
    elif choice == "4":
        print("=>程式結束。")
        break
    else:
        print("=>請輸入有效的選項。")