student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_Integration": "English, Math, Science"},
    "id2": {"name": "David", "class": "V", "subject_Integration": "English, Math, Science"},
    "id3": {"name": "Sara", "class": "V", "subject_Integration": "English, Math, Science"},
    "id4": {"name": "Surya", "class": "V", "subject_Integration": "English, Math, Science"},
}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key =(details["name"], details["class"], details["subject_Integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]= details
for k , v in result.items():
    print(k,":",v)