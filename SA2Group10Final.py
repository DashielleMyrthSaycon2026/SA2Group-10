def get_grades(quarter, kind):
    grades = []

    print("\n" + quarter + " " + kind + " Grades")
    print("Type the grades one by one. Press Enter if you are done")

    while True: 
        grade_input = input(kind + " grade #" + str(len(grades) + 1) + ": ")

        if grade_input == "":
            if len(grades) == 0:
                print("You need to enter at least one grade.")
            else:
                break
        else:
            grade = float(grade_input)

            if grade < 0 or grade > 100:
                print("Invalid grade. It should only be from 0 to 100.")
            else:
                grades.append(grade)

    return grades


def print_equivalent_grade(grade):
    if grade >= 96 and grade <= 100:
        print("Equivalent Grade: 1.00")
        print("Adjectival Equivalent: EXCELLENT")
    elif grade >= 90 and grade <= 95.99:
        print("Equivalent Grade: 1.25")
        print("Adjectival Equivalent: VERY GOOD")
    elif grade >= 84 and grade <= 89.99:
        print("Equivalent Grade: 1.50")
        print("Adjectival Equivalent: VERY GOOD")
    elif grade >= 78 and grade <= 83.99:
        print("Equivalent Grade: 1.75")
        print("Adjectival Equivalent: GOOD")
    elif grade >= 72 and grade <= 77.99:
        print("Equivalent Grade: 2.00")
        print("Adjectival Equivalent: GOOD")
    elif grade >= 66 and grade <= 71.99:
        print("Equivalent Grade: 2.25")
        print("Adjectival Equivalent: SATISFACTORY")
    elif grade >= 60 and grade <= 65.99:
        print("Equivalent Grade: 2.50")
        print("Adjectival Equivalent: SATISFACTORY")
    elif grade >= 55 and grade <= 59.99:
        print("Equivalent Grade: 2.75")
        print("Adjectival Equivalent: FAIR")
    elif grade >= 50 and grade <= 54.99:
        print("Equivalent Grade: 3.00")
        print("Adjectival Equivalent: FAIR")
    elif grade >= 40 and grade <= 49.99:
        print("Equivalent Grade: 4.00")
        print("Adjectival Equivalent: FAILED ON CONDITION")
    else:
        print("Equivalent Grade: 5.00")
        print("Adjectival Equivalent: FAILED")

quarters = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
quarter_grades = []

for i in range(4):
    print("\n=================================")
    print(quarters[i])

    formative_grades = get_grades(quarters[i], "Formative Assessment")
    summative_grades = get_grades(quarters[i], "Summative Assessment")

    formative_average = sum(formative_grades) / len(formative_grades)
    summative_average = sum(summative_grades) / len(summative_grades)

    tentative_grade = (formative_average * 0.30) + (summative_average * 0.70)


    if i == 0:
        quarter_grade = tentative_grade
    else: 
        quarter_grade = (tentative_grade * (2 / 3)) + (quarter_grades[i - 1] * (1 / 3))

    quarter_grades.append(quarter_grade)

    print("\nTentative Grade: " + str(round(tentative_grade, 2)))
    print("Quarter Grade: " + str(round(quarter_grade, 2)))
    print_equivalent_grade(quarter_grade)


final_grade = quarter_grades[3]

print("\n=================================")
print("Final Grade: " + str(round(final_grade, 2)))
print_equivalent_grade(final_grade)

    # FA average is 30%
    # SA average is 70%
    # 1st Quarter has no previous grade
    # 2nd to 4th quarter uses 2/3 current quarter and 1/3 previous quarter