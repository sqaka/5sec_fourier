import wave as wave
from datetime import datetime
import numpy as np
import sounddevice as sd

REC_TIME = 5
SAMPLE_RATE = 16000
SAVE_DIR = 'src/static/data/'


def rec_sound():
    wave_length = REC_TIME
    sample_rate = SAMPLE_RATE
    data = sd.rec(int(wave_length*sample_rate),
                  sample_rate, channels=1)
    sd.wait()

    data_scale_adjust = data * np.iinfo(np.int16).max
    data_scale_adjust = data_scale_adjust.astype(np.int16)

    return data_scale_adjust


def save_sound(data_scale_adjust):
    save_dir = SAVE_DIR
    now = datetime.now()
    dt_txt = '{0:%Y%m%d%H%M%S}'.format(now)

    wave_out = wave.open(save_dir + '{}.wav'.format(dt_txt), 'w')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(SAMPLE_RATE)
    wave_out.writeframes(data_scale_adjust)

    wave_out.close()
    return dt_txt


def main():
    data_scale_adjust = rec_sound()
    dt_txt = save_sound(data_scale_adjust)
    return dt_txt


if __name__ == '__main__':
    main()
