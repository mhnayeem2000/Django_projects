from django.shortcuts import render
# Create your views here.

def home(request):

    data = [
    {
        "title": "Top 10 important tips on IT services & design",
        "category" : "Technology",
        "img" : "/static/blog-1.jpg",
        
    },
    {
        "title": "How our company works in different ways",
        "category" : "Design",
        "img" : "/static/blog-2.jpg",
    },
    {
        "title": "How is technology working with new things?",
        "category" : "Artificial",
        "img" : "/static/blog-3.jpg",
    }
    ]

    return render(request, 'myapp/home.html' , {"data" : data})