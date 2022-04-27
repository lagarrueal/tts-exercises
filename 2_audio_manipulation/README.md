# Audio manipulation

## 1. Multiple components
We start off where we ended in the last assignment. We now know how to generate sine waves and play them back as audio. Speech however is much more complicated than pure tone sine waves. Each period of speech consists of multiple frequency components with different relative amplitudes. I.e. each speech instance could be given as `c_1*f_1 + c_2*f_2 + ... + c_n*f_n` where the `c_i` are scalar values that determine the relative amplitude of each frequency component `f_i`.
1. (*)
    * Create a function multi_sine(C, F, sr, duration) that generates a weighted sum of frequency components as explained above. C should be a list of the scalar values as explained above and F is a list of frequencies.
    * Create 4 frequency components, all sampled at `16,000 Hz` for 5 seconds. These components should have the frequencies `500`, `1000`, `2000`, `5000` Hz. The relative amplitude scalar values should be `1`, `0.5`, `0.1`, `0.05`. Save the audio and play it back. This combination should sound distinctly different from any of the singular pure tone sine waves it consists of.
2. (*) Using the [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform) we can determine the frequency domain from the waveform (which is in time domain). The result of the transformation is called the `magnitude spectrum` of the signal. The density is split evenly between a positive and a negative component as explained [here](https://en.wikipedia.org/wiki/Euler%27s_formula#Relationship_to_trigonometry).
    * Create the same weighted sum as in 1.1 and use `tools.plot_spectrum()` to show the spectrum. Describe what you see. Can you identify which values in the frequency domain belong to which component in time domain?
3. (*) A spectrogram shows how the spectrum changes over time. Speech is not only a single combination of frequency components over the whole duration of speech, rather this combination of frequencies changes depending on prosody and the phonetic contents of what is being said. Human perception of `loudness` does not scale linearly to pitch. Therefore different perceptual scales have been used in speech processing to account for this. One such is the [Mel scale](https://en.wikipedia.org/wiki/Mel_scale).
    * Use the `tools.plot_spectrogram()` function to plot the Mel-scale spectrogram for the combination you created earlier.
    * plot the Mel-scale spectrogram for `./data/f1.wav`.
    * Given the information above, can you explain why they are so different?


## 2. Adjusting sample rate
Lets see what happens when we manipulate the sample rate.
1. (*) Create a function `half_sr(wave)` that, given a waveform, halfs the number of samples by removing every second sample from the waveform.
    * Load a sample from the `./data` directory and half the number of sample using your function.
    * Save the waveform and keep the same sample rate. Describe the results. Why does this happen?
2. (*) Now do the same but half the sample rate as well when you save the waveform. Describe the results. Why does this happen?
3. (*) Next repeat step two but remove ever more samples while reducing the sample rate at an equal rate. Compare the output for sr, sr/2, sr/4, sr/8, sr/16. sr/32. At what point does the audio get too distorted in your opinion? At what point could you no longer understand what is being said. Calculate what the actual sample rate is at these points and compare to what is used in telephone audio (8000 Hz).


## 3. Mixing waveforms
1. (*) Create a function `zip_waves(a, b)` that takes in two waveforms and zips them together (e.g. |a1|b1|a2|b2|a3|...)
    * Load two samples of your choice from `./data`. Mix them by using your zip function. Note: The samples in `./data` are all of different lengths so cut the samples like shown in `./example.py`
    * Plot the results
    * Save the waveform and describe what you hear.
2. (*) What is needed to do get the audio to sound more normal?
    * Produce a normal sounding mixed waveform by changing the sample rate.
    * Compare this result by mixing the waveforms like you do in your `multi_sine` function.
        * Create a function `mix_waves(a, b, c_a, c_b)` where `a` and `b` are waveforms and `c_a` and `c_b` are the relative amplitude scalars for each. Each sample from combining waveforms samples `a_i` and `b_i` in this way should be `c_a*a_i + c_b*b_i`. Choose whatever `c` values you like the most!
    * Do you hear a difference between these two results? Why / Why not?
3. (*) Create a function `fade(wave, start_val, stop_val)` that fades a waveform such that the first sample has a scaling factor of `start_val` and the last has a scaling factor of `stop_val` where the scales increase linearly from start to finish (use `np.linspace()` for this).
    * Apply this type of fade on any sample from `./data` with `start_val=0` and `stop_val=1`.
    * Plot the resulting waveform
    * Listen to the output
    * Describe the results.


## 4. Combine
1. (*) Create something! You can do whatever you like here using the methods we have uncovered already and methods used in `example.py`. Explain what you decided to do. If you have no idea what to do, do this:
1. Load `f1.wav` and `m2.wav`
2. Segment each recording into 1 second segments
3. zip the segments
4. Apply linear fading to each segment such as the first increases in scale and the next one decreases in scale and so on.
5. Plot the results.
6. Save the audio file
