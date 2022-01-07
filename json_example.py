import json


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


tournaments = {
    'Aeroflot Open': 2010,
    'FIDE World Cup': 2012,
    'FIDE Grand Prix': 2017
}

json_data = json.dumps(tournaments, indent=2) # сериализация
print(json_data)

loaded = json.loads(json_data) # десериализация
print(type(loaded))
print(loaded)

t1 = Tournament('Aeroflot Open', 2010)
json_data = json.dumps(t1.__dict__)
print(json_data)
t = Tournament(**json.loads(json_data))
print(f'name={t.name}, year={t.year}')


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments


t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament('FIDE World Cup', 2012)
t3 = Tournament('FIDE Grand Prix', 2017)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__)
print(json_data)

decoded_player = ChessPlayer(**json.loads(json_data))
print(decoded_player)

player_tournaments = decoded_player.tournaments[0]
print(type(player_tournaments))
print(player_tournaments)


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data['tournaments']))
        return cls(tournaments)


t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament('FIDE World Cup', 2012)
t3 = Tournament('FIDE Grand Prix', 2017)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
print(type(json_data))
print(json_data)

decoded_player = ChessPlayer.from_json(json.loads(json_data))
print(decoded_player)
print(decoded_player.tournaments)


with open('player.json', 'w') as file:
    json.dump(p1, file, default=lambda obj: obj.__dict__)

with open('player.json', 'r') as read_file:
    data = json.load(read_file)

print(data)

decoded_player = ChessPlayer.from_json(data)
print(decoded_player)
print(decoded_player.tournaments)






