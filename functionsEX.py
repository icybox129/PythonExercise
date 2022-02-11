name = input("Enter your first name: ")
homework = int(input("Enter your homework score (MAX 25): "))
assessment = int(input("Enter your assessment score (MAX 50): "))
final = int(input("Enter your final exam score (MAX 100): "))


def calc(homework, assessment, final):
    return (homework + assessment + final) / 175 * 100

grade = round(calc(homework, assessment, final))

print(f"Hi {name}, your overall percentage for this course is", grade)