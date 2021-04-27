# Print the square of each number on a separate line.

# The list of non-negative integers that are less than n is [0,1,2]

# Output:
# 0
# 1
# 4

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(0,n):
        a.append(i*i)
    print(*a, sep = "\n")