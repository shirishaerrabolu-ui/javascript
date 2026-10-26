students = {
    "Riya": ["Math", "Science", "English", "Math"],
    "Arjun": ["History", "Math", "History"],
    "Priya": ["Science", "English", "Science"],
    "Rahul": ["Math", "Computer", "English", "Math"]
}

print("===== STUDENT SUBJECT RECORD CLEANER =====")

for student, subjects in students.items():
    cleaned_subjects = list(dict.fromkeys(subjects))

    students[student] = cleaned_subjects

    print("\nStudent:", student)
    print("Original Subjects:", subjects)
    print("Cleaned Subjects:", cleaned_subjects)
    print("Total Unique Subjects:", len(cleaned_subjects))

print("\n===== CLEANED STUDENT RECORDS =====")

for student, subjects in students.items():
    print(student, ":", ", ".join(subjects))

print("\nAll duplicate subjects have been removed!")