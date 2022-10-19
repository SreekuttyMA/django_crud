from django.shortcuts import render,redirect
from .forms import BookCreate
from django.http import HttpResponse
from .models import Book
# Create your views here.
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('display')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'display'}}">reload</a>""")
    else:
        return render(request, './upload_form.html', {'upload_form':upload})
    
    
def display(request):
    shelf = Book.objects.all()
    return render(request, './library.html', {'shelf': shelf})



def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('display')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('display')
    return render(request, './upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('display')
    book_sel.delete()
    return redirect('display')