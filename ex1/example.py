from tools import read_list, save_list, read_diphones

def test():
    # Read the list
    data = read_list()
    print(f'1. The number of sentences: {len(data)}')

    # Get the first sentence and it's pronounciation:
    first_txt, first_pron = data[0]
    first_txt = first_txt.split(' ')

    print('2. The first sentence and pronounciation')
    for i, txt in enumerate(first_txt):
        print(f'\t {txt} - {first_pron[i]}')

    # order the data by the length of sentences
    data.sort(key = lambda s: len(s[0]))
    print(f'3. The shortest sentence is: {data[0][0]}')

    # order the data by the length of sentences in
    # descending order
    data.sort(key = lambda s: -len(s[0]))
    print(f'4. The longest sentence is: {data[0][0]}')

    # Read the diphones
    diphones = read_diphones()
    print(f'5. The first diphone contains the following phonemes: {" ".join(diphones[0])}')


if __name__ == '__main__':
    test()






