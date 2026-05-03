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


def print_equivalent_grades(grade):
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


