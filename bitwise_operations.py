import sys

try:
  integers = [int(value) for value in sys.argv[1].split(',')]
  threshold = int(sys.argv[2]) 
except ValueError:
  print("<span>All numbers and threshold must be integers</span>")
  sys.exit()

bitwise_and = integers[0]
bitwise_or = integers[0]
bitwise_xor = integers[0]

for current_integer in integers[1:]:
  bitwise_and &= current_integer
  bitwise_or |= current_integer
  bitwise_xor ^= current_integer

filtered = [integer for integer in integers if integer > threshold]

html_output = (
  f"<p>Bitwise AND: {bitwise_and}</p>"
  f"<p>Bitwise OR: {bitwise_or}</p>"
  f"<p>Bitwise XOR: {bitwise_xor}</p>"
  f"<p>Values gratear than threshold: {filtered}</p>"
)

print(html_output)

# # Input: Retrieve values from the user
# raw_input = input("Enter a list of integers separated by spaces: ").split()

# # Validate input to ensure it contains only integers
# numbers = []
# for item in raw_input:
#     item = item.strip()
#     if item.isdigit():
#         numbers.append(int(item))
#     else:
#         print(f"Error: '{item}' is not a valid integer.")
#         exit()

# # Bitwise Operations
# and_result = numbers[0]
# or_result = numbers[0]
# xor_result = numbers[0]

# for num in numbers[1:]:
#     and_result &= num
#     or_result |= num
#     xor_result ^= num

# print(f"Bitwise AND result: {and_result}")
# print(f"Bitwise OR result: {or_result}")
# print(f"Bitwise XOR result: {xor_result}")

# # Filtering
# threshold_input = input("Enter a threshold value: ")
# if threshold_input.isdigit():
#     threshold = int(threshold_input)
#     filtered_numbers = []
#     for num in numbers:
#         if num > threshold:
#             filtered_numbers.append(num)
#     print(f"Numbers greater than {threshold}: {filtered_numbers}")
# else:
#     print("Error: Threshold must be an integer.")
