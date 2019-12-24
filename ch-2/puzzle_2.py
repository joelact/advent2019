
def execute(codes, position, size):
    if position >= size:
        return

    value = codes[position]

    if value == 99:
        return

    if value == 1:
        position_to_add = codes[position+3]
        add_value = codes[codes[position+1]] + codes[codes[position+2]]
        if position_to_add < size:
            codes[position_to_add] = add_value

    if value == 2:
        position_to_add = codes[position+3]
        add_value = codes[codes[position+1]] * codes[codes[position+2]]
        if position_to_add < size:
            codes[position_to_add] = add_value

    return execute(codes, position + 4, size)


def find_noun_verb(codes):
    for i in range(0, 99):
        for j in range(0, 99):
            aux = list(codes)
            aux[1] = i
            aux[2] = j

            execute(aux, 0, size)

            if aux[0] == 19690720:
                print('noun: %d, verb: %d' % (i, j))
                return (i, j)

    return


f = open("input2", "r")

codes = list(map(lambda x: int(x), f.readline().strip().split(',')))

size = len(codes)

result = find_noun_verb(codes)

print('Result: %d' % (100 * result[0] + result[1]))
