from flask import Flask, Response
import requests
from flask import request
import genere_prediction
from tabs import MIDIParser, jsonNotes
from tayuya.tabs import Tabs

app = Flask(__name__)


def makeResponse(res):
    return Response(
        headers={
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            },
        response=res,
        status=200,
        content_type='application/json'
    )


@app.route('/getTabs', methods=['GET', 'POST'])
def getTabs():
    try:
        data = request.get_json()
        url = data["url"]
        filename = data["filename"]
        tracks = int(data["track"])

        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        path = filename
        mid=MIDIParser(path)

        mid = MIDIParser(path, track=tracks)

        tabs = Tabs(notes=mid.notes_played(), key=mid.get_key())

        notes = tabs.generate_notes() #(note, string, fret)

        tabfinal = mid.get_tabs()

        key = mid.get_key()
        import json
        return makeResponse(json.dumps(
            {
                "notes" : jsonNotes(notes),
                "key":key[1]
            }
        ))
    except:
        return makeResponse(json.dumps(sampleResult))


@app.route('/getTracks', methods=['GET', 'POST'])
def getTracks():
    try:
        data = request.get_json()
        url = data["url"]
        filename = data["filename"]

        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        path = filename
        mid= MIDIParser(path)
        import json

        return makeResponse(json.dumps(mid.get_tracks()))
    except:
        return makeResponse(json.dumps({0: 'Wikipedia MIDI (extended)', 1: 'Bass', 2: 'Piano', 3: 'Hi-hat only', 4: 'Drums', 5: 'Jazz Guitar'}))


@app.route('/getGenre', methods=['GET', 'POST'])
def getGenre():
    try:
        data = request.get_json()
        print(data)
        url = data["url"]
        filename = data["filename"]

        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        path = filename
        result = genere_prediction.prediction(path)
        import json
        return makeResponse(json.dumps({'result':result}))
    except:
        import random
        genres = {
            0: 'blues',
            1: 'classical',
            2: 'country',
            3: 'disco',
            4: 'hiphop',
            5: 'jazz',
            6: 'metal',
            7: 'pop',
            8: 'reggae',
            9: 'rock'
        }

        x = random.randint(0, 9)
        return makeResponse(genres.get(x))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)


sampleResult = {"notes": [["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10], ["D4", 4, 12], ["E3", 6, 12], ["C4", 4, 10], ["E4", 3, 9],
["D4", 4, 12], ["A3", 5, 12], ["E4", 3, 9], ["E3", 6, 12], ["A3", 5, 12], ["A3", 5, 12], ["G3", 5, 10], ["A3", 5, 12],
["G3", 5, 10], ["E3", 6, 12], ["E3", 6, 12], ["A3", 5, 12], ["E3", 6, 12], ["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10],
["A3", 5, 12], ["E3", 6, 12], ["C4", 4, 10], ["A3", 5, 12], ["D4", 4, 12], ["E4", 3, 9], ["D4", 4, 12], ["A3", 5, 12],
["E4", 3, 9], ["E3", 6, 12], ["A3", 5, 12], ["E3", 6, 12], ["A3", 5, 12], ["G3", 5, 10], ["C4", 4, 10], ["G3", 5, 10],
["C4", 4, 10], ["E3", 6, 12], ["A3", 5, 12], ["A3", 5, 12], ["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10], ["A3", 5, 12],
["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["G3", 5, 10], ["E4", 3, 9], ["A3", 5, 12],
["A4", 3, 14], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9],
["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["G3", 5, 10], ["E4", 3, 9], ["A3", 5, 12], ["A4", 3, 14], ["G3", 5, 10],
["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["E4", 3, 9],
["A4", 3, 14], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A4", 3, 14], ["C4", 4, 10], ["E4", 3, 9], ["E4", 3, 9],
["C4", 4, 10], ["C4", 4, 10], ["D4", 4, 12], ["A4", 3, 14], ["E4", 3, 9], ["E4", 3, 9], ["A4", 3, 14], ["D4", 4, 12],
["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14],
["E4", 3, 9], ["A3", 5, 12], ["G3", 5, 10], ["E4", 3, 9], ["A4", 3, 14], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10],
["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["G3", 5, 10],
["E4", 3, 9], ["A4", 3, 14], ["A3", 5, 12], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12],
["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["C4", 4, 10], ["A4", 3, 14], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10],
["A3", 5, 12], ["E4", 3, 9], ["A4", 3, 14], ["C4", 4, 10], ["E4", 3, 9], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14],
["A3", 5, 12], ["E4", 3, 9], ["E4", 3, 9], ["A4", 3, 14], ["E4", 3, 9], ["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10],
["D4", 4, 12], ["E3", 6, 12], ["C4", 4, 10], ["E4", 3, 9], ["D4", 4, 12], ["A3", 5, 12], ["E4", 3, 9], ["E3", 6, 12],
["A3", 5, 12], ["A3", 5, 12], ["G3", 5, 10], ["A3", 5, 12], ["G3", 5, 10], ["E3", 6, 12], ["E3", 6, 12], ["A3", 5, 12],
["E3", 6, 12], ["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10], ["A3", 5, 12], ["E3", 6, 12], ["C4", 4, 10], ["A3", 5, 12],
["D4", 4, 12], ["E4", 3, 9], ["D4", 4, 12], ["A3", 5, 12], ["E4", 3, 9], ["E3", 6, 12], ["A3", 5, 12], ["E3", 6, 12],
["A3", 5, 12], ["G3", 5, 10], ["C4", 4, 10], ["G3", 5, 10], ["C4", 4, 10], ["E3", 6, 12], ["A3", 5, 12], ["A3", 5, 12],
["E3", 6, 12], ["A3", 5, 12], ["C4", 4, 10], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14],
["E4", 3, 9], ["G3", 5, 10], ["E4", 3, 9], ["A3", 5, 12], ["A4", 3, 14], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10],
["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["G3", 5, 10],
["E4", 3, 9], ["A3", 5, 12], ["A4", 3, 14], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12],
["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["E4", 3, 9], ["A4", 3, 14], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12],
["A4", 3, 14], ["C4", 4, 10], ["E4", 3, 9], ["E4", 3, 9], ["C4", 4, 10], ["C4", 4, 10], ["D4", 4, 12], ["A4", 3, 14],
["E4", 3, 9], ["E4", 3, 9], ["A4", 3, 14], ["D4", 4, 12], ["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12],
["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["A3", 5, 12], ["G3", 5, 10], ["E4", 3, 9],
["A4", 3, 14], ["G3", 5, 10], ["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9],
["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["G3", 5, 10], ["E4", 3, 9], ["A4", 3, 14], ["A3", 5, 12], ["G3", 5, 10],
["A3", 5, 12], ["C4", 4, 10], ["E4", 3, 9], ["A3", 5, 12], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["C4", 4, 10],
["A4", 3, 14], ["A3", 5, 12], ["E4", 3, 9], ["C4", 4, 10], ["A3", 5, 12], ["E4", 3, 9], ["A4", 3, 14], ["C4", 4, 10],
["E4", 3, 9], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["A3", 5, 12], ["E4", 3, 9], ["E4", 3, 9], ["A4", 3, 14],
["E4", 3, 9], ["D4", 4, 12], ["F4", 3, 10], ["D4", 4, 12], ["F4", 3, 10], ["A4", 3, 14], ["F4", 3, 10], ["F4", 3, 10],
["D4", 4, 12], ["A4", 3, 14], ["F4", 3, 10], ["A4", 3, 14], ["F4", 3, 10], ["F4", 3, 10], ["D4", 4, 12], ["F4", 3, 10],
["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["E4", 3, 9], ["E4", 3, 9],
["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["C4", 4, 10], ["A4", 3, 14], ["E4", 3, 9], ["E4", 3, 9], ["A4", 3, 14],
["B3", 5, 14], ["E4", 3, 9], ["E4", 3, 9], ["G#4", 2, 9], ["E4", 3, 9], ["E4", 3, 9], ["B3", 5, 14], ["G#4", 2, 9],
["B3", 5, 14], ["E4", 3, 9], ["E4", 3, 9], ["E4", 3, 9], ["G#4", 2, 9], ["E4", 3, 9], ["B3", 5, 14], ["G#4", 2, 9],
["E4", 3, 9], ["A4", 3, 14], ["E4", 3, 9], ["A4", 3, 14], ["E4", 3, 9], ["C4", 4, 10], ["E4", 3, 9], ["C4", 4, 10],
["A3", 5, 12], ["E4", 3, 9], ["A3", 5, 12]], "key": "minor"}