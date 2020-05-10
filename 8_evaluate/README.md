# Evaluate your TTS
It is time to evaluate your TTS systems. We will use the very popular MOS (Mean Opinion Score) metric for this task. In a MOS test a participant:
* Listens to multiple synthesized waveforms
* The participant rates each on a scale from 1 to 5, 1 being "completely unnatural" and 5 being "completely natural"

It is hard to judge exactly what participants are rating in MOS but there is evidence that the participants often base their score on how much they like the system, rather than how much they actually understand of what was being said. We will add two modifications to the MOS metric to get additional information:
1. We will ask the participants to write down what words they heard.
2. We will sprinkle in some ground truth waveforms (i.e. some recordings from your training data) to attempt to ground the ratings.

## Google Drive and Google Forms
We will be using Google Forms to carry out this task. An example MOS survey is available [here](https://docs.google.com/forms/d/1KsEq-Ckt_z1oHAnlWWl_h07NhkqJCUMRHZkZPGPVKlM/edit?usp=sharing). To the best of my knowledge, there is no direct way to embed audio in google form. I just added the waveforms to a public Google Drive folder and add links to each waveform in each question. You can do the same. You can use this Google form as a template for your survey.

## Technical details
In your form you should survey:
* 10 synthesized samples from your Festival TTS (you can choose to either use your unit selection voice or your clustergen voice)
* 10 synthesized samples from your Ossian TTS
* 5 ground truth samples
Randomize the order of these so not do add unwanted bias. Make sure that the text being read is different in each sample, otherwise we could also add unwanted bias.

You should ask 5 individuals to complete your MOS survey. To get additional data you will also survey one participant from another student's pool of participants. Contact another student in the course via Teams.
* You will survey one of their participants
* They will survey one of your participants
* It is your shared responsibility that your participants receive a link to the survey and finish the survey.

## What to Turn In
You should report on the results.
1. For each group (Festival, Ossian, Ground truth) do the following:
    * What is the average MOS score for each sample and across all samples in the group.
    * Create a bar chart with a bar for each rating value (1-5) and set the height as the corresponding number of responses for the given value.
    * Create a plot with sample index on the x-axis and MOS score on the y-axis where you plot the graph of each participant's MOS response to each question (on the same graph).
    * The ratio of samples that were completely understood (the words are the same in the input and the survey)
2. The shared participant will have 2 sets of ratings. Compare the ratings the participant gave your Ossian and Festival systems and the ratings given to the other student's systems. You should compare the average rating and standard deviation across all ratings given for each system.