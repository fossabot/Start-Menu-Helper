import configparser
import typing


class Configuration:

    def __init__(self):
        self._config = configparser.ConfigParser()

        self.reload()

        if not self._config.sections():
            self._create_new_config()

    def _create_new_config(self):
        """Create a default configuration file."""
        self._config["options"] = {
            "flatten_folders_str": "None",
            "delete_empty_folders_bool": False,
            "delete_duplicates_bool": False,
            "delete_files_based_on_file_type_str": "in the list",
            "delete_broken_links_bool": False
        }
        self.save()

    def reload(self):
        """Reload the configuration from the configuration file."""
        self._config.read("config.ini")

    def save(self):
        """Save the configuration to the configuration file."""
        with open("config.ini", "w") as configfile:
            self._config.write(configfile)

    def get(self, key: str) -> typing.Union[bool, int, float, str]:
        """Get a value from the configuration in its correct type."""
        if key.endswith("_bool"):
            return self._config["options"].getboolean(key)
        elif key.endswith("_int"):
            return self._config["options"].getint(key)
        elif key.endswith("_float"):
            return self._config["options"].getfloat(key)
        else:
            return self._config["options"][key]

    def set(self, key: str, value: typing.Union[bool, int, float, str]):
        """Set a value in the configuration."""
        self._config["options"][key] = str(value)