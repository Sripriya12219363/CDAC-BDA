import csv
import json

def process_student_records(input_csv_path, output_json_path):
    students = []
    with open(input_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["score"] = float(row["score"])
            students.append(row)
    total_students = len(students)
    total_score = 0
    top_student = students[0]
    course_counts = {}
    for student in students:
        total_score += student["score"]
        if student["score"] > top_student["score"]:
            top_student = student
        course = student["course"]
        if course in course_counts:
            course_counts[course] += 1
        else:
            course_counts[course] = 1
    average_score = round(total_score / total_students, 2)
    summary = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": {
            "name": top_student["name"],
            "score": top_student["score"]
        },
        "course_counts": course_counts
    }

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)
def main():
    process_student_records("students.csv", "summary.json")

main()