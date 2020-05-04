import itertools

def read_diphones(path: str = './data/dps.tsv'):
    '''
    Returns a list of diphones read from a tsv file
    Input arguments:
    * path (str='./data/dps.tsv'): A path to a tsv file containing
    diphones
    '''
    dps = []
    with open(path) as f:
        for line in f:
            dps.append(tuple(line.strip().split('\t')))
    return dps


def read_list(path: str = './data/list.tsv'):
    '''
    Returns a list of tuples where each tuple includes an sentence
    and the corresponding phonetic prediction

    Input arguments:
    * path (str='./data/list.tsv'): The path to a file with tab
    seperated text and phonetic labels.
    '''
    out = []
    with open(path) as f:
        for line in f:
            txt, *pron = line.strip().split('\t')
            out.append((txt, list(pron)))
    return out


def save_list(list_data: list, path: str = './data/my_list.tsv'):
    '''
    Saves a generated reading list to <path>

    Input arguments:
    * list_data (list): Your reading list data in the same format as
    returned from read_list()
    * path (str='./data/my_list.tsv'): Where the export will be stored

    For example:
    list_data[0] =
    ('Ég held að það sé ekki rétt orð, þetta komi ekkert almanakinu við.',
        ['~ j ɛː ɣ', 'h ɛ l t', 'aː ð', 'θ aː ð', 's j ɛː', 'ɛ h c ɪ',
        'r j ɛ h t', 'ɔ r ð', 'θ ɛ h t a', 'kʰ ɔː m ɪ', 'ɛ h c ɛ r̥ t',
        'a l m a n aː c ɪ n ʏ', 'v ɪː ð ~'])
    '''

    with open(path, 'w') as f:
        if list_data is not None:
            for item in list_data:
                pron = '\t'.join(item[1])
                f.write(f'{item[0]}\t{pron}\n')

def coverage(list_path: str = './data/list.tsv'):
    '''
    Measure the coverage of a reading list at <list_path>
    * list_path (str): A path to a file with sentence pronouncation
    tab-seperated values.
    '''
    all_dps = read_diphones()
    reading_list = read_list(list_path)
    rl_dps = set()
    for utt in reading_list:
        dps = prons_2_dps(utt[1])
        for dp in dps:
            rl_dps.add(dp)
    return len(rl_dps) / len(all_dps)

def prons_2_dps(prons: list):
    '''
    Transforms a list of lists where each list contains word
    pronounciations into a list of diphones
    Input arguments:
    * pron (list): A list of lists containing word pronounciations
    e.g. [('~', 'j', 'ɛː', 'ɣ'), ('h', 'ɛ', 'l', 't')] ->
    [('~', 'j'), (), ...]

    '''
    pron = list(itertools.chain.from_iterable([p.split(' ') for p in prons]))
    return pron_2_dps(pron)


def pron_2_dps(pron: list):
    '''
    Transform a string representing a pronounciation for a single
    word into diphone duples.
    e.g. ('~', 'j', 'ɛː', 'ɣ') -> [('~', 'j'), ('j', 'ɛː'), ('ɛː', 'ɣ')]
    '''
    return [(pron[i], pron[i+1]) for i in range(len(pron) - 1)]
