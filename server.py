import web
web.config.debug = True

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        albums = db.select('Album', limit=5)
        artists = db.select('Artist', limit=5)
        genres = db.select('Genre',limit=5) 
        customers= db.select('Customer', limit=5)
        media = db.select('MediaType', limit=5)
        
        result = '<html><head><title>SERVER-GROUP001</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += '<nav class="navbar navbar-expand-lg navbar-light bg-primary">'
        result += '<a class="col-3 navbar-brand" href="#">Music</a>'
        result += '</button>'
        result += '<div class="col-6 offset-2 collapse navbar-collapse text-center"  id="navbarNav">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item">'
        result += '<a class="nav-link text-light" href="#">Accueil</a>'
        result += '</li>'
        result += '<li class="nav-item text-light">'
        result += '<a class="nav-link text-light" href="#">Album</a>'
        result += '</li>'
        result += '<li class="nav-item">'
        result += '<a class="nav-link text-light" href="#">Artist</a>'
        result += '</li>'
        result += '<li class="nav-item">'
        result += '<a class="nav-link text-light" href="#">Contact</a>'
        result += '</li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        result += '<table class"table-striped">'
        result += '<tr class="table-bordered thead-dark text-center"><th class="p-3 table-dark">id</th><th class="p-3 table-dark">Genres</th><th class="p-3 table-dark">Album</th><th class="p-3 table-dark">Artist</th><th class="p-3 table-dark">Customer_Company</th><th class="p-3 table-dark">MediaType</th></tr>'
        for artist in artists:
            result += '<tr class="table table-striped table-bordered">'
            result += '<td class="table-primary table-striped p-2 ">'+ str(artist.ArtistId) +'</td>'
            for genre in genres:
                result += '<td>' + genre.Name + '</td>'
                break
            for album in albums:
                result += '<td>' + album.Title + '</td>'
                break
            result += '<td>' + artist.Name + '</td>'
            for customer in customers:
                result += '<td>' + str(customer.Company) + '</td>'
                break
            for mediatype in media:
                result += '<td>' + mediatype.Name + '</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
