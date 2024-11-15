from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page requested")
    friends = ['riti', 'shantanu', 'saloni']
    return JsonResponse(friends, safe=False)
