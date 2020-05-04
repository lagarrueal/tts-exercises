import os
import json
import matplotlib.pyplot as plt
from shutil import copyfile

from tools import read_audio

def test():
    archive_path = './data/example_archive'
    info = json.load(open(os.path.join(archive_path, 'info.json')))

    print(f'1. Number of recordings: {len(info)}, here are the recording IDs:')
    for id, rec_info in info.items():
        print(id)


    # access the information of the "first" recording
    first_id = list(info.keys())[0]
    print(f'2. The first recording ID is: {len(info)}')

    first_info = info[first_id]
    print(f'3. It was read by {first_info["collection_info"]["user_name"]}')

    # build the paths of the "first" recording and text
    speaker_id = first_info['collection_info']['user_id']
    wav_fname = first_info['recording_info']['recording_fname']
    text_fname = first_info['text_info']['fname']

    wav_path = os.path.join(archive_path, 'audio', str(speaker_id), wav_fname)
    text_path = os.path.join(archive_path, 'text', text_fname)

    # plot the first waveform
    wave, sr = read_audio(wav_path)
    print(f'4. The sample rate is: {sr}')
    plt.plot(wave)
    plt.show()

    # move this sentence, waveform pair to a new location in a new format
    new_location = './data/new_archive'
    audio_dir = os.path.join(new_location, 'audio')
    text_dir = os.path.join(new_location, 'text')

    # create the new directories
    os.makedirs(audio_dir)
    os.makedirs(text_dir)

    # Copy the files to the new location. Change the file names such that the audio
    # file will be 0001.wav and the sentence file will be 0001.txt
    copyfile(wav_path, os.path.join(audio_dir, '{:04d}.wav'.format(1)))
    copyfile(text_path, os.path.join(text_dir, '{:04d}.txt'.format(1)))

    print(f'5. I have moved the first recording to the new location. Check it at {new_location}')

if __name__ == '__main__':
    test()