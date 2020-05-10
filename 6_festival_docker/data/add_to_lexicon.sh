#! /bin/bash

# Create nthe new vocabulary and new prompts
python3 ../lvl_is_text/normalize.py tests.txt "-" | grep -o "[^ ]*" | sort | uniq > new-vocab.txt
g2p.py --model ipd_clean_slt2018.mdl --apply new-vocab.txt --encoding utf-8 > new-lexicon-prompts.txt

# Join them to the base
cat lexicon-prompts.txt new-lexicon-prompts.txt | sort | uniq > lexicon-prompts.txt

python3 ../lvl_is_text/build_lexicon.py ../lvl_is_text/aipa-map.tsv lexicon-prompts.txt lexicon-prompts.scm

echo "MNCL" > festvox/lexicon.scm
cat lexicon.scm lexicon-prompts.scm | fgrep "(" | sort | uniq >> festvox/lexicon.scm