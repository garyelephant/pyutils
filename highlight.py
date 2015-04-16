class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def highlight( s, **term_color ):
    """return ANSI color rendered string
    This will work on unixes including OS X, linux and windows (provided you enable ansi.sys).
    """
    color_pos = {}

    for term, color in term_color.items():
        start = 0
        while start < len( s ):
            term_start = s.find( term, start )
            term_end = term_start + len( term )
            if term_start == -1:
                break
            start = term_start + 1

            color_pos[ term_start ] = color
            color_pos[ term_end ] = bcolors.ENDC

    if len( color_pos ) == 0:
        return s 

    segments = []
    last_i = 0
    for i in range( len( s ) + 1 ):
        if i in color_pos:
            segments.append( s[ last_i : i ] )
            segments.append( color_pos[ i ] )
            last_i = i
    segments.append( s[ last_i : ] )
        
    return ''.join( segments )
            
if __name__ == '__main__':
    s = "How to print string with color in terminal? \n" \
         "This somewhat depends on what platform you are on. \n" \
         "The most common way to do this is by printing ANSI escape sequences."

    terms_color = {
                      'print string with color': bcolors.WARNING,
                      'platform': bcolors.OKBLUE,
                      'ANSI escape sequences': bcolors.FAIL
                  }
    print highlight( s, **terms_color )
