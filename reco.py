from vosk import Model,KaldiRecognizer
import pyaudio

model=Model(r"C:\Gen AI\vosk\vosk models\vosk-model-small-hi-0.22")

recognizer=KaldiRecognizer(model,16000)

mic=pyaudio.PyAudio()

stream=mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)

stream.start_stream()

while True:
    data=stream.read(4096, exception_on_overflow=False)
    if len(data)==0:
        break
    elif recognizer.AcceptWaveform(data):
        print(recognizer.Result())
        print(recognizer.PartialResult())


  