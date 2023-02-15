import web
import nav
from database import Db
urls = (
    '/details','details',
    '/index','index'
)
class details:
    def GET(self):
        d = Db()
        db = d.getDb()
        albums = db.select('Album', limit=10)
        artists = db.select('Artist', limit=10)
        genres = db.select('Genre', limit=10)
        media = db.select('MediaType', limit=10)
        cust = db.select('Customer', limit=10)
        
        result = '<html><head><meta charset="UTF-8"><title>Test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.css">'
        result += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.css">'
        result += '</head>'
        result += '<body>'
        result += nav.navbar()
        result += '<div class="container">'
        result += '<h4 class="text-center my-5">Notre top 10 des meilleures musiques du mois</h4>'
        result += '<div class="carousel" data-slick=\'{"dots": true,"prevArrow":"<button type=\\"button\\" class=\\"slick-prev text-dark bg-dark\\"><span class=\\"carousel-control-prev-icon text-dark\\" aria-hidden=\\"true\\"></span><span class=\\"sr-only text-dark\\">Previous</span></button>","nextArrow":"<button type=\\"button\\" class=\\"slick-next bg-dark\\"><span class=\\"carousel-control-next-icon text-dark\\" aria-hidden=\\"true\\"></span><span class=\\"sr-only text-dark\\">Next</span></button>"}\'>'
        
        for artist in artists:
            for album in albums:
                if album.ArtistId == artist.ArtistId:
                    result += '<div class="card">'
                    result += '<div class="card-header bg-dark text-white">'
                    result += '<h5 class="mb-0 text-center">' + album.Title + '</h5>'
                    result += '</div>'
                    result += '<div class="row">'
                    result += '<div class="col-4"><img src="https://w.wallhaven.cc/full/4x/wallhaven-4x87lz.jpg" class="card-img-top my-5 w-100"></div>'
                    result += '<div class="col-8 my-5">'
                    result += '<table class="table">'
                    result += '<tr><td>Artist:</td><td>'+ artist.Name+'</td></tr>'
                    for genre in genres:
                        if album.AlbumId == genre.GenreId:
                            result += '<tr><td>Genre:</td><td>'+ genre.Name+'</td></tr>'
                            break
                    for Media in media:
                        if album.AlbumId == Media.MediaTypeId:
                            result += '<tr><td>Type :</td><td>'+Media.Name+'</td></tr>'
                            break
                    for customer in cust:
                        if album.AlbumId == customer.CustomerId:    
                            result += '<tr><td>Compagnie du client :</td><td>'+str(customer.Company)+'</td></tr>'       
                            result += '<tr><td>Pays :</td><td>'+ customer.Country+'</td></tr>'        
                            break
                    result += '</table>'
                    result += '</div>'
                    result += '</div>'
                    result += '</div>'
                    break

        result += '</div>'
        result += '</div>'
        result += '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>'
        result += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>'
        result += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>'
        result += '<script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js"></script>'
        result += '<script>$(".carousel").slick();</script>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
