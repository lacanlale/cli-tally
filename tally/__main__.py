from colorama import init
from colorama import Fore, Back, Style
import tally.__init__ as __init__


def main():
    ##### Required for colorama
    init()

    ##### Get counts and run main display
    count, fn = __init__.get_counts()
    __init__.disp(count, fn)


if __name__ == '__main__':
    main()