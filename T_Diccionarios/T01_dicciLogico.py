age = 25

if age < 18:
    status = "Too young"
elif age == 18:
    status = "Still too young"
elif 18 < age < 20:
    status = "Old enough now"
elif 20 <= age <= 40:
    status = "perfect"
else:
    status = "Welcome"
    
print(status)

# Forma dos para resolver el mismo problema
el_estatus = {
    (age < 18):"Too young",
    (age == 18): "Still too young",
    (18 < age < 20): "Old enough now",
    (20 <= age <40): "Perfect",
    (age >= 40): "Welcome",
}[True]

print(el_estatus)
