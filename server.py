import web
import nav 
from details import details
from database import Db
web.config.debug = True

urls = (
    '/', 'index',
    '/liste','liste',
    '/details','details'
)
class index:
    def GET(self):
        return '''<html>
        <head>
            <meta charset="UTF-8">
            <title>Accueil</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <style>
                body{
                    background-image: url('https://w.wallhaven.cc/full/1k/wallhaven-1kzryg.png');
                    background-size: cover;
                }
                #msg{
                    text-align: center;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    color: white;
                }
            </style>
        </head>
        <body>
            ''' + nav.navbar() + '''
            <div id="msg">
                <h1>Bienvenue sur Music</h1>
                <p>Découvrez notre top 10 des meilleures musiques du moment</p>
            </div>
        </body>
        </html>
        '''  
class liste:
    def GET(self):
        d = Db()
        db = d.getDb()
        albums = db.select('Album', limit=10)
        artists = db.select('Artist', limit=10)
        result = '<html><head><meta charset="UTF-8"><title>Tracklist</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.navbar()
        result += '<div class="container">'
        result += '<h4 class="text-center my-5">Notre top 10 des meilleures musiques du mois</h4>'
        result += '<table class="table table-striped table-bordered mx-auto">'
        result += '<tr class="table-bordered thead-dark text-center"><th class="p-3 table-dark">ID</th><th class="p-3 table-dark">Artist</th><th class="p-3 table-dark">Album Title</th></tr>'
        for artist in artists: 
            result += '<tr class="table table-striped table-bordered">'
            result += '<td class="table-primary p-2 ">'+ str(artist.ArtistId) +'</td>'
            for album in albums:
                result += '<td>' + artist.Name + '</td>'
                result += '<td>' + album.Title + '</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
