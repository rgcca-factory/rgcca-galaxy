import sys


def __main__():
    try:
        infile = open(sys.argv[1], 'r')
        outfile = open(sys.argv[2], 'w')
    except Exception:
        sys.exit('Cannot open or create a file\n')

    if len(sys.argv) < 4:
        sys.exit('No columns to merge\n')
    else:
        cols = sys.argv[3:]

    skipped_lines = 0

    for line in infile:
        line = line.rstrip('\r\n')
        if line and not line.startswith('#'):
            fields = line.split('\t')
            line += '\t'
            for col in cols:
                try:
                    line += fields[int(col) - 1]
                except Exception:
                    skipped_lines += 1

            print(line, file=outfile)

    if skipped_lines > 0:
        print('Skipped %d invalid lines' % skipped_lines)


if __name__ == "__main__":
    __main__()
