from tools import read_audio, save_audio

import numpy as np
import matplotlib.pyplot as plt


def test():
    # wave contains the samples and sr is the sample rate
    # for the audio file
    wave, sr = read_audio('./data/f1.wav')

    print(f'The number of samples: {wave.shape[0]}\n')

    # Get the segment starting from 0:01.5 and lasting a second
    start = int(1.5 * sr)
    end = int((1.5 + 1) * sr)
    segment = wave[start: end]

    # plot the segment
    plt.plot(segment)
    plt.show()

    # save the segment
    save_audio(segment, sr, './data/segment.wav')

    # double the waveform by repeating every sample while
    # keeping the same sample rate
    doubled_wave = np.repeat(wave, 2)
    save_audio(doubled_wave, sr, './data/doubled.wav')

    # Now do the same but double the sample rate
    doubled_wave = np.repeat(wave, 2)
    save_audio(doubled_wave, sr*2, './data/doubled_2sr.wav')

    # Mix two recordings
    wave_2, _ = read_audio('./data/m1.wav')

    # cut the longer recording to be equal in length to the shorter
    max_samples = min(wave.shape[0], wave_2.shape[0])
    wave = wave[:max_samples]
    wave_2 = wave_2[:max_samples]

    # Lets give the female recording (wave) a higher relative amplitude
    mixed_wave = wave + 0.5 * wave_2
    save_audio(mixed_wave, sr, './data/mixed.wav')


if __name__ == '__main__':
    test()
