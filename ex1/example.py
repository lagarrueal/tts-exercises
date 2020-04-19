from tools import read_list, save_list, read_diphones, coverage

def test():
    # Read the list
    data = read_list()
    print(f'1. The number of sentences: {len(data)}\n')

    # Get the first sentence and it's pronounciation:
    first_txt, first_pron = data[0]
    first_txt = first_txt.split(' ')

    print('2. The first sentence and pronounciation\n')
    for i, txt in enumerate(first_txt):
        print(f'\t {txt} - {first_pron[i]}')

    # order the data by the length of sentences
    data.sort(key = lambda s: len(s[0]))
    print(f'3. The shortest sentence is: {data[0][0]}\n')

    # order the data by the length of sentences in
    # descending order
    data.sort(key = lambda s: -len(s[0]))
    print(f'4. The longest sentence is: {data[0][0]}\n')

    # Read the diphones
    diphones = read_diphones()
    print(f'5. The first diphone contains the following phonemes: {" ".join(diphones[0])}\n')

    # Create a new reading list using only the first 500 sentences
    data_500 = data[:500]
    save_list(data_500)

    # measure the coverage of the new list
    print(f'The new list contains {coverage("./data/my_list.tsv")} of all diphones')


if __name__ == '__main__':
    test()






