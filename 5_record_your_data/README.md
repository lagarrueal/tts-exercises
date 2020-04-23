# Record your data
You will now start recording the sentences you have selected in assignment 4. We will be using our own recording client, `LOBE` to carry out the recording sessions.

## Setting up your own recording studio
There is a good [document on speech.zone](http://www.speech.zone/exercises/build-a-unit-selection-voice/make-the-recordings/) about carrying out your own recording sessions. Most importantly:
* Try to use a headphone microphone if you have access to one (or a proper microphone if you have one)
* Manage your levels. Before starting a recording session, open up audacity and record a sample sentence. You can then play back the recording and audacity will show the playback level in the tool bar. We want to try to keep this value as stable as possible across sessions. Try to aim for a value between -18 and -9 dB.
    * You can change the input volume of your microphone through your operating system. We want the input volume to be high (hot) but never "hit the red" which would result in clipping. Changing the input volume such that recording your natural voice results in levels bouncing between -18 and -9 should suffice.
* Try to speak as uniformly as possible across all sentences and avoid animated speech.
* Ensure chair, microphone, etc. are positioned the same way in every session.
* When you are speaking, ensure that you are not fidgeting, playing with any of the cables, your hair, etc.

## Recording
* TODO: add information about LOBE
* In our experiments, each 50 sentence session takes about 10 minutes to finish. This means that you could finish recording your list of 500 sentences in two 50 minute sessions. We recommend you do this across two days to avoid any strain.
* When you have finished your reading list you can export the dataset from LOBE.

## What to turn in
* A short document that includes:
    * Details about your recording environment, such as choice of microphone, how you maintained the same position relative to mic across sessions etc. A photo of your recording environment is also beneficial.
    * A list of the recording sessions and the duration of them (TODO: add information about how to do this in LOBE)
    * We will monitor your progress on LOBE and you don't need to send us your datasets.
    * The dataset export includes a detailed information file, `info.json`. Each item in that file has a `text_info` and a `recording_info` dictionary.
        * Using `item['text_info']['text]` as well as `item['recording_info']['duration']` calculate the average string length of your text data and the average recording duration. Plot a scatter plot for each recording item where string length is on the x-axis and recording duration is on the y-axis.



