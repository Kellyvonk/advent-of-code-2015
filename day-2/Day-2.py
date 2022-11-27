import statistics

# surface area = 2*l*w + 2*w*h + 2*h*l

input = open ('input', 'r').read()

print (input)

boxlist = input.split(sep="\n")

print (boxlist)

boxarea = 0
total = 0
total2 = 0

for box in boxlist:

    boxsize = box.split(sep="x")
    (l,w,h) = box.split(sep='x')
    l = int(l)
    w = int(w)
    h = int(h)

    boxarea = 2*l*w + 2*w*h + 2*h*l

    small = min(l*w, w*h, h*l)

    total += boxarea
    total2 += small

total3 = total + total2

print (total)
print (total2)
print (total3)

wraps = 0
bow = 0

for box in boxlist:

    boxsize = box.split(sep="x")
    (l,w,h) = box.split(sep='x')
    l = int(l)
    w = int(w)
    h = int(h)

    shorty = min(l,w,h)

    remedial = statistics.median([l,w,h])

    wrapper = shorty + shorty + remedial + remedial

    wraps += wrapper

    bowsize = l*w*h

    bow += bowsize 

ribbon = wraps + bow

print (ribbon)


# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.







