from math import ceil

def main():

    f = open('submitInput.txt', 'r')
    fout = open('submitOutput.txt', 'w')
    num_cases = int(f.readline())
    case = 0

    for line in f:
        case += 1
        num_diners = int(line)

        if num_diners <= 0:
            num_tables = 0
        elif num_diners < 5:
            num_tables = 1
        else:
            num_tables = ceil((num_diners - 2) / 2)

        fout.write('Case #{}: {}\n'.format(case, num_tables))

    f.close()
    fout.close()


if __name__ == '__main__':
    main()