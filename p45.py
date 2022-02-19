import math

def generate_hex(i):
    return i * (2*i - 1)
def generate_tri(i):
    return i*(i+1)/2
def generate_penta(i):
    return i * (3*i - 1) / 2


if __name__ == '__main__':

    tri = 286
    pent = 166
    hex = 144

    hex_num = generate_hex(hex)
    tri_num = generate_tri(tri)
    pent_num = generate_penta(pent)

    while hex_num != tri_num or hex_num != pent_num:
        if hex_num <= tri_num and hex_num <= pent_num:
            hex = hex + 1
            hex_num = generate_hex(hex)
        elif pent_num <= tri_num and pent_num <= hex_num:
            pent = pent + 1
            pent_num = generate_penta(pent)
        else:
            tri = tri + 1
            tri_num = generate_tri(tri)
    print(hex_num)

