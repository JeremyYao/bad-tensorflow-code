from random import randint, random


def isEven(in_num: float) -> bool:
    return in_num % 2 == 0


increment_amount = 3
train_test_data_ratio = 0.1
iterations = 90000
file_name_input = "input.txt"
file_name_labels = "labels.txt"

data_dict = dict()
# Create a dictionary mapping a number to its result.

train_data_file_stream = open('train_data.csv', 'w')
test_data_file_stream = open('test_data.csv', 'w')

num = 0
for iteration in range(iterations):
    scalar = -1 if iteration % 2 == 0 else 1
    curr_num = scalar * num
    result = isEven(curr_num)
    data_dict[curr_num] = "even" if result else "odd"
    num += randint(0, increment_amount)

num = 0
for iteration in range(iterations):
    scalar = -1 if iteration % 2 == 0 else 1
    curr_num = float(scalar * num)
    result = isEven(curr_num)
    data_dict[curr_num] = "even" if result else "odd"
    num += randint(0, increment_amount)

num = 0.0000099
for iteration in range(iterations):
    scalar = -1 if iteration % 2 == 0 else 1
    curr_num = scalar * num
    result = isEven(curr_num)
    data_dict[curr_num] = "even" if result else "odd"
    num += random()*increment_amount

# Write headers
header_str = 'Value,Type,Result\n'
test_data_file_stream.write(header_str)
train_data_file_stream.write(header_str)

# Put data inside
for curr_num in data_dict.keys():
    line_str = f"{curr_num},{type(curr_num)},{data_dict[curr_num]}\n"
    if (random() <= train_test_data_ratio):
        test_data_file_stream.write(line_str)
    else:
        train_data_file_stream.write(line_str)


train_data_file_stream.close()
test_data_file_stream.close()
