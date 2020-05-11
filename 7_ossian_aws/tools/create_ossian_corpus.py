import os
import json
import shutil

def create_ossian_corpus(in_path:str, out_path:str, voice_name:str):
    info = json.load(open(os.path.join(in_path, 'info2.json')))

    # create directories
    out_dir = out_path
    speaker_dir = os.path.join(out_dir, 'speakers', voice_name)
    wav_dir = os.path.join(speaker_dir, 'wav')
    txt_dir = os.path.join(speaker_dir, 'txt')
    other_dir = os.path.join(out_dir, 'text_corpora', 'ice_g2p')

    os.makedirs(txt_dir)
    os.makedirs(wav_dir)
    os.makedirs(other_dir)

    # iterate info
    for key, item in info.items():
        # get path for files
        wav_fname = item['recording_info']['recording_fname']
        wav_path = os.path.join(in_path, 'audio', str(item['collection_info']['user_id']), wav_fname)
        text_path =  os.path.join(in_path, 'text', item['text_info']['fname'])
        new_txt_fname = f'{os.path.splitext(wav_fname)[0]}.txt'

        # copy the files to the new corpus
        shutil.copyfile(wav_path, os.path.join(wav_dir, wav_fname))
        shutil.copyfile(text_path, os.path.join(txt_dir, new_txt_fname))


def change_sample_rate(in_path:str):




if __name__ == '__main__':
    create_ossian_corpus('corpus', 'corpus2', 'atli')