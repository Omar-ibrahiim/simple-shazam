import librosa
import numpy as np
import sounddevice as sd


class SoundData():
    """
    A class that handles sound data
    """
    def __init__(self, sndPath: str = None):
        if sndPath == None:
            self.sndPath, self.sndByte, self.sr = None, None, None
            sd.stop()
        else:
            self.sndPath = sndPath
            self.sndByte, self.sr = librosa.load(sndPath,
                                                 duration=60.0,
                                                 sr=44100)

    def playAudio(self):
        #sd.play(self.sndByte, self.sr)
        return

    def mix(self, imageToBeMixed: 'SoundData', ratio: float):
        Mix = SoundData()
        Mix.sndByte = (ratio * self.sndByte) + (
            (1 - ratio) * imageToBeMixed.sndByte)
        Mix.sr=44100
        return Mix
