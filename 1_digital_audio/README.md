

# Digital Audio
## 1. Samples and time
Digital audio is stored as a sequence of `samples`. Each sample is just a numeric value with a certain precision. The `sample rate` (sr) is the number of samples the audio signal contains per second. Generally speaking, when sample rate increases, the quality of the audio increases.

1. Define a function that takes in a sample index and sample rate and returns the time value in seconds that correspond to the index.
    * A signal has sample rate = 1. The 0th sample is sampled after 0 seconds, Sample of `i=1` is sampled after 1 second.
    * A signal has sample rate = 200. Sample at `i=5` is sampled after 0.025 seconds.

2. Create another function that achieves the same but for an 1-D array of sample indices (e.g. [0, 500, 1000, ...]). You can use your sample_to_time function as long as the output is a numpy array.
    * Calling `samples_to_time(np.arange(0, 22050, 512), 22050)` should produce the following results:
        ```
        [0.         0.02321995 0.04643991 0.06965986 0.09287982 0.11609977
        0.13931973 0.16253968 0.18575964 0.20897959 0.23219955 0.2554195
        0.27863946 0.30185941 0.32507937 0.34829932 0.37151927 0.39473923
        0.41795918 0.44117914 0.46439909 0.48761905 0.510839   0.53405896
        0.55727891 0.58049887 0.60371882 0.62693878 0.65015873 0.67337868
        0.69659864 0.71981859 0.74303855 0.7662585  0.78947846 0.81269841
        0.83591837 0.85913832 0.88235828 0.90557823 0.92879819 0.95201814
        0.9752381  0.99845805]
        ```

3. Create a function `gen_time(duration, sr)` that creates time stamps in seconds for the given duration at the given sample rate. For e.g. `gen_time(1, 10)` the output should be
    ```
    array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,
        0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])
    ```

## 2. Creating waves
The frequency of a sine wave can be understood as the number of cycles the sine wave achieves in a second.

1. (*) How many Radians does it take the sine wave to complete a single cycle?

2. Create a function `single_period()` that takes in a sample rate and returns values linearly spaced between 0 and the number of radians at which the sine function completes one cycle. `single_period(10)` should return
    ```
    array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
    3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
    ```

3. (*) Create a function `single_sine()`. In this function you should use `single_period()` to generate the x-axis that the sine function takes as input. Return the results of the sine function. In three different plots, plot the sine wave for the sample rates `10`, `50` and `100`.
    * Use `plt.plot(x, y)` where `x` are the correct time stamps in seconds for each sine wave. You can use a combination of `samples_to_time()` and `single_period()` to generate the time stamps.

    * Describe what you see in the plot. What is the total duration in seconds of each sine wave. Explain the difference in duration of each sine wave.


Based on what we have seen so far, it would be beneficial to be able to control more than just the sample rate of our sine waves. We also want to control:
    * The frequency of the sine wave (i.e. how many cycles the sine wave achieves per second)
    * The duration of the wave (in seconds)
Lets tackle these two parameters one by one.

4. (*) Define a function `sine5(sine_hz, sr)` that returns a sine wave with a 5 second duration sampled with the given `sr` and a frequency corresponding to `sine_hz`. Plot 3 sine waves in the same figure with `sine_hz = 1` and
    * sr = 5
    * sr = 10
    * sr = 100
Use your `gen_time()` to create the x-axis for each plot. Based on the plot, explain the difference between the sine waves.

5. (*) Define a function `sine(sine_hz, sr, duration)` that achieves the same as `sine5()` but for any duration (in seconds). In the same figure, plot three sines with `duration = 2`, `sr=1000` and:
    * `sine_hz = 1`
    * `sine_hz = 5`
    * `sine_hz = 20`
Again, use `gen_time()` for the x-axis of each plot.


## 3. Listen
Instead of just looking at these sine waves, lets try to listen to them.

1. (*) Generate a 5 second sine wave using your `sine()` function. The sine wave should have a frequency of 500 Hz sampled at 16000 Hz. Use `tools.save_audio()` to save your waveform to file. Then open it in e.g. `VLC` or any media player (Lower the volume if you are wearing headphones!). Describe what you hear.

2. (*) According to [this](https://en.wikipedia.org/wiki/Hearing_range), the human hearing range is commonly given as 20 - 20,000 Hz. Can you hear a 20Hz and a 20,000 Hz 1 second sine wave? Create a `low_sine()` and a `high_sine()` function to generate these waveforms sampled at 48,000 Hz.
    * Use the information from [this](http://www.speech.zone/sampling-and-quantisation/) to determine a minimum sample rate for the `high_sine()` function.