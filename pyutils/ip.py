def binary_ipaddr( ip_str ):
    return '.'.join([bin(int(x)+256)[3:] for x in ip_str.split('.')])

if __name__ == '__main__':
    ip_base10 = '192.168.0.13'
    ip_binary = binary_ipaddr( ip_base10 )
    print ip_base10, '-->', ip_binary
    # 192.168.0.13 --> 11000000.10101000.00000000.00001101
