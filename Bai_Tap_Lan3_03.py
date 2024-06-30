read_file = 'names.txt'
with open(read_file, 'r') as f:
    all_lines = f.read()
names = all_lines.replace('"', '').split(',')

sort_names = sorted(names)


def value(char):
    # Chuyển đổi ký tự chữ cái thành giá trị tương ứng
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    else:
        raise ValueError("Input must be a single letter from A-Z")

def sum_of_string_values(s):
    # Tính tổng giá trị của các chữ cái trong chuỗi
    total = 0
    for char in s:
        total += value(char)
    return total
# for  in sort_names:
#     print(sum_of_string_values(sort_names[i])) 
for i in sort_names:
    print("sau khi sort: ",i)
print(sum_of_string_values(sort_names[4]))


