from django.shortcuts import render

posts = [
    {
        'titulo' : 'revision 1',
        'autor' : 'Alex',
        'fecha' : '10 de enero de 2020',
        'contenido' : 'Primer contenido'
    },
    {
        'titulo' : 'revision 2',
        'autor' : 'Alex',
        'fecha' : '12 de enero de 2020',
        'contenido' : 'segundo contenido'
    },
    {
        'titulo' : 'revision 3',
        'autor' : 'Alex',
        'fecha' : '10 de enero de 2020',
        'contenido' : 'Primer contenido'
    },
    {
        'titulo' : 'revision 4',
        'autor' : 'Alex',
        'fecha' : '12 de enero de 2020',
        'contenido' : 'segundo contenido'
    }
]

def home (request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def services (request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/services.html', context)

def about (request):
    
    return render(request, 'blog/about.html', {'title' : 'about'})

def quotes (request):
    
    return render(request, 'blog/quotes.html', {'title' : 'quotes'})

def contact (request):
    
    return render(request, 'blog/contact.html', {'title' : 'contact'})

def login (request):
    
    return render(request, 'blog/login.html', {'title' : 'login'})

def calculator (request):
    
    return render(request, 'blog/calculator.html', {'title' : 'calculator'})