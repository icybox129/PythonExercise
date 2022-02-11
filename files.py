#1

teams = ["Sportball1", "Fightball2", "Momball3", "Murderball4", "Fightstick"]

with open("teams.txt", "w") as file:
    for x in teams:
        newline = f"{x}\n"
        file.write(newline)

with open("teams.txt", "r") as file:
    print(file.readline())
    file.readline()
    file.readline()
    print(file.readline())

#2

with open("teams.txt", "r") as file:
    lines = file.readlines()
    lines[0] = "I like sports\n"

with open("teams.txt", "w") as file:
    for x in lines:
        newline = f"{x}"
        file.write(newline)

print(lines)