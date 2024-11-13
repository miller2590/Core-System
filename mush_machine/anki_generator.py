import genanki
from gtts import gTTS
import uuid
import os


class AnkiGenerator:
    def __init__(self, deck_name, data):
        self.deck_name = deck_name
        self.data = data
        self.deck = None
        self.deck_id = None
        self.model = None
        self.model_config = None
        self.note = None

    def generate_audio_file(self):
        audio_dir = f'anki_{self.deck_name}_audio'
        os.makedirs(name=audio_dir, exist_ok=True)

        audio_files = []
        for i, target_language in enumerate(self.data["Spanish Phrase"]):
            tts = gTTS(text=target_language, lang='es')
            audio_file = f'{audio_dir}/translation_{i}.mp3'
            tts.save(audio_file)
            audio_files.append(audio_file)
        return audio_files

    def create_deck(self):
        self.deck = genanki.Deck(
            int(uuid.uuid4().int & (1 << 31) - 1),
            self.deck_name
        )

    def create_model(self):
        self.model = genanki.Model(
            self.model_config["id"],
            self.model_config["description"],
            fields=self.model_config["fields"],
            templates=self.model_config["templates"]
        )

    def create_note(self):
        for i, (target_language, native_language) in enumerate(
                zip(self.data["Spanish Phrase"], self.data["English Translation"])):
            self.note = genanki.Note(
                model=self.model,
                fields=[target_language, native_language, f'[sound:translation_{i}.mp3]']
            )
            self.deck.add_note(self.note)

    def create_package(self):
        audio_files = self.generate_audio_file()
        package = genanki.Package(self.deck)
        package.media_files = audio_files
        package.write_to_file(f'{self.deck_name}.apkg')
