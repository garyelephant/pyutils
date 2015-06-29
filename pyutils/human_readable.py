# coding: utf-8

def sizeof_fmt(num, suffix='B'):
    """
    Supports:
        all currently known binary prefixes, https://en.wikipedia.org/wiki/Binary_prefix#Specific_units_of_IEC_60027-2_A.2_and_ISO.2FIEC_80000
        negative and positive numbers
        numbers larger than 1000 Yobibytes
        arbitrary units (maybe you like to count in Gibibits!)
    """
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
    

if __name__ == '__main__':
    # '157.4GiB'
    sizeof_fmt(168963795964)
    
