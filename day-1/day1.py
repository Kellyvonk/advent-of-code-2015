floors = open('input', 'r')

floors = floors.read()


total_floors = 0

for letter in floors:
    if letter == '(':
        total_floors = total_floors +1
    
    if letter == ')':
        total_floors = total_floors -1

print (total_floors)

total_floors_door = 0
position = 1
n = -1

for letter in floors:
    if letter == '(':
        total_floors_door +=1
    
    if letter == ')':
        total_floors_door -=1

    if n == total_floors_door:
        break

    position = position +1
print (position)