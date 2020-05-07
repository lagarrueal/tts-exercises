# Festival

## 1. About Festival
*The following is built on the [official Festival documentation](http://www.festvox.org/)*

Festival is a general multi-lingual speech synthesis system. The system is written in C++ and uses the Edinburgh Speech Tools Library for low level architecture and has a Scheme (SIOD) based command interpreter for control.

We will now quickly cover the three basic parts of TTS in Festival:
### 1-2. Text & Linguistic Analysis
*From raw text to identified words and basic utterances. Then finding pronunciations of the words and assigning prosodic structure to them: phrasing, intonation and durations.*

Text analysis is the task of identifying the *words* in the text. By *words*, we mean tokens for which there is a well defined method of finding their pronunciation, i.e. from a lexicon, or using letter-to-sound rules.

The first task in text analysis is to make chunks out of the input text (tokenizing it). In Festival, at this stage,

we also chunk the text into more reasonably sized *utterances*. An utterance structure is used to hold the information for what might most simply be described as a sentence. Separating a text into utterances is important, as it allows synthesis to work bit by bit, allowing the waveform of the first utterance to be available more quickly than if the whole files was processed as one.

Apart from chunking, text analysis also does *text normalization*. There are many tokens which appear in text that do not have a direct relationship to their pronunciation. Numbers are perhaps the most obvious example. Consider the following sentence

"*On May 5 1996, the university bought 1996 computers.*"

In English, tokens consisting of solely digits have a number of different forms of pronunciation.
* The "*5*" above is pronounced "*fifth*", an ordinal, because it is the day in a month
* The first "*1996*" is pronounced as "*nineteen ninety six*" because it is a year
* the second "*1996*" is pronounced as "*one thousand nine hundred and ninety six*" (British English) as it is a quantity.

Two problems that turn up here: non-trivial relationship of tokens to words, and homographs, where the same token may have alternate pronunciations in different contexts. In Festival, homograph disambiguation is considered as part of text analysis. In addition to numbers, there are many other symbols which have internal structure that require special processing; such as money, times, addresses, etc. All of these can be dealt with in Festival by what is termed *token-to-word rules*. These are of course language specific.

#### Lexicons
After we have a set of words to be spoken, we have to decide what the sounds should be; what phonemes, or basic speech sounds, are spoken. Each language and dialect has a phoneme set associated with it. Given a set of units we can train models from them, but it is up to linguistics to help us find good levels of structure and the units at each.

#### Prosody
Prosody, or the way things are spoken, is an extremely important part of the speech message. Changing the placement of emphasis in a sentence can change the meaning of a word, and this emphasis might be revealed as a change in pitch, volume, voice quality, or timing.

We'll present two approaches to taming the prosodic beast:
* limiting the domain to be spoken
* intonation modeling.

By limiting the domain, we can collect enough data to cover the whole output. For some things, like weather or stock quotes, very high quality can be produced, since these are rather contained.

For general synthesis, however, we need to be able to turn any text, or perhaps concept, into a spoken form, and we can never collect all the sentences anyone could ever say. To handle this, we break the prosody into a set of features, which we predict using statistically trained models:
* phrasing
* duration
* intonation
* energy
* voice quality

### 3. Waveform Generation
*From a fully specified form (pronunciation and prosody) generate a waveform.*

For the case of concatenative synthesis, we actually collect recordings of voice talent, and this captures the voice quality to some degree. This way, we avoid detailed physical simulation of the oral tract, and perform synthesis by integrating pieces that we have in our inventory; as we don't have to produce the precisely controlled articulatory motion, we can model the speech using the units available in the sound alone

During waveform generation, the system assembles the units into an audio file or stream, and that can be finally "*spoken*". There can be some distortion as these units are joined together, but the results can also be quite good.

We systematically collect the units, in all variations, so as to be able to reproduce them later as needed. To do this, we design a set of utterances that contain all of the variation that produces meaningful or apparent contrast in the language, and record it (You did a naive version of this in assignment 4).



## 2. About the Recipe
The recipe you will run uses the  [Clustergen training method](https://www.cs.cmu.edu/~awb/papers/is2006/IS061394.PDF) that is included in Festival. Clustergen is a *statistical parametric synthesis* (SPS) system. SPS systems do not select units  from a database like unit selection systems but generate the waveform directly by training statistical parametric models.

### About Clustergen
1. **Label the database**:

    The first stage, which is not technically part of the clustergen synthesizer is to label the database using an HMM labeler. Clustergen uses EHMM which is included within the latest FestVox release. It uses Baum Welch from a flat start to train context independent HMM models, which it then uses to force align the phonemes generated from the transcriptions with the audio.

    Clustergen uses 3-state models, that generate HMM state sized labels, three per phone.

2. **Extract features**:
    F0 is extracted using the Edinburgh Speech Tools `pda` program. Using the generated phoneme labels, the F0 is interpolated through unvoiced regions, thus there is a non-zero F0 value for all 5ms frames that contain voiced or unvoiced speech.

    24 MFCCs are combined with the F0 to give a 25 feature vector every 5ms. For each of these vectors high level features are extracted, including phone context (with phonetic features), syllable structure, word position, etc.

3. **Training feature predictors**:
    Clustering is done by the Edinburgh Speech Tools CART tree builder `wagon`. CART trees are built with `wagon` to find questions that split the data to minimize impurity. A tree is built for all the vectors labeled with the same HMM state name.

    Separate F0 and MFCC models are built. No delta features are used in clustergen.

    An additional CART tree is built to predict durations for each HMM state. Each state duration is predicted independently.

4. **Synthesis**:
    At synthesis time the phone string is generated from the text as is done in other synthesis techniques within Festival, then an HMM
    state name relation is build linking each phone to its three subphonetic parts.

    The duration CART tree is used to predict the length of each HMM state. A set of empty vectors is created to fill the length of the predicted state duration. Using the CART tree specific to the state name, the questions are asked and the means from the vector at the selected leaf are added as values to each vector.

    After prediction smoothing is done by a simple 3-point moving average to each track of coefficients.

    Then the speech is reconstructed from the predicted parameters using the MLSA filter. Voicing decisions are currently done by phonetic type directly from the labels, rather than trained from the acoustics.



### Technical overview of the `build-voice.sh` script
All the steps to train the model are performed inside `/usr/local/src/lvl_is_txt/build-voice.sh` in the Docker image. The main steps in the voice building script are:

1. Setup the Festvox Clustergen build:

        $FESTVOXDIR/src/clustergen/setup_cg lvl is $VOX

    * `$FESTVOXDIR` is an environment variable that points to `/usr/local/src/festvox/`
    * `$VOX` is the identify of the voice. This could for example be `atli`. The demo recipe supports `$VOX=f1` or `$VOX=m1` where `f1` is a female voice and `m1` is a male voice.

2. The script will download the voice data that you have selected (f1 or m1):

        wget https://eyra.ru.is/gogn/${VOX}-small.zip

3. We then convert the voice data to the right format, 16 bit single channel at 16 kHz:

        for i in audio/*/*.wav
        do
            sox "$i" -r 16000 -c 1 -b 16 "wav/$(basename -s .wav "$i").wav" 1\
            > sox.log 2> sox.err
        done

4. Configure the clustergen voice:

        sed -i 's/^(set! framerate .*$/(set! framerate 16000)/' festvox/clustergen.scm

5. Normalize the prompts for the recordings using `lvl_text/normalize.py` which can read in the `info.json` file that is exported from sLOBE:

        python3 ../lvl_is_text/normalize.py info.json "-" --lobe | grep -o "[^ ]*" | sort | uniq > vocabulary.txt

    Most importantly, the normalizer will:
    * lower case all text
    * remove punctuations and other symbols such as "!", ";" and ":".
    * Replace certain symbols with a `_pause` token to denote a pause in speech. Specifically we only replace "," with a pause.

    **You can change this normalization script if you like but make sure to document your changes.**


6. Since this naive recipe does not have a very advanced normalizer for Icelandic we have to remove some sentences (specifically that contain numbers or the character "c" which appear in some of the prompts on sLOBE). You might need to edit this rule if you run into issues:

        grep -v '"[^"]*[0-9c]' txt.complete.data > txt.nonum.data

7. Select sentences to train on. This could either be the full set of prompts:

        cp -p txt.nonum.data etc/txt.done.data

    or a subset, below we use `head -n1000` to select the first 1000 prompts from `txt.nonum.data`:

        head -n1000 txt.nonum.data > etc/txt.done.data

8. Next we create the Festival lexicon. It is an specific scheme format and must contain pronounciations for all words that appear in the training data:
    1. First copy all words from the training data

            python3 ../lvl_is_text/normalize.py info.json "-" --lobe | grep -o "[^ ]*" | sort | uniq > vocabulary.txt

    2. Copy the lexicon from `lvl_is_text/`:

            cp ../lvl_is_text/framburdarordabok.txt lexicon.txt

    3. Apply a pretrained Sequitur G2P model to words in training data

            wget https://eyra.ru.is/gogn/ipd_clean_slt2018.mdl
            g2p.py --model ipd_clean_slt2018.mdl --apply vocabulary.txt --encoding utf-8 > lexicon-prompts.txt

    4. Create a combined lexicon

            python3 ../lvl_is_text/build_lexicon.py ../lvl_is_text/aipa-map.tsv lexicon.txt lexicon.scm
            python3 ../lvl_is_text/build_lexicon.py ../lvl_is_text/aipa-map.tsv lexicon-prompts.txt lexicon-prompts.scm
            echo "MNCL" > festvox/lexicon.scm
            cat lexicon.scm lexicon-prompts.scm | fgrep "(" | sort | uniq >> festvox/lexicon.scm

    5. Apply the phonology script which reads a phonology description and writes/updates several files in a Festvox Clustergen build tree, including the phonset definition and various feature and feature description files:

            ../lvl_is_text/apply_phonology.py ../lvl_is_text/phonology.json .

5. Run the Clustergen build:

        time bin/build_cg_voice 1>build.out 2>build.err

6. After training, synthesize one sample and save it to `./example.wav`

        echo 'halló _pause ég kann að tala íslensku alveg hnökralaust' |
        ../festival/bin/text2wave \
        -eval festvox/lvl_is_${VOX}_cg.scm \
        -eval "(voice_lvl_is_${VOX}_cg)" \
        > example.wav

    TODO: this assumes that no preprocessing is applied to the input (which won't be the case in the end).

## If you have reached this point, congratulations! You have caught up with us. We are currently doing the finishing touches on the image and it will soon be ready. You can run the following but do note that you will have to re-clone the image when it is ready.

## Using the Festival recipe
We will start by testing the recipe on pre-recorded data.

1. Under `/usr/local/src/`, create a new directory: `mdkir demo_voice`.
2. Direct your shell to the new directory: `cd demo_voice`
3. Do e.g. `export VOICE=f` if you want to train on the female voice data.
4. Run the `build-voice.sh` script via `../lvl_is_text/build-voice.sh`

The script will now perform all of the steps that were mentioned above and this could take some time to finish.
