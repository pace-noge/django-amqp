from django.http import HttpResponse
from anyjson import serialize
from celerytest import tasks

def multiply(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    result = tasks.multiply.delay(x,y)
    #result = x * y
    result = result.get()
    response = {'status': 'success', 'retval': result}
    return HttpResponse(serialize(response), mimetype='application/json')

