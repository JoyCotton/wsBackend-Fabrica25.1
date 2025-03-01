from django.shortcuts import get_object_or_404, redirect, render
from .models import Personagem
import requests

def CatarPersonagens(request):
    response = requests.get('https://rickandmortyapi.com/api/character')
    data = response.json()
    characters = data['results']
    for char in characters:
        Personagem.objects.update_or_create(
            name=char['name'],
            defaults={
                'status': char['status'],
                'species': char['species'],
                'gender': char['gender'],
                'image': char['image']
            }
        )
    return redirect('personagem_lista')

def PersonagemLista(request):
    characters = Personagem.objects.all()
    return render(request, 'RaM/personagemLista.html', {'characters': characters})

def PersonagemDetalhe(request, pk):
    character = get_object_or_404(Personagem, pk=pk)
    return render(request, 'RaM/personagemDetalhe.html', {'character': character})

def PersonagemCriar(request):
    if request.method == 'POST':
        name = request.POST['name']
        status = request.POST['status']
        species = request.POST['species']
        gender = request.POST['gender']
        image = request.POST['image']
        Personagem.objects.create(name=name, status=status, species=species, gender=gender, image=image)
        return redirect('personagem_lista')
    return render(request, 'RaM/personagemForm.html')

def PersonagemUpdate(request, pk):
    character = get_object_or_404(Personagem, pk=pk)
    if request.method == 'POST':
        character.name = request.POST['name']
        character.status = request.POST['status']
        character.species = request.POST['species']
        character.gender = request.POST['gender']
        character.image = request.POST['image']
        character.save()
        return redirect('personagem_lista')
    return render(request, 'RaM/personagemForm.html', {'character': character})

def PersonagemDeletar(request, pk):
    character = get_object_or_404(Personagem, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('personagem_lista')
    return render(request, 'RaM/personagemConfirmarDelecao.html', {'character': character})