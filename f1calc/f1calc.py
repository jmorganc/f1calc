import json


def save_drivers(drivers, grandsprix):
    try:
        drivers_json = json.loads(open('drivers.json', 'r').read())
        for driver in drivers:
            if not driver in drivers_json:
                drivers_json[driver] = {}
            for gp in grandsprix:
                if not gp in drivers_json[driver]:
                    drivers_json[driver][gp] = 0
    except:
        drivers_json = {}
        for driver in drivers:
            drivers_json[driver] = {}
            for gp in grandsprix:
                drivers_json[driver][gp] = 0
        open('drivers.json', 'w').write(json.dumps(drivers_json, indent=4, sort_keys=True))


def save_grandsprix(grandsprix, drivers):
    try:
        grandsprix_json = json.loads(open('grandsprix.json', 'r').read())
        for gp in grandsprix:
            if not gp in grandsprix_json:
                grandsprix_json[gp] = {}
            for driver in drivers:
                if not driver in grandsprix_json[gp]:
                    grandsprix_json[gp][driver] = 0
    except:
        grandsprix_json = {}
        for gp in grandsprix:
            grandsprix_json[gp] = {}
            for driver in drivers:
                grandsprix_json[gp][driver] = 0
        open('grandsprix.json', 'w').write(json.dumps(grandsprix_json, indent=4, sort_keys=True))
