import json


class UserSettings:
    @classmethod
    def get_settings(self):
        with open('app/settings.json') as f:
            settings = json.load(f)

        MODE = settings['user_settings']['mode']
        ACCENT_COLOR = settings['user_settings']['accent_color']

        if MODE == 'light':
            BG_COLOR = settings['light_theme']['background']
            FG_COLOR = settings['light_theme']['foreground']
            CR_COLOR = settings['light_theme']['copyright']
        else:
            BG_COLOR = settings['dark_theme']['background']
            FG_COLOR = settings['dark_theme']['foreground']
            CR_COLOR = settings['dark_theme']['copyright']

        return {
            'MODE': MODE,
            'ACCENT_COLOR': ACCENT_COLOR,
            'BG_COLOR': BG_COLOR,
            'FG_COLOR': FG_COLOR,
            'CR_COLOR': CR_COLOR
        }

    @classmethod
    def write_settings(self, param, value):
        with open('app/settings.json', 'r') as f:
            settings = json.load(f)
            settings['user_settings'][param] = value

        with open('app/settings.json', 'w') as f:
            json.dump(settings, f, indent=4)
