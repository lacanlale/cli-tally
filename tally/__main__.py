import tally.__init__ as m


def main():
    count, fn = m.get_counts()
    m.disp(count, fn)


if __name__ == '__main__':
    main()