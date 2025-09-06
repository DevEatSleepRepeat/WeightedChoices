students = ["Alice", "Bob", "Charlie", "David", "Emily", "James", "Olivia", "Noah", "Sophia", "Ethan", "Ava", "Liam", "Mia", "Jackson", "Isabella", "Logan", "Jeremy", "Evan", "Darby", "Bob"]
tables = 5
studentsPerTable = round(len(students)/tables)
count = 0

for t_count in range(0,tables):
    print("------------Table "+str(t_count))
    for i in range(0,studentsPerTable):
        try:
            print(students[count])
        except IndexError:
            1+1
        count += 1
    print()
