#!usr/bin/env python  
#coding=utf-8  

import pyaudio  
import wave  


#----------------------
#python setup.py register sdist upload
#



#define stream chunk   
chunk = 1024  

def choomah_scream():
    #open a wav format music
    f = wave.open(r"choomah.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()