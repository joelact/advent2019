
def execute(codes, position):
    if position >= len(codes):
        return

    value = codes[position]

    if value == 99:
        return

    if value == 1:
        position_to_add = codes[position+3]
        add_value = codes[codes[position+1]] + codes[codes[position+2]]
        codes[position_to_add] = add_value

    if value == 2:
        position_to_add = codes[position+3]
        add_value = codes[codes[position+1]] * codes[codes[position+2]]
        codes[position_to_add] = add_value

    return execute(codes, position + 4)


f = open("input", "r")

codes = list(map(lambda x: int(x), f.readline().strip().split(',')))

execute(codes, 0)

print(codes)
