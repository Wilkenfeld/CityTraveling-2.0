import samples.classes.core as core
import math

def calc_distances(path):
    i = 0
    tot = list()
    while i < len(path) - 1:
        xa = core.position_dict[str(path[i])][0]
        xb = core.position_dict[str(path[i + 1])][0]
        ya = core.position_dict[str(path[i])][1]
        yb = core.position_dict[str(path[i + 1])][1]

        tot.append(math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2))

    return tot