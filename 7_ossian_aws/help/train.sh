#! /bin/bash

language=is
voice=anon_medium_16k
recipe_name=is_nn

# Prepare the acoustic and duration models using Ossian:
python ./scripts/train.py -s $voice -l $language $recipe_name
# Train the duration model on CPU:
export THEANO_FLAGS=""; python ./tools/merlin/src/run_merlin.py train/$language/speakers/$voice/$recipe_name/processors/duration_predictor/config.cfg
# Train the acoustic model on CPU:
export THEANO_FLAGS=""; python ./tools/merlin/src/run_merlin.py train/$language/speakers/$voice/$recipe_name/processors/acoustic_predictor/config.cfg
# Convert the models
python ./scripts/util/store_merlin_model.py train/$language/speakers/$voice/$recipe_name/processors/duration_predictor/config.cfg voices/$language/$voice/$recipe_name/processors/duration_predictor
python ./scripts/util/store_merlin_model.py train/$language/speakers/$voice/$recipe_name/processors/acoustic_predictor/config.cfg voices/$language/$voice/$recipe_name/processors/acoustic_predictor
# Test out synthesis:
python ./scripts/speak.py -l $language -s $voice -o ./test/wav/my_test.wav $recipe_name ./test/txt/ice.txt