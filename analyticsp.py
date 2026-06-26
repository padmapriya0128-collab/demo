def student_analyze(cgpa, skill, projects, certifications, internships):
    score = 0
    strength = []
    weakness = []
    recommendations = []

    if cgpa >= 8:
        cgpa_score = 25
        score += cgpa_score
        strength.append("good at academics")
    elif cgpa >= 7:
        cgpa_score = 15
        score += cgpa_score
        weakness.append("average at academics")
    else:
        cgpa_score = 0
        weakness.append("not good at academics")
        recommendations.append("improve academics")

    all_skills = ["python","java","c++","html","css","javascript","sql","react","node.js"]
    if skill.lower() in all_skills:
        skill_score = 30
        score += skill_score
        strength.append("good at skills")
    else:
        skill_score = 0
        weakness.append("need to improve skills")
        recommendations.append("learn new skills")

    if projects >= 5:
        project_score = 20
        score += project_score
        strength.append("good at technical projects")
    elif projects >= 3:
        project_score = 10
        score += project_score
        weakness.append("average at technical projects")
    else:
        project_score = 0
        weakness.append("not good at technical projects")
        recommendations.append("work on more technical projects")

    if certifications >= 5:
        certification_score = 10
        score += certification_score
        strength.append("good at certifications")
    elif certifications >= 3:
        certification_score = 5
        score += certification_score
        weakness.append("average at certifications")
    else:
        certification_score = 0
        weakness.append("not good at certifications")
        recommendations.append("pursue more certifications")

    if internships >= 3:
        internship_score = 15
        score += internship_score
        strength.append("good at internships performance")
    elif internships >= 1:
        internship_score = 5
        score += internship_score
        weakness.append("average at internships performance")
    else:
        internship_score = 0
        weakness.append("not good at internships performance")
        recommendations.append("gain more internship experience")

    if score >= 80:
        readiness = "Placement Ready"
    elif score >= 60:
        readiness = "Needs Improvement"
    else:
        readiness = "Not Ready"
        recommendations.append("work on all areas to improve readiness")

    return {
        "score": score,
        "readiness": readiness,
        "strength": strength,
        "weakness": weakness,
        "recommendations": recommendations,
        "cgpa_score": cgpa_score,
        "skill_score": skill_score,
        "project_score": project_score,
        "certification_score": certification_score,
        "internship_score": internship_score
    }

if __name__ == "__main__":
    result = student_analyze('7.5','python','5','5','3')
    print(result)


