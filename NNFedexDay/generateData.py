from random import randint, random


def isEven(in_num: float) -> bool:
    return in_num % 2 == 0


train_test_data_ratio = 0.1
iterations = 900000
file_name_input = "input.txt"
file_name_labels = "labels.txt"

data_dict = dict()
# Create a dictionary mapping a number to its result.

train_data_file_stream = open('train_data.csv', 'w')
test_data_file_stream = open('test_data.csv', 'w')

num = 0
for iteration in range(iterations):
    scalar = -1 if num % 2 == 0 else 1
    curr_num = scalar * num
    result = isEven(curr_num)
    data_dict[curr_num] = "even" if result else "odd"
    num += randint(1, 3)

# Write headers
test_data_file_stream.write('Value,Result\n')
train_data_file_stream.write('Value,Result\n')

# Put data inside
for curr_num in data_dict.keys():
    if (random() <= train_test_data_ratio):
        test_data_file_stream.write(
            # f"{curr_num},{type(curr_num)},{1 if data_dict[curr_num] == 'even' else 0}\n")
            f"{curr_num},{data_dict[curr_num]}\n")
    else:
        train_data_file_stream.write(
            # f"{curr_num},{type(curr_num)},{1 if data_dict[curr_num] == 'even' else 0}\n")
            f"{curr_num},{data_dict[curr_num]}\n")


train_data_file_stream.close()
test_data_file_stream.close()
