import json

class UserSettings:
    @classmethod
    def user_settings(self):
        with open('app/settings.json') as f:
            settings = json.load(f)

        THEME = 'light'
        ACCENT_COLOR = '#e74c3c'
        # ACCENT_COLOR = '#2e86de'

        if THEME == 'light':
            BG_COLOR = settings['light_theme']['background']
            FG_COLOR = settings['light_theme']['foreground']
            CR_COLOR = settings['light_theme']['copyright']
        else:
            BG_COLOR = settings['dark_theme']['background']
            FG_COLOR = settings['dark_theme']['foreground']
            CR_COLOR = settings['dark_theme']['copyright']
        
        return {
            'THEME': THEME,
            'ACCENT_COLOR': ACCENT_COLOR,
            'BG_COLOR': BG_COLOR,
            'FG_COLOR': FG_COLOR,
            'CR_COLOR': CR_COLOR
        }

if __name__ == "__main__":
    color = UserSettings.user_settings()
    print(color['BG_COLOR'])