#type conversion example
birth_year=input("Birth year:")
age=2026 - int(birth_year)
print(type(birth_year))
print(age)
print(type(age))
can_drive= age>18
print(bool(can_drive))

height=float(input("Enter your height"))
print(height,"Foot")

weight_in_grams=input("Enter your weight:")
Weight_in_kg=float(weight_in_grams)*0.001
print(Weight_in_kg)




