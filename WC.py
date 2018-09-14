import sys
import re


"""
read the file contents
parameters
        file_path(string)：the file path
return：
        lines(list)：the file content
"""
def read_file(file_path):
    with open(file_path, encoding='UTF-8') as file:
        lines = file.readlines()
    return lines


"""
count the char num of the file
parameters:
        lines(list)：the file content
return：
        char_num(int)：the char num of the file
"""
def char_counter(lines):
    char_num = 0
    for line in lines:
        line = re.sub('\s', '', line)
        char_num += len(line)
    return char_num


"""
count the line num of the file
parameters:
        lines(list)：the file content
return:
        line_num(int)：the line num of the file
"""
def line_counter(lines):
    line_num = len(lines)
    return line_num


"""
count the word num of the file
parameters:
        lines(list)：the file content
return:
        word_num(int)：the word num of the file
"""
def word_counter(lines):
    word_num = 0
    for line in lines:
        line = re.split('[^\w]+', line)
        while "" in line:
            line.remove("")
        word_num += len(line)
    return word_num


"""
count the null/coding/annotation line num of the file
parameters:
        lines(list)：the file content
return:
        null_line_num(int)：the null line num of the file
        coding_line_num(int)：the coding line num of the file
        annotation_line_num(int)：the annotation line num of the file
"""
def extended_function_a(lines):
    null_line_num = 0
    coding_line_num = 0
    annotation_line_num = 0
    is_annotation = False
    for line in lines:
        is_null = False

        # the null line test
        null_line = re.sub('\s', '', line)
        if len(null_line) <= 1:
            null_line_num += 1
            is_null = True

        # the annotation line test
        # the head of annotation with """
        if '"""' in line and len(line.split('"""')[0].strip()) == 0 and is_annotation == False:
            annotation_line_num += 1
            is_annotation = True
            continue
        # the tail of annotation with """
        elif '"""' in line and len(line.split('"""')[-1].strip()) == 0 and is_annotation == True:
            annotation_line_num += 1
            is_annotation = False
            continue
        # the annotation content with """
        elif is_annotation == True:
            annotation_line_num += 1
            continue

        # the annotation line with #
        if '#' in line:
            first_part = re.sub('\s', '', re.split('#', line)[0])
            if len(first_part) <= 1:
                annotation_line_num += 1
                continue

        if is_null == True:
            continue

        # the coding line test
        coding_line_num += 1

    return null_line_num, coding_line_num, annotation_line_num



if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1 or args[1] not in ['-c', '-w', '-l', '-a']:
        print('usage:')
        print('WC.exe -c filename   (counting the char num)')
        print('WC.exe -w filename   (counting the word num)')
        print('WC.exe -l filename   (counting the line num)')
        print('WC.exe -a filename   (the extend function -a)')
        sys.exit(0)
    try:
        # read the file
        lines = read_file(args[2])

        if args[1] == '-c':     # count the char num
            char_num = char_counter(lines)
            print('the char num is ', char_num)
        elif args[1] == '-w':   # count the word num
            word_num = word_counter(lines)
            print('the word num is ', word_num)
        elif args[1] == '-l':   # count the line num
            line_num = line_counter(lines)
            print('the line num is ', line_num)
        elif args[1] == '-a':   # the extended function
            null_line_num, coding_line_num, annotation_line_num = extended_function_a(lines)
            print('the null line num is ', null_line_num)
            print('the coding line num is ', coding_line_num)
            print('the annotation line num is ', annotation_line_num)
    except:
        print('the file is not found.')