count = int(input("How many SAs?: "))
sa_grades = []
for i in range(count):
     val = float(input("SA Grade Percentage: "))
     sa_grades.append(val)
sa_final = int(sum(sa_grades) / len(sa_grades))
