from django.shortcuts import render , redirect ,get_object_or_404
from .models import Note
# Create your views here.
# def addnote(reuquets):
def home(request):
    nts = Note.objects.all()
    return render(request , "index.html" , {"nts" : nts })

def addNote(request):
    if request.method == 'POST':
        note_txt = request.POST["note_txt"]
        color = request.POST["color"]
        note = Note()
        note.note_txt=note_txt
        note.color = color
        note.save()
    
    return redirect('home')

def editNote(request):
    if request.method == 'POST':
        note = request.POST["note_txt"]
        color = request.POST["color"]
        note.save()
    
    return redirect('home')


def delNote(request):
    if request.method == 'POST':
        note_id = request.POST["note_id"]
        db_note = Note.objects.filter(id = note_id )[0]
        # print(db_note)
        db_note.delete()
    
    return redirect('home')

def expandNote(request):
    if request.method == 'POST':
        note_id = request.POST["note_id"]
        db_note = Note.objects.filter(id = note_id )[0]

        return render(request , "expand.html" , {"db_note" : db_note})
    else:
        return redirect("home")


def editNote(request):
    if request.method == 'POST':
        note_id = request.POST["note_id"]
        db_note = Note.objects.filter(id = note_id )[0]

        return render(request , "edit.html" , {"db_note" : db_note})
    else:
        return redirect("home")

def saveNote(request):
    if request.method == 'POST':
        note_id = request.POST["note_id"]
        db_note = Note.objects.filter(id = note_id )[0]
        note_txt = request.POST["note_txt"]
        db_note.note_txt = note_txt
        db_note.save()
    return redirect("home")
        