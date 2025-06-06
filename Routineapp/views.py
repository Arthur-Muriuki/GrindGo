from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('routine_list')
    else:
        form = RegisterForm()
    return render(request, 'routine/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine
from .forms import RoutineForm

@login_required
def routine_list(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'Routineapp/routine_list.html', {'routines': routines})

@login_required
def routine_create(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.save()
            return redirect('routine_list')
    else:
        form = RoutineForm()
    return render(request, 'Routineapp/routine_form.html', {'form': form})

@login_required
def routine_update(request, pk):
    routine = get_object_or_404(Routine, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RoutineForm(instance=routine)
    return render(request, 'Routineapp/routine_form.html', {'form': form})

@login_required
def routine_delete(request, pk):
    routine = get_object_or_404(Routine, pk=pk, user=request.user)
    if request.method == 'POST':
        routine.delete()
        return redirect('routine_list')
    return render(request, 'Routineapp/routine_confirm_delete.html', {'routine': routine})
