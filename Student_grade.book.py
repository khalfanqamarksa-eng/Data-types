grade_book = {
    "Alice":85,
    "Bob":92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}
total_score = 0
for score in grade_book.values():
    total_score += score
    class_average = total_score / len(grade_book)
    print("Class Average Score:", class_average)
top_student= max(grade_book, key=grade_book.get)
print("top student:", top_student)
bottom_student = min(grade_book, key = grade_book.get)
print("bottom student:", bottom_student)
search_name = input("Enter the name of any Student for their score: ")
student_score = grade_book.get(search_name, "Student not found in the grade book.")
print("Search Result:", student_score)
