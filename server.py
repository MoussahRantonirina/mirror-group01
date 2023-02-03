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
        
        result = '<html><head><title>TEST</title></head><body>'
        result += '<table border="1">'
        result += '<tr><th>id</th><th>Genres</th><th>Album</th><th>Artist</th><th>Customer_Company</th><th>MediaType</th></tr>'
        for artist in artists:
            result += '<tr>'
            result += '<td>'+ str(artist.ArtistId) +'</td>'
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
