def binary_ipaddr( addr ):
    return '.'.join([bin(int(x)+256)[3:] for x in addr.split('.')])

def ip2int( addr ):
    import socket, struct
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip( addr ):
    import socket, struct
    return socket.inet_ntoa(struct.pack("!I", addr))

def ip_in_network( addr, network ):
    """check whether a given IP address(currently only support IPv4) is in the given network
    addr: ip v4 address like 192.168.1.18
    network: ip network like 192.168.1.0/24
    """
    net, net_bits = network.split( '/' )
    mask = ( 0xFFFFFFFF << ( 32 - int( net_bits ) ) ) & 0xFFFFFFFF

    if ( ip2int( addr ) & mask ) == ( ip2int( net ) & mask ):
        return True

    return False

if __name__ == '__main__':
    ip_base10 = '192.168.0.13'
    ip_binary = binary_ipaddr( ip_base10 )
    print ip_base10, '-->', ip_binary
    # 192.168.0.13 --> 11000000.10101000.00000000.00001101
