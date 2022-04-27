from tools import read_audio, save_audio


def test():
    # wave contains the samples and sr is the sample rate
    # for the audio file

    # note: On some systems, this relative path will not work
    #       and you will need to change it to an absolute path
    #       (e.g. /path/to/data/f1.wav)
    wave, sr = read_audio('./data/f1.wav')
    print(f'The number of samples: {wave.shape[0]}\n')

    # save the audio to a new location
    save_audio(wave, sr, './data/new_f1.wav')

if __name__ == '__main__':
    test()