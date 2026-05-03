p = bool(int(input('enter value for p (1 = True, 0 = False): ')))
q = bool(int(input('enter value for q (1 = True, 0 = False): ')))

print("\nTruth Table:")
print("p AND q:", p and q)
print("p OR q:", p or q)
print("NOT p:", not p)
print("p => q:", (not p) or q)
print("p <=> q:", p == q)