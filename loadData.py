import os
import librosa
import json
import math
import numpy as np

DATASET_PATH = "Drum_Dataset"
JSON_PATH = "drum_data----.json"
SAMPLE_SIZE = int(22050/2) #0.5 seconds


def saveMfcc(datasetPath, jsonPath, n_mfcc=13, n_fft=2048, hop_length=512):

    #sets up dict
    data = {
        "mapping": [],
        "mfcc": [],
        "labels": []
    }

    #loop through folders
    for i, (dirPath, dirName, filesNames) in enumerate(os.walk(datasetPath)):

        testArray = np.zeros(shape=(1,0))
        tested = True

        #makes sure it gets to the data files
        if dirPath is not datasetPath:
            #gets mapping
            dirPathComponents = dirPath.split("/")
            mapLabel = dirPathComponents[-1]
            data["mapping"].append(mapLabel)
            print("\nProcessing {}".format(mapLabel))

            #gets files
            for file in filesNames:

                if not file == '.DS_Store':

                    #loads audio
                    filePath = os.path.join(dirPath, file)
                    signal, sr = librosa.load(filePath, sr=SAMPLE_SIZE)

                    #processes mfcc
                    lenOfSignal = len(signal)
                    signal = signal[:SAMPLE_SIZE] #cuts to 1 sec
                    mfcc = librosa.feature.mfcc(signal,
                                               sr=sr,
                                               n_mfcc=n_mfcc,
                                               n_fft=n_fft,
                                               hop_length=hop_length)

                    mfcc = mfcc.T

                    #gets expected length
                    expected_mfcc_length = math.ceil(SAMPLE_SIZE / hop_length)

                    if len(mfcc) < expected_mfcc_length:
                        #stretches files that have length lower than expected length
                        mfcc = stretchAdudio(mfcc, expected_mfcc_length, signal, sr, n_mfcc, n_fft, hop_length)

                        #used to write test files
                        # if mapLabel == "hihats":
                        #   wav = librosa.feature.inverse.mfcc_to_audio(mfcc.T)
                        #   librosa.output.write_wav('stectch_sample.wav', wav, SAMPLE_SIZE)


                    if len(mfcc) == expected_mfcc_length:
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i-1)
                        print("-----------------")
                    else:
                        print("SOMETHING IS WORNG")

    #writes up json file
    with open(jsonPath, "w") as fp:
        json.dump(data, fp, indent=4)


def stretchAdudio(mfcc, expected_mfcc_length, signal, sr, n_mfcc, n_fft, hop_length):
    '''recursively stretches the audio file until it gets to expected_mfcc_length'''

    if len(mfcc) < expected_mfcc_length:

        # calculates how much to stretch
        slowBy = len(mfcc) / (expected_mfcc_length)

        slowedSignal = librosa.effects.time_stretch(signal, slowBy)
        slowedSignal = slowedSignal[:SAMPLE_SIZE]

        mfcc = librosa.feature.mfcc(slowedSignal,
                                    sr=sr,
                                    n_mfcc=n_mfcc,
                                    n_fft=n_fft,
                                    hop_length=hop_length)
        mfcc = mfcc.T

        return stretchAdudio(mfcc, expected_mfcc_length, slowedSignal, sr, n_mfcc, n_fft, hop_length)

    else:
        return mfcc

if __name__=="__main__":
    saveMfcc(DATASET_PATH, JSON_PATH)










