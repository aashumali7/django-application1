from django.http import HttpResponse

def index(request):
    return HttpResponse("<b>Hello, this is our website</b> ")

def intId(request,id):
    return HttpResponse(id)

def stringId(request,id):
    return HttpResponse(id)

def slugId(request,id):
    return HttpResponse(id)

def courseId(request,courseid):
    return HttpResponse(courseid)