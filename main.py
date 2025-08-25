import sqlite3, time

# Intro
print("""____________________________________________
|=================WCTbCB===================|
|=Weighted Choices Text-based Concept Beta=|
|=================v0.7.2===================|""")

# Setup Database
r_time = round(time.time())
save_name = "weights_"+str(r_time)+".db" # Make Filename

cw_lib = sqlite3.connect(save_name)
cur = cw_lib.cursor()
existing_combos = []
cur.execute("CREATE TABLE IF NOT EXISTS weights (choice TEXT, weight REAL)") # Create Table
cw_lib.commit() # Commit Changes

def null():
    five = 2+2
    five.bit_count()

def update_data(a,b):
    global existing_combos
    print(a + " or " + b)
    existing_combos.append(a)
    print("Press 1 for " + a + ", and 2 for " + b)
    inp = input(">>> ")
    try:
        inp = int(inp)
        if inp == 1:
            cur.execute("UPDATE weights SET weight = weight + 0.1 WHERE choice = ?", (a,))
            cur.execute("UPDATE weights SET weight = weight - 0.1 WHERE choice = ?", (b,))
            cw_lib.commit()
        elif inp == 2:
            cur.execute("UPDATE weights SET weight = weight - 0.1 WHERE choice = ?", (a,))
            cur.execute("UPDATE weights SET weight = weight + 0.1 WHERE choice = ?", (b,))
            cw_lib.commit()
    except ValueError:
        print("Invalid Input, choices added at random.")
        cur.execute("UPDATE weights SET weight = weight + 0.1 WHERE choice = ?", (a,))
        cur.execute("UPDATE weights SET weight = weight - 0.1 WHERE choice = ?", (b,))

def get_weights(choices):
    global existing_combos
    # Create Base Data
    for i in choices:
        cur.execute("INSERT OR IGNORE INTO weights VALUES (?, ?)", (i, "0.0"))
    cw_lib.commit()
    # Start the data collection processes.
    for idx_i, i in enumerate(choices):
        for idx_j, j in enumerate(choices):
            if idx_j <= idx_i:
                continue  # Skip duplicates and self-comparisons
            update_data(i, j)

def main():
    print("|____Press [ENTER] to begin!_______________|")
    input()
    breakfast = ["Pancakes", "Bacon", "Eggs", "Grits", "Waffles", "Bagles", "Sausage"]
    get_weights(breakfast)
    #print("\nSuccessfully Completed!\nOutput weights saved to "+save_name)
    cur.execute("SELECT * FROM weights ORDER BY weight DESC;")
    cw_lib.commit()
    print("\n\n|=========================================|\n|=Your Results:===========================|")
    output_data = []
    for row in cur.execute("SELECT * FROM weights"):
        output_data.append(row)
    for r in output_data:
        line = ""
        for n in r:
            try:
                num = round(n,1)
                line += str(num)
            except TypeError:
                line += "|="+n+" "
        print(line)
        print("|=========================================|")

main()