import json
import os
from mush_machine.anki_generator import AnkiGenerator
from utils.conversation_data import conversation_data
from utils.logger import Logger

logger = Logger.get_logger(name=__name__)


class Main:
    def __init__(self):
        self.config = self.get_config()
        self.data = conversation_data

    @staticmethod
    def get_config():
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as config_file:
            if config_file:
                return json.load(config_file)
            else:
                logger.warning("No config found")

    def run(self):
        anki_generator = AnkiGenerator(deck_name="Common Conversation", data=self.data)
        anki_generator.model_config = self.config["mush_config"]["base_model"]
        anki_generator.create_deck()
        anki_generator.create_model()
        anki_generator.create_note()
        anki_generator.create_package()
        logger.info("Anki package created successfully")


if __name__ == "__main__":
    main = Main()
    main.run()
