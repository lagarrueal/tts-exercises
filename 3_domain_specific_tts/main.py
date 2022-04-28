import numpy as np
import subprocess

from tools import read_audio, save_audio


def say_order(order: str, out_path:str, play: bool = False):
    '''
    Takes in e.g. "fish with fries and wine" and saves a synthesized
    waveform for the phone number at <out_path>
    '''
    parts = []
    details = order.split(' ')
    hello, sr = read_audio('./custom_data/hello.wav')
    start, sr = read_audio('./custom_data/start.wav')
    parts.append(hello)
    parts.append(gen_silence(1, sr))
    parts.append(start)
    for i in range(len(details)):
        parts.append(generate_meal(details[i]))

    end, _ = read_audio('./custom_data/end.wav')
    parts.append(end)

    output = splice(parts)

    save_audio(output, sr, out_path)
    if play:
        subprocess.call(['play', out_path])


def generate_meal(item):
    part, _ = read_audio(f'./custom_data/{item}.wav')
    return part


def splice(parts):
    return np.hstack(parts)

def gen_silence(duration, sr):
    return np.zeros(int(duration * sr))


if __name__ == '__main__':
    str = 'hotdog with vegetables and beer and steak with fries and soda'
    say_order(str, './custom_data/order.wav')
    # you can also use the following if you have
    # sox installed on your system.
    say_order(str, './custom_data/order.wav', play=True)