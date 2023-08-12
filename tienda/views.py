from django.shortcuts import render
from tienda.models import Orden

def v_index(request):

    fecha_inicio = request.GET.get("fecha_inicio",None)
    fecha_fin = request.GET.get("fecha_fin",None)

    fecha_e_inicio = request.GET.get("fecha_e_inicio",None)
    fecha_e_fin = request.GET.get("fecha_e_fin",None)
    
    consulta = Orden.objects.all()


    context = {
        "ordenes": consulta
    }

    return render(request, "index.html",context)