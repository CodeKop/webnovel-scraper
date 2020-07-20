import json

# TODO: Consider directly inheriting from file management modules, like json, yaml, whatever and implementing methods to work with these differen format. Don't think its going to work though.


class ConfigManager(object):
    def __init__(self):
        pass
    
    def load_config(self, filename):
        """ Load config file data to the config manager instance. """