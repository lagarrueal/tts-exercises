# Digital Audio

## Playing with the sample rate
1. Load a sample from the `./data` directory and half the number of samples by removing every second sample. Keep the same sample rate and save the waveform. Describe the results. Why does this happen?
2. Now do the same but half the sample rate. Describe the results. Why does this happen?
3. Next repeat step two but remove ever more samples while reducing the sample rate at an equal rate. Compare the output for sr, sr/2, sr/4, sr/8, sr/16. sr/32. At what point does the audio get too distorted in your opinion? At what point could you no longer understand what is being said. Calculate what the actual sample rate is at these points and compare to what is used in telephone audio (8000 kHz)

## Mixing the samples
1. Load two samples of your choice from `./data`. Mix them by interleaving the samples from each (e.g. |a1|b1|a2|b2|a3|...). Note: The samples in `./data` are all of different lengths so cut the samples like shown in `./example.py`
2. Plot the results
3. Save the waveform and describe what you hear.
4. What is needed to do get the audio to sound more normal? Compare this result by mixing the voices by adding up the samples at every step. Naively reduce the relative amplitude of both samples by a factor of two. Do you hear a difference? Why/Why not?

## Fade a voice
1. Load a sample from `./data`
2. Scale each sample such that the first sample has a scaling factor of 0 and the last has a scaling factor of 1 where the scales increase linearly from start to finish. You can use `np.linspace(0, 1, n)` to create `n` values that increase linearly in the range (0, 1).
3. Plot the waveform.
4. Save the audio, listen to the output and describe the results.

## Combine
Create something! You can do whatever you like here using the methods we have uncovered already. If you have no idea what to do, do this:
1. Load `f1.wav` and `m2.wav`
2. Segment each recording into 1 second segments
3. Interleave the segments
4. Apply linear scale fading at the joints between every segment such that the relative amplitude is 0 at the joint and increases to maximum scaling after half a second.
5. Plot the results.
6. Save the audio file
