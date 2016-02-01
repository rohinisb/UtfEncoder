import sys
out = open("utf8encoder_out.txt","w")


def get_value(b):
    return int("".join(map(lambda x: '%02x' % ord(x), b)), 16)

if len(sys.argv) != 0:
    f = open(sys.argv[1], 'rb')
    while 1:
        byte = f.read(2)
        if not byte: break
        intval = get_value(byte)
        binval = str('{0:08b}'.format(intval))
        if intval < 128:
            out.write(chr(int(binval, 2)))
        elif intval < 2048:
            d = binval.zfill(11)
            out.write(chr(int("110"+d[0:5], 2))+chr(int("10"+d[5:11], 2)))
        else:
            e = binval.zfill(16)
            out.write(chr(int("1110"+e[0:4], 2))+chr(int("10"+e[4:10], 2))+chr(int("10"+e[10:16], 2)))
