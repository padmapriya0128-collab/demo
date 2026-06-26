import matplotlib.pyplot as plt
from analytics import student_analyze

result = student_analyze(0, 0, 0, 0, 0)

categories = [
    "Academics",
    "Skills",
    "Projects",
    "Certifications",
    "Internships"
]

scores = [
    result["cgpa_score"],
    result["skill_score"],
    result["project_score"],
    result["certification_score"],
    result["internship_score"]
]

plt.figure(figsize=(8,5))
plt.bar(categories, scores)

plt.title("Student Performance Analysis")
plt.xlabel("Categories")
plt.ylabel("Score")

plt.show()