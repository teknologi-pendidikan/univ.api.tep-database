import json
import jsonschema
from jsonschema import validate


# University JSON Schema
f = open('jsonschema.json')
jsonSchema = json.load(f)


def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        print('==== SKEMA TIDAK DAPAT DIVALIDASI ====')
        print('UNIVERSITAS: {}'.format(err.instance['nama']))
        print('PESAN ERROR: {}'.format(err.message))
        print('======= PENGECEKAN DIHENTIKAN! =======')
        return False
    return True


with open("../list_universitas.json") as json_file:
    list_universitas = json.load(json_file)
    for data in list_universitas['daftarPT']:
        isValid = validateJson(data)

        if isValid:
            print('SKEMA VALID: {} - {} - {}'.format(data['nama'], data['kodePT'], data['domain']))
