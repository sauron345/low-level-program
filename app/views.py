from django.shortcuts import render


def control_panel(request):
    return render(request, 'control-panel.html', {})
