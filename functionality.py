from pydub import AudioSegment, effects
from io import BytesIO


def normalize_audio(audio_bytes: bytes) -> BytesIO:
    raw_audio = AudioSegment.from_file(BytesIO(audio_bytes), 'ogg')
    normalized_audio: AudioSegment = effects.normalize(raw_audio)
    audio_buffer = BytesIO()
    audio_buffer.name = True
    normalized_audio.export(audio_buffer)
    return audio_buffer

