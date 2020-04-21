# Create your own domain specific TTS!
Your task is to create a TTS system with a very limited domain application. These types
of systems are often used where the output is either very limited or highly repeatable.
An example is the TTS system used by Strætó (The Icelandic public transport company).
A public transport system might record utterances like:
* "The next stop is"
* "Remember to take your belongings"
* "Hlemmur"
* "Hamraborg"
And then splice these together to form e.g. "The next stop is Hlemmur. Remember to take your belongings".

## Steps
### Select a domain.
You can do whatever you like but we highly encourage you to be creative! Basic examples would be to create something similar to Strætó's but limit it to your favorite route. You could also create a talking clock.

### Record the data
* Create a reading list
* Download [Audacity](https://www.audacityteam.org/download/), the recording client.
* Record your utterances
    * You should preferably trim your recordings such that they have a uniform starting and ending silences. You can do this be selecting the area of the waveform you want to cut by dragging over the waveform in Audacity and then press <ctrl+x>.
    * You want to export each utterance as a seperate `.wav` file.
    * Make sure to use the same format for every utterance (e.g. the same number of channels, the same sample rate and so on).

### Write your logic
The input to the system will most likely be text (as with other TTS systems). You will have create some logic that takes as input e.g. text and returns your synthesized voice. For a talking clock you would need something like

```
def speak(hour, minute):
    parts = []
    parts += generate_the_time_is() # a function that returns the waveform for "the time is"
    parts += generate_hour(hour) # maps the hour value to the corresponding hour waveform
    parts += generate_minute(minute) # same but for minutes

    output = splice(parts) # a function that splices together waveform parts
    return output
```

Take a look at `example.py` but you will need to define at least:
* your `say_phone()` function that takes in the text or whatever the input is for your system
* `splice()` The function that will combine your waveforms. It doesn't have to be complicated but some linear fading might be a good addition here!

You could also add:
* A function `gen_silence(duration, sr)` that creates a number of 0-frames to represent a period of silence for the given duration. This would allow you to create more complicated "prosody" by e.g. adding a period of silence after a "," in your input sentence (e.g. "Hello, my name is Atli").