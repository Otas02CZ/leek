from configuration import Configuration
import text





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
    
    