from configparser import ConfigParser


class Scenario:
    def __init__(self, name: str, author: str, description: str, audios, img: str, roles, discussion_time=40):
        self.name = name
        self.author = author
        self.description = description
        self.roles = roles  # Implementierte Rollen im Szenario
        self.audios = audios  # Szenario spezifische Audios
        self.img = img
        self.role_weighting = {}
        self.discussion_time = discussion_time  # seconds

    def write_to_file(self):
        """Saves Scenario to config"""
        file = ConfigParser(allow_no_value=True)
        file['GENERAL'] = {'name': self.name, 'author': self.author, 'description': self.description,
                           'discussion_time': self.discussion_time, 'img': self.img}
        role_name_array = {}
        for role in self.roles:
            role_name_array.update({role})
        file['ROLES'] = role_name_array

        audio_name_array = {}
        for audio in self.audios.keys():
            audio_name_array.update({audio: self.audios[audio]})
        file['AUDIOS'] = audio_name_array

        file_name = '../scenarios/' + self.name + '.ini'
        print('Write to \"' + file_name + '\"')

        with open(file_name, 'w') as f:
            file.write(f)

    def update_role(self, role, weighting):
        """Updates Roles Weighting in Scenario. Maybe unnecessary."""
        self.roles.update({role.name: role})
        self.role_weighting.update({role.name: weighting})

    def remove_role(self, role_name):
        """Removes a Role from the Scenario."""
        del self.roles[role_name]
        del self.role_weighting[role_name]

    def calculate_role_count(self, player_count):  # TODO Fertig Rollenanzahl berechnen
        """Calculate Role-Counts based on player-Count."""
        counts = {'werwolf': 1}
        roles = ['Nazi',
                 'Stalker',
                 'Nazi',
                 'Drogendealerin',
                 'Wingwoman',
                 'OW-Suchtie',
                 'Nazi',
                 'Nachbar',
                 'WG-Flittchen',
                 'Bodyguard',
                 'Dönermann',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Nazi',
                 'Künstler',
                 'Nazi',
                 'Künstler'
                 ]
        role_array = []
        for i in range(0, player_count):
            role_array.append(roles[i])
        for role in role_array:
            counts['role'] = role_array.count(role)

        # z.B. {'role_name': 5}
        return counts
