import os
if __name__=="__main__":

    print("Welcome to Robospeaker 1.1. Created by Sehaj Arora")
    while(True):
        s=input("What do you want to speak: ")
        if(s=="q"):
             print("Bye bye friend!")
             break
        command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
        os.system(command)