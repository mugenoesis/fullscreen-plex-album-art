from time import sleep

import requests
from plexapi.server import PlexServer
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('album.html')


if __name__ == '__main__':
    # app.run()
    baseurl = ''
    token = ''
    player_name = ''

    previous_album_title = ''

    while True:

        plex = PlexServer(baseurl, token)
        sessions = plex.sessions()
        for session in sessions:
            for player in session.players:
                if player.title == player_name:
                    if previous_album_title != session.parentTitle:
                        previous_album_title = session.parentTitle
                        x = requests.get(session.thumbUrl)

                        open('templates/album.jpg', 'wb').write(x.content)

                        f = open("templates/album.html", "r")
                        test = f.read()

                        f = open("templates/album.html", "w")
                        f.write(test)
                        f.close()
        sleep(1)
