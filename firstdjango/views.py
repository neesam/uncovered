from django.shortcuts import render, HttpResponse, redirect
import random
from django.http import JsonResponse
from firstdjango.models import Users, Brookfield, Sundial, Albums, Tracks, RYM, RandAlbum, Artist, Ryan, RandomArtist, RandPerson, GreatScene, Jazz, Log, Vinyls, SMS, MLEP, UTSTMS, MELA, RYMRecs, RYMChallenge, Criterion, melodicEng, Records

def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'info.html', context)

def createUser(request):

    Users.objects.create(name=request.POST['name'], age=request.POST['age'])
    return redirect('/')

def sundial(request):

    context = {
        'sundial': Sundial.objects.all().order_by('?')
    }
    return render(request, 'sundial.html', context)

def brookfield(request):
    context = {
        'brookfield': Brookfield.objects.all().order_by('?')
    }

    return render(request, 'brookfield.html', context)

def album(request, name):

    context = {
        'albums': Albums.objects.get(name=name),
        'tracks': Tracks.objects.filter(album=name),
        'brookfield': Brookfield.objects.all()

    }
    return render(request, 'album.html', context)

def magicSheet(request):

    context = {
        'album': RYM.objects.all().order_by('?').first(),
    }

    return render(request, 'magic_sheet.html', context)

def randomAlbum(request):

    context = {
        'artist': RandAlbum.objects.all().order_by('?').first()
    }

    return render(request, 'random_album.html', context)

def ryan(request):
    
    context = {
        'album': Ryan.objects.all().order_by('?').first()
    }

    return render(request, 'random_ryan.html', context)

def randomArtist(request):

    context = {
        'artist': RandomArtist.objects.all().order_by('?').first()
    }

    return render(request, 'random_artist.html', context)

def randomPersonTop(request):
    
        context = {
            'album': RandPerson.objects.all().order_by('?').first()
        }
    
        return render(request, 'random_person_top.html', context)

def greatScene(request):
    
        context = {
            'album': GreatScene.objects.all().order_by('?').first()
        }
    
        return render(request, 'great_scene.html', context)

def jazz(request):
    
        context = {
            'album': Jazz.objects.all().order_by('?').first()
        }
    
        return render(request, 'jazz.html', context)

def login(request):
    
    return render(request, 'login.html')

def listeningLog(request):

    context = {
        'albums': Log.objects.all().order_by('-created_at')
    }

    return render(request, 'listening_log.html', context)

def addListeningLog(request):
    
    return render(request, 'add_listening_log.html')

def addToLog(request):

    Log.objects.create(album=request.POST['album'], artist=request.POST['artist'], image=request.POST['image'], rating=request.POST['rating'])

    return redirect('/listening-log')

def charts(request):

    return render(request, 'charts.html')

def sms(request):

    context = {
        'album': SMS.objects.all().order_by('?').first()
    }

    return render(request, 'SMS.html', context)

def mlep(request):

    context = {
        'album': MLEP.objects.all().order_by('?').first()
    }

    return render(request, 'MLEP.html', context)

def utstms(request):
    
    context = {
        'album': UTSTMS.objects.all().order_by('?').first()
    }

    return render(request, 'UTSTMS.html', context)

def mela(request):
    
    context = {
        'album': MELA.objects.all().order_by('?').first()
    }

    return render(request, 'MELA.html', context)

def rymrecs(request):
    
    context = {
        'album': RYMRecs.objects.all().order_by('?').first()
    }

    return render(request, 'RYMRecs.html', context)

def rymchallenge(request):
    
    context = {
        'album': RYMChallenge.objects.all().order_by('?').first()
    }

    return render(request, 'RYMChallenge.html', context)

def recs(request):
    
    return render(request, 'recs.html')

def criterion(request):
    
        context = {
            'title': Criterion.objects.all().order_by('?').first()
        }
    
        return render(request, 'criterion.html', context)

def melEng(request):
    
    context = {
        'album': melodicEng.objects.all().order_by('?').first()
    }

    return render(request, 'melodicEng.html', context)

def records(request):

    context = {
        'album': Records.objects.all().order_by('?').first()
    }

    return render(request, 'records.html', context)

def friends(request):

    return render(request, 'friends.html')