#-*-coding:utf-8-*-

START_BOOLEAN = True
START_SIGN = "*******"
SPLIT_SIGN = ";"
SPLIT_SIGN_CN = "；"


def file_read(file):
    with open(file, "r", encoding="utf8") as fp:
        dict = {}
        is_ent_process = False

        while True:
            read_line = fp.readline()

            if not read_line:
                break

            if is_begin_line(read_line):
                dict.clear()
                is_ent_process = True
                continue

            if is_end_line(read_line):
                is_ent_process = False
                print_dict(dict)
                continue

            if is_ent_process:
                key_value = split_line(read_line)
                input_dict(key_value, dict)

def is_begin_line(read_line):
    global START_BOOLEAN
    global START_SIGN

    read_line = read_line.strip()

    if read_line == START_SIGN and START_BOOLEAN:
        START_BOOLEAN = False
        return True

    return False

def is_end_line(read_line):
    global START_BOOLEAN
    global START_SIGN

    read_line = read_line.strip()

    if read_line == START_SIGN and not START_BOOLEAN:
        START_BOOLEAN = True
        return True

    return False

def split_line(read_line):
    global SPLIT_SIGN
    global SPLIT_SIGN_CN

    key_value = read_line.split(SPLIT_SIGN, 1)

    if len(key_value) < 2:
        key_value = read_line.split(SPLIT_SIGN_CN, 1)

        if len(key_value) < 2:
            raise Exception('日志格式有问题，需要联系工程师处理')

    key_value[0] = key_value[0].strip()
    key_value[1] = key_value[1].strip()
    return key_value

def input_dict(key_value, dict):
    dict[key_value[0]] = key_value[1]

def print_dict(dict):
    for d in dict:
        print("{0} : {1}".format(d, dict[d]))
