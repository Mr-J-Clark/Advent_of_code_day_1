# Open the file in read mode

col1 = []
col2 = []
total_diff = 0
with open("day1.txt", "r") as file:
    # Read lines and strip newline characters
    lines = [line.strip() for line in file.readlines()]

# Print the list
print(lines)

# for line in lines:
#     col1 = line

# Split each string into two separate values
separated_data = [item.split() for item in lines]

# Print the result
print(separated_data)

for i in range(len(separated_data)):
        col1.append(int(separated_data[i][0]))
        col2.append(int(separated_data[i][1]))



col1.sort()
col2.sort()
print (col1)
print (col2)
for i in range(len(col1)):
    if col1[i] >= col2[i]:
        diff = col1[i] - col2[i]
    else:
        diff = col2[i] - col1[i]
    total_diff += diff
    #( you could do total_diff += abs(col1[i] - col2[i]))

print (total_diff)