from datetime import datetime

class EstonianPeopleAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_age(self, birth_date, death_date=None):
        now = datetime.now()
        if death_date:
            if (death_date.month, death_date.day) < (birth_date.month, birth_date.day):
                return death_date.year - birth_date.year - 1
            return death_date.year - birth_date.year
        else:
            age = now.year - birth_date.year
            if (now.month, now.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age

    def analyze_data(self):
        results = {
            'total_count': len(self.data),
            'longest_name': ('', 0),
            'oldest_alive': (None, -1, '', ''),
            'oldest_deceased': (None, -1, '', ''),
            'actors_count': 0,
            'born_in_1997_count': 0,
            'unique_roles_count': 0,
            'more_than_two_names_count': 0,
            'same_birth_and_death_day_count': 0,
            'alive_count': 0,
            'deceased_count': 0
        }

        oldest_deceased_age = -1
        for person in self.data:
            name_length = len(person['nimi'])
            if name_length > results['longest_name'][1]:
                results['longest_name'] = (person['nimi'], name_length)

            birth_date = datetime.strptime(person['sundinud'], '%Y-%m-%d')
            if person['surnud'] == '0000-00-00':
                age = self.calculate_age(birth_date)
                if age > results['oldest_alive'][1]:
                    results['oldest_alive'] = (person['nimi'], age, birth_date.strftime('%d.%m.%Y'), '')

            elif person['surnud'] != '0000-00-00':
                death_date = datetime.strptime(person['surnud'], '%Y-%m-%d')
                birth_date = datetime.strptime(person['sundinud'], '%Y-%m-%d')
                age = self.calculate_age(birth_date, death_date)
                if age > oldest_deceased_age:
                    oldest_deceased_age = age
                    results['oldest_deceased'] = (person['nimi'], age, birth_date.strftime('%d.%m.%Y'),
                                                  death_date.strftime('%d.%m.%Y'))

            if 'näitleja' in person.get('amet', '').lower():
                results['actors_count'] += 1

            if person['sundinud'].startswith('1997'):
                results['born_in_1997_count'] += 1



            if len(person['nimi'].split(' ')) > 2:
                results['more_than_two_names_count'] += 1

            if person['surnud'] != '0000-00-00' and person['sundinud'][5:] == person['surnud'][5:]:
                results['same_birth_and_death_day_count'] += 1

            if person['surnud'] == '0000-00-00':
                results['alive_count'] += 1
            else:
                results['deceased_count'] += 1
        results['unique_roles_count'] = len(set(person['amet'] for person in self.data))
        return results
