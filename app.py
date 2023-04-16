from flask import Flask
import tabs
import requests
from flask import request
import genere_prediction

app = Flask(__name__)


@app.route('/getTabs', methods=['GET', 'POST'])
def getTabs():
    data = request.get_json()
    url = data["url"]
    filename = data["filename"]
    tracks = int(data["track"])

    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    
    path = filename
    mid=tabs.MIDIParser(path)

    mid = tabs.MIDIParser(path, track=tracks)
    mid.render_tabs()
    tabs = tabs.Tabs(notes=mid.notes_played(), key=mid.get_key())
    
    notes = tabs.generate_notes() #(note, string, fret)

    tabfinal = mid.get_tabs()

    key = mid.get_key()

    import json
    return json.dumps(
        {
            "notes" : tabs.jsonNotes(notes),
            "key":key[1]
        }
    )

@app.route('/getTracks', methods=['GET', 'POST'])
def getTracks():
    data = request.get_json()
    print(data)
    url = data["url"]
    filename = data["filename"]

    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    
    path = filename
    mid=tabs.MIDIParser(path)
    import json
    return json.dumps(mid.get_tracks())



@app.route('/getGenre', methods=['GET', 'POST'])
def getGenre():
    data = request.get_json()
    print(data)
    url = data["url"]
    filename = data["filename"]

    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    
    path = filename
    result = genere_prediction.prediction(path)
    import json
    return json.dumps({'result':result})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)