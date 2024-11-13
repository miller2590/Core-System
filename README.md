# Anki Deck Generator

This project generates Anki decks with audio files for language learning. It uses the `genanki` library to create Anki packages and `gTTS` to generate audio files.

## Features

- Generate Anki decks with custom models and notes.
- Add audio files to the notes using Google Text-to-Speech (gTTS).
- Save the generated Anki package as a `.apkg` file.

## Requirements

- Python 3.6+
- `genanki` library
- `gTTS` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/anki-deck-generator.git
    cd anki-deck-generator
    ```

2. Install the required libraries:
    ```sh
    pip install genanki gtts
    ```

## Usage

1. Prepare your data and configuration files:
    - `config/config.json`: Contains the model configuration.
    - `utils/data_2.py`: Contains the data as a dictionary of lists.

2. Update the `config/config.json` file with your model configuration:
    ```json
    {
      "mush_config": {
        "base_model": {
          "id": 1908401568,
          "description": "Base Model with Audio",
          "fields": [
            {"name": "Spanish"},
            {"name": "English"},
            {"name": "Audio"}
          ],
          "templates": [
            {
              "name": "Card1",
              "qfmt": "{{Spanish}}<br>{{Audio}}",
              "afmt": "{{FrontSide}}<hr id=\"answer\">{{English}}"
            }
          ]
        }
      }
    }
    ```

3. Update the `utils/data_2.py` file with your data:
    ```python
    data_2 = {
        "Spanish Phrase": ["Hola", "Adiós"],
        "English Translation": ["Hello", "Goodbye"]
    }
    ```

4. Run the `main.py` script to generate the Anki package:
    ```sh
    python main.py
    ```

5. The generated Anki package will be saved as `Spanish Two.apkg`.

## Project Structure

- `main.py`: Main script to run the Anki deck generator.
- `anki_generator.py`: Contains the `AnkiGenerator` class to create the Anki deck, model, notes, and package.
- `config/config.json`: Configuration file for the Anki model.
- `utils/data_2.py`: Data file containing the phrases and translations.

## Example

Here is an example of how to use the `AnkiGenerator` class in `main.py`:

```python
import json
import os
from mush_machine.anki_generator import AnkiGenerator
from utils.data_2 import data_2

class Main:
    def __init__(self):
        self.config = self.get_config()
        self.data = data_2

    @staticmethod
    def get_config():
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as config_file:
            if config_file:
                return json.load(config_file)
            else:
                print("No config found")

    def run(self):
        anki_generator = AnkiGenerator(deck_name="Spanish Two", data=self.data)
        anki_generator.model_config = self.config["mush_config"]["base_model"]
        anki_generator.create_deck()
        anki_generator.create_model()
        anki_generator.create_note()
        anki_generator.create_package()
        print(f"Anki package created successfully")

if __name__ == "__main__":
    main = Main()
    main.run()
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
