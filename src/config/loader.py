import logging
import yaml
from core.models import Environment
from utils.validator import validate_path

class Loader:

    def __init__(self, file) -> None:
        self.file = yaml.load(file, Loader=self.get_loader())
        print(self.file)
    
    def get_contents(self):
        keys: list = self.file.keys() if self.file is not None else []

        log_level = self.file.get("log_level", "")
        master = self.file.get("master", "")
        app_name=self.file.get("app_name", "")
        source_file = validate_path(self.file.get("source_file", ""))
        print(source_file)

        return Environment(
            log_level=log_level,
            master=master,
            source_file=source_file,
            app_name=app_name
        )

    def get_loader(self):
        """
        Gets SafeLoader class from yaml
        :returns: SafeLoader
        """
        loader = yaml.SafeLoader

        return loader 
