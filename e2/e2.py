import operator

def main():

    corpus_file = open('corpus.txt', 'r')
    corpus = corpus_file.readline().split()
    corpus_file.close()

    input_file = open('submitInput.txt', 'r')
    output_file = open('submitOutput.txt', 'w')
    num_cases = int(input_file.readline())
    case = 0

    for line in input_file:
        case += 1
        boundaries = line.split()
        first_word = int(boundaries[0])
        last_word = int(boundaries[1])
        words = {}

        for i in range(first_word - 1, last_word):
            if corpus[i] in words:
                words[corpus[i]] += 1
            else:
                words[corpus[i]] = 1

        sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
        output_file.write('Case #{}: {} {},{} {},{} {}\n'.format(case,
                                                                 sorted_words[0][0], sorted_words[0][1],
                                                                 sorted_words[1][0], sorted_words[1][1],
                                                                 sorted_words[2][0], sorted_words[2][1]))

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()