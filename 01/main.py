from os import path

input_file = 'input_01.txt'

total_elf_food = []
with open(input_file) as file_object:
    lines = file_object.readlines()
    elf_total = 0
    for line in lines:
        line = line.rstrip('\n')
        if line != '':
            elf_total += int(line)
        else:
            total_elf_food.append(elf_total)
            elf_total = 0
    
    print(max(total_elf_food)) # Answer to first challenge
    print(sum(sorted(total_elf_food)[-3:])) # Answer to second challenge