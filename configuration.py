import os
import json



class Configuration:
    
    def __init__(self) -> None:
        self.base_path = f"{os.getenv('APPDATA')}/Leek"
        self.config_path = f"{os.getenv('APPDATA')}/Leek/config.txt"
        self.add_locales_path = f"{os.getenv('APPDATA')}/Leek/locales"
        self.cfg = {
            'save_cfg' : False,
            'rows' : 40,
            'locale' : 'cs',
            'size_unit': 'KB',
            'sort_key': 'none',
            'sort_direction' : 'up'
        }
    
    def get_cfg(self, key : str) -> any:
        return self.cfg[key]
    
    def set_cfg(self, key : str, value : any) -> None:
        self.cfg.update({key : value})
    
    def cfg_exists(self) -> bool:
        return os.path.exists(self.config_path)
    
    def load_cfg(self) -> str:
        if self.cfg_exists():
            cfg_file = open(self.config_path, "r")
            cfg_data = cfg_file.read()
            cfg_file.close()
            self.cfg.update(json.loads(cfg_data))
            return 'load_successful'
        else:
            return 'cannot_load'
    
    def save_cfg(self) -> str:
        if self.cfg['save_cfg']:
            if not os.path.exists(self.base_path):
                try:
                    os.mkdir(self.base_path)
                except:
                    return 'cannot_save'
            if not os.path.exists(self.add_locales_path):
                try:
                    os.mkdir(self.add_locales_path)
                except:
                    return 'cannot_save'
            cfg_file = open(self.config_path, "w")
            cfg_data = json.dumps(self.cfg)
            cfg_file.write(cfg_data)
            cfg_file.close()
            return 'save_successful'
        return 'not_saving'
            