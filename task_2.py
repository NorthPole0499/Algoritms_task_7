def xor(a, b):
    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def division(dividend, divisor):
    curr = len(divisor)
    segment = dividend[0:curr]

    while curr < len(dividend):
        if segment[0] == '1':
            segment = xor(divisor, segment) + dividend[curr]
        else:
            segment = xor('0' * curr, segment) + dividend[curr]
        curr += 1

    if segment[0] == '1':
        segment = xor(divisor, segment)
    else:
        segment = xor('0' * curr, segment)

    return segment


def encode_data(data, key):
    appended_data = data + '0' * (len(key) - 1)
    remainder = division(appended_data, key)
    codeword = data + remainder

    return codeword


s = input('Введите текст, который нужно хэшировать: ')
data = ''.join(format(ord(x), 'b') for x in s)
crc = '00000100110000010001110110110111'
ans = encode_data(data, crc)
print('Хэшированный текст (CRC-32):', ans)
