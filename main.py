#Simple abuse the keyboard program
from gtts import gTTS
from playsound import playsound
from pynput import keyboard


text = "Stop Pressing My Buttons!"
language = "en"

myobj = gTTS(text=text, lang=language, slow=True)
myobj.save("sound.mp3")

def on_press(key):
        try:
           playsound("sound.mp3")
        except AttributeError:\
            print('Key {0} pressed'.format(key))
#Add Code
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


# Collect events until released
with keyboard.Listener(on_press= on_press,on_release=on_release) as listener:
    listener.join()

