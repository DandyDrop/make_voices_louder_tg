# import soundfile as sf
# import pyloudnorm as pyln
#
#
# def a(path_to_audio):
#     data, rate = sf.read(path_to_audio)  # load audio (with shape (samples, channels))
#     meter = pyln.Meter(rate)  # create BS.1770 meter
#     loudness = meter.integrated_loudness(data)  # measure loudness
#     if -20 < loudness:
#         target_loudness = loudness
#     elif -40 < loudness:
#         target_loudness = -25
#     else:
#         target_loudness = loudness + 20
#
#     loudness_normalized_audio = pyln.normalize.loudness(data, loudness, target_loudness)
#
#     sf.write(path_to_audio, loudness_normalized_audio, rate)

from pydub import AudioSegment, effects
from io import BytesIO


def normalize_audio(audio_bytes: bytes) -> BytesIO:
    raw_audio = AudioSegment.from_file(BytesIO(audio_bytes), 'ogg')
    normalized_audio: AudioSegment = effects.normalize(raw_audio)
    audio_buffer = BytesIO()
    normalized_audio.export(audio_buffer)
    return audio_buffer

