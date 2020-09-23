begin =5
lines=begin
for line in range(lines):
    for number in range(begin - line,0, -1):
        print(number, end=' ' )
    print()

start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)
