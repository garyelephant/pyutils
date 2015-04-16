class colors:
    '''Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

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
            color_pos[ term_end ] = colors.reset

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
                      'print string with color': colors.fg.yellow,
                      'platform': colors.fg.blue,
                      'ANSI escape sequences': colors.fg.red
                  }
    print highlight( s, **terms_color )
