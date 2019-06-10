from django.shortcuts import render, get_object_or_404

from .models import Mineral


def index(request):
    """Get all minerals to display on main page"""
    minerals = Mineral.objects.order_by('name').all()
    # 'minerals' is a dictionary sent to template
    return render(request, 'index.html', {'minerals':minerals})

def mineral_details(request, pk):
    """Get details of each mineral"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'mineral_details.html', {'mineral':mineral})
