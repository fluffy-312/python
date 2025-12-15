sum_grade = 0
sum_credit = 0
grades = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
for i in range(20):
    name,credit,grade = input().split(" ")
    try:
        sum_grade += float(credit)*grades.get(grade)
        sum_credit += float(credit)
    except TypeError:
        continue

print(sum_grade/sum_credit)