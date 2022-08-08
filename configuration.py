import os
import json



class Configuration:
    
    def __init__(self) -> None:
        self.path = f"{os.getenv('APPDATA')}/Leek/config.txt"
        self.cfg = {
            'save_cfg' : False,
            'row_size' : 40,
            'locale' : 'cs'
        }
    
    def get_cfg(self, key : str) -> any:
        return self.cfg[key]
    
    def set_cfg(self, key : str, value : any) -> None:
        self.cfg.update({key : value})
    
    def cfg_exists(self) -> bool:
        return os.path.exists(self.path)
    
    def load_cfg(self):
        if self.cfg_exists:
            cfg_file = open(self.path, "r")
            cfg_data = cfg_file.read()
            cfg_file.close()
            self.cfg.update(json.loads(cfg_data))
    
    def save_cfg(self):
        if self.cfg['save_cfg']:
            cfg_file = open(self.path, "w")
            cfg_data = json.dumps(self.cfg)
            cfg_file.write(cfg_data)
            cfg_file.close()
            