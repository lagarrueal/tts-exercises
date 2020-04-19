
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
            dps.append(line.strip().split('\t'))
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


def save_list(txts: list, prons: list, path: str = './data/my_list.tsv'):
    '''
    Saves a generated reading list to <path>

    Input arguments:
    * txts (list): A list of strings containing the sentences to be read
    * prons (list): A list of tuples where each element of the tuple corresponds
    with the phonetic label for a word in the sentence
    * path (str='./data/my_list.tsv'): Where the export will be stored

    For example:
    * txts[0] = 'Ég held að það sé ekki rétt orð, þetta komi ekkert almanakinu við.'
    * prons[0] = ['~ j ɛː ɣ', 'h ɛ l t', 'aː ð', 'θ aː ð', 's j ɛː', 'ɛ h c ɪ',
        'r j ɛ h t', 'ɔ r ð', 'θ ɛ h t a', 'kʰ ɔː m ɪ', 'ɛ h c ɛ r̥ t',
        'a l m a n aː c ɪ n ʏ', 'v ɪː ð ~']
    '''

    with open(path, 'w') as f:
        for i, txt in enumerate(txts):
            pron = '\t'.join(prons[i])
            f.write(f'{txt}\t{pron}\n')

def coverage(list_path:str):
    '''
    Measure the coverage of a reading list at <list_path>
    TODO
    '''
    reading_list = read_list(list_path)
