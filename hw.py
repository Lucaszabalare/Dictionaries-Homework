capitals = {"Ecuador" : "Quito" , "England" : "London" , "Italy" : "Rome"}

for key in capitals:
  print(key)
for key in capitals:
  print(capitals[key])

if "Spain" in capitals:
  print(capitals["Spain"])
else:
  print("Spain does not exist")
capitals["Spain"] = "Madrid"
print(capitals)
del(capitals["Italy"])
print(capitals)

# Changing a capital
capitals["England"] = "Wandsworth"
print(capitals)
print("Wandsworth is not a capital.")