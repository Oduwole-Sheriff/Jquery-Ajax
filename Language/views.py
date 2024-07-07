from django.shortcuts import render, redirect
from .forms import EntryCreationForm
from django.http import JsonResponse
from .models import Entry, Language

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def language(request):
    form = EntryCreationForm(instance=Entry.objects.first())

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        term = request.GET.get('term')  # Get the search term from the GET parameters
        languages = Language.objects.filter(title__icontains=term)  # Filter using icontains
        response_content = list(languages.values())  # Convert queryset to a list of dictionaries
        return JsonResponse(response_content, safe=False)  # Return JSON response

    if request.method == 'POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        if form.is_valid():
            form.save()
            return redirect('language')
    return render(request, 'Language/language.html', {'form': form})

    
