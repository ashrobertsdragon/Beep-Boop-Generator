# Beep Boop Generator

The Beep Boop Generator is a Python script that converts a string of text into a sequence of tones ("beeps" and "boops") and exports this sequence as an audio file.

## Features

- Converts any given string to binary representation.
- Generates two distinct tones for binary 1s (beeps) and 0s (boops).
- Combines the sequence of tones into a single WAV file.

## Prerequisites

Before running this script, you will need to install the `pydub` library, which is used for handling audio segments. If you don't have it installed, you can install it using pip:

```bash
pip install pydub
```

## Usage

To use the Beep Boop Generator, simply run the script in your Python environment. The script will prompt you to enter a word or phrase, which it will then convert into an audio file `beepboop.wav` in the current directory.

### Running the Script

Execute the script from the command line:

```bash
python beep_boop_generator.py
```

Follow the prompt to enter a word or phrase when the script is running:

```text
Enter a word or phrase: Hello World!
```

After inputting the text, the script will create an audio file named `beepboop.wav` in the same directory, encoding the binary representation of the input text in tones.

## License

This script is released under the MIT License. See the LICENSE file for details.