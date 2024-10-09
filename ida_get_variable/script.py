import ida_bytes

def get_arr(addr,length):

    values = []
    for i in range(length):
        value = ida_bytes.get_byte(addr + i)
        values.append(value)


    value_hexes = ','.join([f'0x{x:02x}' for x in values])
    print(f'[{value_hexes}]')
