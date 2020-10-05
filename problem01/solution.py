# Parameter
N = 1000

# Initialize output
sum_out = 0

# Compute output
for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        sum_out += i

print(sum_out)
