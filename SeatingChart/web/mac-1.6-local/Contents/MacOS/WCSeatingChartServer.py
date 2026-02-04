from flask import Flask, request, jsonify
from flask_cors import CORS
from random import shuffle

# Setup flask app.
app = Flask(__name__)
CORS(app)

def generate_seating_chart(students:list,tables:int,rules:dict):
    # Generate standard tables without the ruleset applied.
    studentsPerTable = round(len(students)/tables)
    s_count = 0
    tables_list = []
    for t_count in range(tables):
        table = []
        for i in range(studentsPerTable):
            if s_count < len(students):
                table.append(students[s_count])
            s_count += 1
        tables_list.append(table)

    shuffle(tables_list) # Shuffle the tables for more random results.

    # Detect rule conflicts and swap.
    for t_index, table in enumerate(tables_list):
        for student in list(table):
            if student in rules:
                partner = rules[student]
                if partner in table:
                    # Find another table to swap with.
                    for other_t_index, other_table in enumerate(tables_list):
                        if other_t_index != t_index:
                            for swap_candidate in other_table:
                                if swap_candidate not in rules.values():
                                    # Perform swap
                                    si, oi = table.index(student), other_table.index(swap_candidate)
                                    table[si], other_table[oi] = other_table[oi], table[si]
                                    #print(f" -> Swapped {student} with {swap_candidate} (from Table {other_t_index}) to avoid {student} and {partner} sitting together.")
                                    break
                            break

    # Print final tables
    return tables_list

# Define generation endpoint.
@app.route("/generate", methods=["POST"])
def api_generate():
    data = request.get_json()

    students = data.get("students")
    tables = data.get("tables")
    rules = data.get("rules")

    result = generate_seating_chart(students, tables, rules)

    return jsonify({"tables": result})

# Define index endpoint.
@app.route("/", methods=["GET"])
def main():
    with open("index.html","r") as indexHTML:
        return indexHTML.read()

# Run server!
if __name__:
    app.run(host="0.0.0.0", port=80)