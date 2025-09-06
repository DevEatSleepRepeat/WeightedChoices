students = ["Alice", "Bob", "Charlie", "David", "Emily", "James", "Olivia", "Noah", "Sophia", "Ethan", "Ava", "Liam", "Mia", "Jackson", "Isabella", "Logan", "Jeremy", "Evan", "Darby", "Peter"]
tables = 4
studentsPerTable = round(len(students)/tables)
s_count = 0
incrorrect = []

rules = {
    "Evan":"Jeremy",
    "Bob":"Charlie",
    "Mia":"Isabella"}
for t_count in range(0,tables):
    print("------------Table "+str(t_count))
    table0 = ""
    for i in range(0,studentsPerTable):
        try:
            table0 += students[s_count]+"\n"
        except IndexError:
            1+1
        s_count += 1
    table_split = table0.split("\n")
    for i in table_split:
        try:
            if table0.find(i) and table0.find(rules[i]):
                print("==============NOTICE==============")

        except KeyError:
            1+1
    print(table0)
