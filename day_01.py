import os
import numpy as np
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

lines1 = sorted([int(x.split("   ")[0]) for x in read_input_lines()])
lines2 = sorted([int(x.split("   ")[1]) for x in read_input_lines()])
part_a  = sum([abs(x-y) for x, y in zip(lines1,lines2)])
print(part_a,"partA: 2378066")
########################################################
array2 = np.array(lines2)
part_b = [x * np.size(np.where(array2 == x)[0]) for ind,x in enumerate(lines1)]

print(sum(part_b),"partB: 18934359")




