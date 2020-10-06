def popcnt1(n):
    return format(n, '08b').count("0")

print(popcnt1(0b0111))