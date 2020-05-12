# Step by step - Icelandic Recipe in Ossian
This is a step by step tutorial for training a very small corpus in Ossian using the Icelandic recipe.

This tutorial assumes that you have a AWS VM up and running and you have Ossian installed.

# Gathering the Data
A very small Icelandic corpus is available at `./help/anon_medium_16k.zip`. It's contents after being unzipped are e.g.

```
anon_medium_16k/
    wav/
        id1.wav
        ...
    txt/
        id1.txt
        ...
```
Do the following:
* Copy the `.zip` file over to your Ossian VM.
* Unzip it and place the content inside the corpus directory such that you get the following structure:
    ```
    $OSSIAN/
        corpus/
            is/
                labelled_corpora/
                    lexicon.txt
                    lts.model
                speakers/
                    anon_medium_16k/
                        wav/
                            id1.wav
                            ...
                        txt/
                            id1.txt
                            ...
    ```
Your corpus is now ready. Remember that you have to copy the `lexicon.txt` and `lts.model` over to the corpus directory yourself.

# Prepare the recipe and model
Make sure that you have followed the steps in the assignment README. It is very important that you are:
* Using the most up to date `Lexicon.py` file. You should completely replace the one in the VM with this new one
* Using the most up to date `is_nn.cfg` file as an earlier one contained the wrong sample rate configuration.
    * You should verify that the file uses the sample rate 16000 rather than 44100.
    * Open the `is_nn.cfg` file and `ctrl+f` for 44100. If no matches then you are good. Otherwise, replace those values with 16000

# Running
At `./help/train.sh` is a training script that will perform all the steps mentioned in the assignment README. Copy this script over to the VM's `$OSSIAN` directory and do `chmod +x train.sh`
* Run it using `./train.sh`
* If you run into exceptions:
    1. Make sure that you delete both `$OSSIAN/train/is/speakers/anon_medium_16k/` and `$OSSIAN/voices/is/anon_medium_16k/` before trying again
    2. Run each step of `train.sh` seperately to identify which step is failing.
    3. Refer to the help channel on Teams or contact me directly.


