from django.shortcuts import render


def get_bootstrap(request):
    # return render(request, 'exemplos/01_hello_world.html')
    return render(request, 'exemplos/02_containers.html')