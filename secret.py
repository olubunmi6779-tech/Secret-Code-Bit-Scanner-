# MY SECRET CODE BIT SCANNER

secret_code = 26
access_key = 10

def bits(number):
    return format(number, "04b")

print("MY SECRET CODE BIT SCANNER")

print("Secret Code:", secret_code)
print("Secret Code in Binary:", bits(secret_code))

print("Access Key:", access_key)
print("Access Key in Binary:", bits(access_key))

print()

and_result = secret_code & access_key
or_result = secret_code | access_key

print("AND AND OR OPERATIONS")

print("AND Result:", and_result)
print("AND Result in Binary:", bits(and_result))

print("OR Result:", or_result)
print("OR Result in Binary:", bits(or_result))

print()


not_result = (~secret_code) & 0b1111
xor_result = secret_code ^ access_key

print("NOT AND XOR OPERATIONS")

print("NOT Result:", not_result)
print("NOT Result in Binary:", bits(not_result))

print("XOR Result:", xor_result)
print("XOR Result in Binary:", bits(xor_result))

print()


left_shift_result = secret_code << 1
right_shift_result = secret_code >> 1

print("SHIFT OPERATIONS")

print("Left Shift Result:", left_shift_result)
print("Left Shift in Binary:", bits(left_shift_result))

print("Right Shift Result:", right_shift_result)
print("Right Shift in Binary:", bits(right_shift_result))

print()


xor_check = secret_code ^ 1

print("ODD OR EVEN CHECK")

print("Secret Code:", secret_code)
print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("The secret code is ODD.")
else:
    print("The secret code is EVEN.")

print()

bit_count = secret_code.bit_count()

print("==========================================")
print("BIT COUNT")
print("==========================================")

print("Secret Code in Binary:", bits(secret_code))
print("Number of 1 bits:", bit_count)

print()


print("FINAL SUMMARY")

print("Secret Code:", secret_code)
print("Secret Code Binary:", bits(secret_code))

print("Access Key:", access_key)
print("Access Key Binary:", bits(access_key))

print("AND Result:", and_result)
print("OR Result:", or_result)
print("NOT Result:", not_result)
print("XOR Result:", xor_result)

print("Left Shift Result:", left_shift_result)
print("Right Shift Result:", right_shift_result)

print("Number of 1 bits:", bit_count)

print("PROGRAM COMPLETE")