# Create a reading list
Your task is to maximize diphone coverage in a list of 500 sentences. The coverage is 100% if all diphones appear in your reading list. You can use any method/algorithm you like to achieve this as long as you motivate your design choices. Your
main goal should be to have a better coverage than by simply choosing a random set of 500 sentences which yields a coverage of approximately 67%.

The basic outline of your algorithm will likely look something like:
1. Create a list of types that you want to cover (for example all diphones)
2. Find a sentence in the corpus which provides the largest number of different types in the wishlist.
3. Add it to the script
4. Remove the types from the wishlist
5. If the script is 500 sentences, stop. Otherwise go to step 2.

Most of the work will go into step two where you have to create some sort of a cost metric for comparing sentences from the corpus. Ideally your cost metric will also consider the length of the sentences.

## What to turn in
* Turn in your code as usual
* Turn in the reading list you generated by using the `tools.save_list()` method. See `example.py` for usage.
* A document explaining your design decisions:
    * What is the unit type you are trying to cover? (e.g. diphones)
    * How your algorithm works.
* clearly state the coverage your script achieves.


## Notes:
* Picking the longest sentences is likely to be a good strategy (since they will contain the highest number of phonemes) but do note that you will be reading the sentences. Take some time to carefully consider how you could maximize diphone coverage while minimizing sentence length.
* A base corpus of approximately 27K sentences is included under `./data` which you reading list will be sourced from.
* A list of diphones in IPA format is also found under `./data`.
* `example.py` contains examples of how to retrieve the corpus and diphones.
* Note: The diphone coverage of `list.tsv` is more than 1.0. This is because `list.tsv` contains possibly wrong phonetic predictions and therefore impossible diphones that don't appear in `dps.tsv`.
* Your reported coverage will be the one returned from `tools.coverage()`. See `example.py` for usage.
* The text is in Icelandic and this is the text you will be reading yourself in the upcoming assignments. Some of you are not native Icelandic speakers however. This doesn't mean however that you shouldn't do the assignments in Icelandic and we even think that these projects might provide very interesting results! If you prefer not to complete the assignments in Icelandic, please contact Atli on Teams.