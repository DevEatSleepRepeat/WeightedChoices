import sqlite3, time

# Intro
print("""____________________________________________
|=================WCTbCB===================|
|=Weighted Choices Text-based Concept Beta=|
|=================v0.7.2===================|""")

# Setup Database
rtime = round(time.time())
save_name = "weights_"+str(rtime)+".db" # Make Filename

cw_lib = sqlite3.connect(save_name)
cur = cw_lib.cursor()
existing_combos = []
cur.execute("CREATE TABLE IF NOT EXISTS weights (id INTEGER, choice TEXT, weight REAL)") # Create Table
cw_lib.commit() # Commit Changes

def null():
    five = 2+2
    five.bit_count()

def update_data(a,b):
    global existing_combos
    print(a + " or " + b)
    existing_combos.append(a)
    print("Press 1 for " + a + ", and 2 for " + b)
    inp = int(input(">>> "))
    if inp == 1:
        cur.execute("UPDATE weights SET weight = weight + 0.1 WHERE choice = ?", (a,))
        cur.execute("UPDATE weights SET weight = weight - 0.1 WHERE choice = ?", (b,))
        cw_lib.commit()
    elif inp == 2:
        cur.execute("UPDATE weights SET weight = weight - 0.1 WHERE choice = ?", (a,))
        cur.execute("UPDATE weights SET weight = weight + 0.1 WHERE choice = ?", (b,))
        cw_lib.commit()
    else:
        null()

def get_weights(choices):
    global existing_combos
    count = 1
    # Create Base Data
    for i in choices:
        cur.execute("INSERT OR IGNORE INTO weights VALUES (?, ?, ?)", (str(count), i, "0.0"))
        count += 1
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
    breakfast = ["Pancakes", "Bacon","Eggs", "Grits", "Waffles", "Bagles", "Sausage"]
    get_weights(breakfast)

main()