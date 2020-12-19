from utils.classes import *

def get_lines_as_dict(start_time, end_time, fd):
    ret = []
    i = 0
    go_one_line_back(fd)
    line = line_to_dict(fd.readline())
    while line != "" and times(line["iso_time"]).earlier_than(start_time):
        line = line_to_dict(fd.readline())
    while line != "" and times(line["iso_time"]).earlier_than(end_time):
        ret.append(line)
        line = line_to_dict(fd.readline())
    return ret

def get_lines_as_dict_backwards(start_time, end_time, fd):
    ret = []
    i = 0
    fd.seek(-1, 2) #goto byte before EOF
    go_one_line_back(fd)
    line = line_to_dict(fd.readline())
    while times(line["iso_time"]).earlier_than(end_time) == False:
        go_one_line_back(fd)
        go_one_line_back(fd)
        line = line_to_dict(fd.readline())
    while times(line["iso_time"]).earlier_than(start_time) == False:
        go_one_line_back(fd)
        go_one_line_back(fd)
        ret.append(line)
        line = line_to_dict(fd.readline())
    return ret
