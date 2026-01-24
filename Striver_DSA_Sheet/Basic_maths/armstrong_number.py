n = int(input("Enter a number: "))

temp = n
count = 0

# Step 1: Count number of digits
while temp > 0:
    count = count + 1
    temp = temp // 10

temp = n
sum = 0

# Step 2: Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

# Step 3: Check
if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
