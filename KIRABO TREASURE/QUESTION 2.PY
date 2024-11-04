def syracuse_sequence(x):
    if x <= 0:
        return "Input must be a natural number"
    sequence = [x]
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    return sequence

start_value = int(input("Enter the starting value: "))
print(f"The Syracuse sequence starting with {start_value} is {syracuse_sequence(start_value)}")
