from math import ceil

def main():

    f = open('submitInput1.txt', 'r')
    fout = open('submitOutput1.txt', 'w')
    num_cases = int(f.readline())
    case = 1

    for line in f:

        num_diners = int(line)

        if num_diners <= 0:
            num_tables = 0
        elif num_diners < 3:
            num_tables = 1
        else:
            num_tables = ceil((num_diners - 2) / 2)

        fout.write('Case #{}: {}\n'.format(case, num_tables))
        case += 1

    f.close()
    fout.close()


if __name__ == '__main__':
    main()