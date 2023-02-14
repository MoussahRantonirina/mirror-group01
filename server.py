import web
import nav 
from database import Db
web.config.debug = True

urls = (
    '/', 'index',
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
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
