import json


class Converter:
    def __init__(self):
        pass

    def convert(self):
        print("Converting ...")
        with open('./data/events.json') as jsonfile:
            json_data = json.load(jsonfile)
        result = [json.dumps(record) for record in json_data]
        with open('./data/output.json', 'w') as output_file:
            json.dump(result, output_file)


if __name__ == '__main__':
    convert = Converter()
    convert.convert()

