print("Enter the marks of 5 subjects: ")
math = int(input("maths :")) 
english = int(input("english :")) 
science = int(input("science :"))
computer = int(input("Computer: "))
social = int(input("Social: "))


sum = math + english + science + computer + social
print("sum of math, english, science, computer, social: ")
perc = (sum/500)*100
print(f"Percentage Mark = {perc}")