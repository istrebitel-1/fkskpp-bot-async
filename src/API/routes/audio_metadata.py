from .. import app
from src.bot.blueprints.chat import music_json

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from json import load, dump


@app.get('/info')
async def info():
    return {'version':f"{config['version']}"}


@app.get('/audio')
async def audio():

    html = '<table border="1">'
    music_json.upd()
    for item in music_json.music_json['music']:
        html += f'''
            <tr id="{item['track_id']}">
                <td>{item['name']}</td>
                <td>{item['track_id']}</td>
                <td>
                    <input type="button" value="Удалить" color="red" onclick="loadDoc('{item['track_id']}')">
                </td>
            </tr>
        '''
    
    html+= '''
        </table>
        <script>
            function loadDoc(id) {{
            const xhttp = new XMLHttpRequest();
            xhttp.open("DELETE", "audio/"+id, true);
            xhttp.send();
            document.getElementById(id).remove();
            }}
        </script>    
    '''

    return HTMLResponse(html)


@app.delete('/audio/{track_id}')
async def audio_delete(track_id):

    with open('json_data/music.json', 'r', encoding='utf-8') as read_file:
        music = load(read_file)

    for i in range(0, len(music['music'])):
        if music['music'][i]['track_id'] == track_id:
            music['music'].pop(i)
            break

    with open('json_data/music.json', 'w', encoding='utf-8') as f:
        dump(music, f, indent=4, ensure_ascii=False)

    music_json.upd()
    f.close()

    return {'success': True}


from src.bot import config
