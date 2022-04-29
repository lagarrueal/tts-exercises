from tools import read_list, save_list, read_diphones, coverage, prons_2_dps
# create the wishlist with all the diphones in dps.tsv using read_diphones('./data/dps.tsv')
# create the reading list with all the sentences and their pronounciation using read_list('./data/list.tsv')
# order the reading list from longest sentences to shortest sentences using sort(key = lambda s: -len(s[0]))
# for each sentence/pronunciation in the reading list, convert the pronounciation to diphones using prons_2_dps(pron)
# for each diphone of the previous pronunciations, check if it is in the wishlist using diphone in wishlist
# if it is in the wishlist, we delete these diphones from the wishlist
# and we add the associated sentence to the final list using save_list(final_list, './data/final_list.tsv')
#   each line of the final list is in the following format:
#       `<sentence>\t<source>\t<score>\t<pron>` where:
#    * `<sentence>` is the sentence being read
#    * `<source>`is my RU is : alexandrel21
#    * `<score>` a score that dictates in what order your sentences will be prompted. A higher score should mean that the sentence appears earlier. So for 500      
#       sentences you could score them with e.g. `500`, then `499` etc.
#    * `<pron>` The pronounciation prediction in the same format as used in `./data/list.tsv`
# if the diphone is not in the wishlist, it means that the diphones are already covered by the final list
# so we repeat the process with the next sentence in the reading list
# we repeat the process until the final list contains 500 sentences
# measure the coverage of the final list using coverage('./data/final_list.tsv')

# create a function that takes the reading list and the wish list as input
# return the sentence that contains the most diphones in the wish list
# return the diphones contained in the sentence that contains the most diphones in the wish list
def max_number_of_diphones(wish_list, reading_list):
    max_number = 0
    max_sentence = ''
    for sentence, pron in reading_list:
        pron = prons_2_dps(pron)
        number = 0
        for diphone in pron:
            if diphone in wish_list:
                number += 1
        if number > max_number:
            max_number = number
            max_sentence = sentence
    return max_sentence, prons_2_dps(max_sentence[1])


def main():
    wish_list = read_diphones('./data/dps.tsv')
    reading_list = read_list('./data/list.tsv')
    final_list = []
    # order the reading list from longest sentences to shortest sentences using sort(key = lambda s: -len(s[0]))
    reading_list.sort(key = lambda s: -len(s[0]))
    while len(final_list) < 500:
        sentence, diphones = max_number_of_diphones(wish_list, reading_list)
        reading_list.remove(sentence)
        wish_list.remove(diphones)
        final_list.append(sentence)
        
    save_list(final_list, './data/final_list.tsv')
    print(coverage('./data/final_list.tsv'))
    print(len(final_list))


if __name__ == '__main__':
    main()