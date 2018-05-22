from django.http import HttpResponse
from django.core.cache import cache
from django.shortcuts import redirect
import json
def show_vote(request):
    votes = cache.get("glosowanie")
    if votes is None:
        cache.set("glosowanie",'{"yes":0, "no": 0}', timeout=60)
        votes = cache.get("glosowanie")
    vote_object = json.loads(votes)
    return HttpResponse("""
    Vote yes: {}<br/>
    Vote no: {}<br/>
    Time left: {}<br/>
    Votes link: <br/><a href="/yes">yes</a> <br/> <a href="/no">no</a></br>
    Clean vote: <a href="/clean">Clean All</a>
    """.format(vote_object['yes'], vote_object['no'], cache.ttl("glosowanie")))

def yes_vote(request):
    votes = cache.get("glosowanie")
    if votes is None:
        cache.set("glosowanie",'{"yes":0, "no": 0}', timeout=60)
        votes = cache.get("glosowanie")
    vote_object = json.loads(votes)
    vote_object['yes']+=1
    cache.set("glosowanie", json.dumps(vote_object), timeout=cache.ttl("glosowanie")+10)
    return redirect('/')

def no_vote(request):
    votes = cache.get("glosowanie")
    if votes is None:
        cache.set("glosowanie",'{"yes":0, "no": 0}', timeout=60)
        votes = cache.get("glosowanie")
    vote_object = json.loads(votes)
    vote_object['no']+=1
    cache.set("glosowanie", json.dumps(vote_object), timeout=cache.ttl("glosowanie")+10)
    return redirect('/')

def clean_vote(request):
    cache.expire("glosowanie", timeout=0)
    return redirect('/')