import os
import numpy as np
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip().split() for x in fh.readlines()]


lines = read_input_lines()
lines_sorted = []
def safe(inp):
    inp = list(map(int, inp))  # cast items to numbers
    if sorted(inp) == inp or sorted(inp, reverse=True) == inp:  # check if increasing or decreasing
        diffs = []
        for i in range(1, len(inp)):
            diffs.append(abs(inp[i] - inp[i - 1]))  #
        if max(diffs) < 4 and min(diffs) > 0:  # check if diff between lvl is 1,2 or 3
            return True
    return False
for x in lines:
    if safe(x):
        lines_sorted.append(x)

print(len(lines_sorted),"partA: 472")
##################################################
lines_sorted = []
for x in lines:
    if safe(x):
        lines_sorted.append(x)
    else:
        for ind,item in enumerate(x):
            temp_list = x.copy()
            del temp_list[ind]
            if safe(temp_list):
                lines_sorted.append(x)
                break
print(len(lines_sorted),"partB: 520")



