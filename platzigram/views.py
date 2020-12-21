""" views """
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
    return HttpResponse('The time is: {now}'.format(
        now=datetime.now().strftime('%b %d, %Y, %H:%M')
        ))
def hi (request):
    nums = request.GET.get('numbers')
    if nums == None:
        return HttpResponse("no numbers variable")
    nums = sorted( [int(i) for i in nums.split(',')])
    data = {
        'status': 'ok',
        'data': nums
    }
    print(nums)
    return JsonResponse(data,safe = False)