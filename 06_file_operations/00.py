#f = open('Text.txt')
#print(f.readline())
filename = 'Text.txt'

# with open(filename, 'r') as f:
#     content = f.read()
#     print(content)

#try:
 #   with open(filename, 'r') as fopen:
 #   except FileExistsError:

# with open(filename, 'r') as fopen:
#     for line in fopen:
#         print(line)

# with open(filename, 'r') as fopen:
#     while True:
#         current_line = fopen.readline()
#         # aktualna linia jest pusta
#         if current_line == '':
#             break
#         print(current_line)

with open(filename, 'r') as fopen:
  lines = fopen.readlines()

# for nr in range(len(lines)):
#     print(f'Linia {nr} -> {lines[nr]}')

# for nr, value in enumerate(lines)   :
#     print(f'linia {nr} --> {value}')

# with open('save.txt', 'w') as f:
#   f.write('Line 1\n')
#   f.write('Line 2\n')
#   f.write('Line 3\n')
#   f.write('Line 4\n')
#   f.write('The end!')
#
#   f.write('Line 1\t')
#   f.write('Line 2\t')
#   f.write('Line 3\t')
#   f.write('Line 4\t')
#   f.write('The end!')

sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']

with open('save.txt', 'w') as f:
    f.write('\n'.join(sweets_list))