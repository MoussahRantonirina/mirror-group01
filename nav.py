def navbar():
    result = '<nav class="navbar navbar-expand-lg navbar-light bg-primary">'
    result += '<a class="col-3 navbar-brand" href="#">Music</a>'
    result += '</button>'
    result += '<div class="col-6 offset-2 collapse navbar-collapse text-center"  id="navbarNav">'
    result += '<ul class="navbar-nav">'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/">Accueil</a>'
    result += '</li>'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/liste">Classement</a>'
    result += '</li>'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/details">Detail</a>'
    result += '</li>'
    result += '</ul>'
    result += '</div>'
    result += '</nav>'
    return result