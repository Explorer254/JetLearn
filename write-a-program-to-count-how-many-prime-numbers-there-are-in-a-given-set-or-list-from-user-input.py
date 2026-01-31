numbers = []

while True:
    s = int(input("Enter some numbers here to check wheter they are prime numbers or not:"))
    if s == -1:
        break
    numbers.append(s)

count = 0

for n in numbers:
    if n > 1:
        i = 2
        prime = True
        while i < n:
            if n % i ==0:
                prime = False
                break
            i+=1

        if prime:
            count += 1

print(count)
