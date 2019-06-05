from django.shortcuts import render

from .models import Mineral


def minerals_index(request):
    """Get all minerals to display on main page"""
    minerals = Mineral.objects.order_by('name').all()
    context = {
        'minerals':minerals
    }
    # context dictionary sent to template
    return render(request, 'minerals_index.html', context)

def mineral_detail(request, pk):
    """Get details of each mineral"""
    mineral = Mineral.objects.get(pk=pk)
    context = {
        'mineral': mineral
    }
    return render(request, 'mineral_detail.html', context)
