from configuration import Configuration
import text
import os
import pathlib
import json




class Localization():
    def __init__(self, cfg : Configuration) -> None:
        self.locales = text.initial_locales
        self.localization_data = text.initial_localization
        self.cfg = cfg
    
    def get_text(self, key : str) -> str:
        if key in self.localization_data[self.cfg.get_cfg('locale')]:
            return self.localization_data[self.cfg.get_cfg('locale')][key]
        else:
            return "none"
    
    def get_locales(self) -> str:
        locales = ""
        for locale in self.locales:
            locales+= f"{locale} "
        return locales
    
    def load_localization(self) -> str:
        if self.cfg.get_cfg('save_cfg'):
            if os.path.exists(self.cfg.add_locales_path):
                for file_name in os.listdir(self.cfg.add_locales_path):
                    file_path = os.path.join(self.cfg.add_locales_path, file_name)
                    if os.path.isfile(file_path):
                        if pathlib.Path(file_path).suffix == '.llf':
                            new_locale = pathlib.Path(file_path).stem
                            is_new = True
                            for locale in self.locales:
                                if locale == new_locale:
                                    is_new = False
                            if is_new:
                                self.locales.append(new_locale)
                            try:
                                locale_file = open(file_path)
                                locale_data = locale_file.read()
                                locale_file.close()
                            except:
                                return 'cannot_load_localization'
                            self.localization_data.update(json.loads(locale_data))                          
        return 'available_localization_loaded'
    
    