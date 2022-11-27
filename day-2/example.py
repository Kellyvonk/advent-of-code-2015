list = "asdf\nasdf\nasdf"
split_list = list.split(sep="\n")



for element in split_list:
    for x in element:
        print(f'Element: {x}')





yolo = "1,2,3"

(a,b,c) = yolo.split(sep=",")

print(f'a={a} b={b} c={c}')





nums = [8, 5, 3, 9, 1, 7, 3]

highest = 0

for n in nums:
    if n > highest:
        highest = n

print(f'Hightest number is {highest}')