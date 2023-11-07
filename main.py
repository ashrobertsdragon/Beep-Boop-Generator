from pydub import AudioSegment
from pydub.generators import Sine

def generate_tone(frequency):

  duration = 100
  tone = Sine(frequency).to_audio_segment(duration)


  return tone

def string_to_binary(input_string):
  
  binary_string = ""
  for character in input_string:
    binary_value = bin(ord(character))[2:]
    binary_string += binary_value


  return binary_string.strip()

def main():

  combine_wav = AudioSegment.silent(duration = 0)
  pause = AudioSegment.silent(duration = 10)

  beep = generate_tone(1200)
  boop = generate_tone(250)

  input_string = input("Enter a word or phrase: ")
  binary_string = string_to_binary(input_string)
   
  for bit in binary_string:
    if bit == "1":
      combine_wav += beep + pause
    else:
      combine_wav += boop + pause

  combine_wav.export("beepboop.wav", format="wav")

if __name__ == "__main__":
  main()