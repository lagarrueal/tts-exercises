# Step by step - Clustergen & Unit Selection
This is a step by step tutorial for running the Icelandic Clustergen recipe in Festival.

## Before you start
Make sure that you have followed the instructions in the docker tutorial. You should have a docker container
running before your proceed.

## Prepare the data
An example of a database extract is located [here](https://drive.google.com/open?id=1dY3hw23U03oG-obfTlbp0oQRcWJGzCS-). We will test out training on this very small corpus of about 130 recordings.
* Create a directory under `/usr/local/src` in the Docker container called `data/`.
* Copy `anon_example.zip` over to the `data` directory
* **Important**: Some students have had issues with using characters such as "_" in the `$VOX` parameter. Rename the `.zip` as `anonexample.zip` and change the `$VOX` parameter accordingly inside `build-example-voice.sh` (see below).
* If you haven't already downloaded the G2P sequitur model, cd into `data/` and run `wget https://eyra.ru.is/gogn/ipd_clean_slt2018.mdl`
* Create a new voice building directory under `/usr/local/src` called `example_clustergen`

## The recipe
The recipe you will be running is of the Clustergen variant and is located at `./help/build-example-voice.sh`
* Copy the file over to the `/usr/local/src/lvl_is_text` directory on your container
* Run `cmod +x build-example-voice.sh`
* Assuming that you haven't changed the name of `anon_example.zip` (`$VOX` is set to `example`) you don't have to change anything in the recipe.

## Train the model
* Point your shell to your voice building directory, i.e. `example_clustergen`.
* Run `../lvl_is_text/build-example-voice.sh`
* Wait for results.
* If everything went OK, you should have a waveform in the `example.wav` file in your voice building directory.

## Continuing
You can now test out synthesis on your sentences with just running this inside your voice building directory
```
echo 'halló halló halló' |
../festival/bin/text2wave \
  -eval festvox/lvl_is_${VOX}_cg.scm \
  -eval "(voice_lvl_is_${VOX}_cg)" \
  > my_example.wav
```

For a more robust synthesis strategy, take a look at the `Finishing and what to turn in` part of the Festival instructions w.r.t. `add_to_lexicon.sh` and `synth_file.sh`.

## Running the Unit Selection Recipe
You have prepared your data so there is very little you now need to do. Now we will be running the `./help/build-example-us-voice.sh`. You will have to move it to your image and do `chmod +x` again.
* Create a new voice building directory, e.g. `example_unitselection`
* Point your shell there
* run `../lvl_is_text/build-example-us-voice.sh`
* Wait for results.
* If everything went OK, you should have a waveform in the `example.wav` file in your voice building directory.


## Troubleshooting
You should always monitor the `build.err` file in your voice building directory. Take a look at the `build.err` file inside your voice building directory. At the top of the file it might contain something like

```
mv: cannot stat 'lab/is640Z_r000003001.sl': No such file or directory
awk: cannot open lab/is640Z_r000003001.slehmm (No such file or directory)
Cannot open file lab/is640Z_r000003001.lab as tokenstream
load_relation: can't open relation input file lab/is640Z_r000003001.lab
utt.load.relation: loading from "lab/is640Z_r000003001.lab" failed
/usr/local/src/festvox/src/general/smooth_f0: input file not accessible "lab/is640Z_r000003001.lab"
```

Something seems to be wrong with the file identified by `is640Z_r000003001`. The simples approach is to simply remove this file from the training set:
* create a new directory called `temp` inside the `data` directory
* Unzip your collection into the `temp` directory: `unzip example.zip -d temp/`
* `cd` into that directory
* Now the bad file had the identity `is640Z_r000003001`. To remove it from the training data you only have to remove the corresponding object from the `info.json` file. The corresponding object will have the key `3001`, the last part of the identity.
    * Simply locate that key inside `info.json`
    * Remove the corresponding object and save the `info.json`

Now create a new `zip` using this new dataset:
* From inside the `temp` directory run: `zip -r ../example2.zip *`
* A new `example2.zip` file should now appear in the `data` directory

Now we try building the voice again.
* Remember to change the `VOX` parameter insider `build-example-voice.sh` to `example2`
* Delete the old voice building directory
* Create it again
* point your shell into it
* Run `../lvl_is_text/build-example-voice.sh`