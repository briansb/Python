import configparser
import os

from create_config import createConfig


def crudConfig(path):
    """
    Create, read, update, delete config
    """
    if not os.path.exists(path):
        createConfig(path)
    
    stat = os.stat(path)
    if stat.st_size == 0:
        # File is zero bytes
        raise RuntimeError('Settings file is empty')
    
    config = configparser.ConfigParser()
    config.read(path)
    
    # read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")
    
    # change a value in the config
    config.set("Settings", "font_size", "12")
    
    # delete a value from the config
    config.remove_option("Settings", "font_style")
    
    # write changes back to the config file
    with open(path, "w") as config_file:
        config.write(config_file)
        
if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)