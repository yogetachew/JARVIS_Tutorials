# The recognizer hangs on recognizer_instance.listen;
# when it’s calling Microphone.MicrophoneStream.read
# Once you do this, change all instances of Microphone() to
# Microphone(device_index=MICROPHONE_INDEX),
# where MICROPHONE_INDEX is the hardware-specific index of the microphone.
# To figure out what the value of MICROPHONE_INDEX should be,
# run the following code:
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(
        f'Microphone: \"{name}\" found for `Microphone(device_index={index})`')