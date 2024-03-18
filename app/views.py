from django.shortcuts import render
# Importing view class from django.views
from django.views import View 

# Importing all models from app/models.py
from .models import*

class IndexView(View):
    # Defining get method
    def get(self, request):
        
        return render (request, 'index.html')
      # Defining post method
    def post(self, request):
        pass

# Index View
class CidadeView(View):
    # Defining get method
    def get(self, request):
        cidade = Cidade.objects.all()
        return render (request, 'cidade.html', {'cidade': cidade})
      # Defining post method
    def post(self, request):
        pass

# Index View
class GeneroView(View):
    # Defining get method
    def get(self, request):
        genero = Genero.objects.all()
        return render (request, 'genero.html', {'genero': genero})
      # Defining post method
    def post(self, request):
        pass

# Index View
class UsuarioView(View):
    # Defining get method
    def get(self, request):
        usuario= Usuario.objects.all()
        return render (request, 'usuario.html', {'usuario': usuario})
      # Defining post method
    def post(self, request):
        pass

# Index View
class AutorView(View):
    # Defining get method
    def get(self, request):
        autor = Autor.objects.all()
        return render (request, 'autor.html', {'autor': autor})
      # Defining post method
    def post(self, request):
        pass

# Index View
class EditoraView(View):
    # Defining get method
    def get(self, request):
        editora = Editora.objects.all()
        return render (request, 'editora.html', {'editora': editora})
      # Defining post method
    def post(self, request):
        pass

# Index View
class LivroView(View):
    # Defining get method
    def get(self, request):
        livro = Livro.objects.all()
        return render (request, 'livro.html', {'livro': livro})
      # Defining post method
    def post(self, request):
        pass

# Index View
class EmprestimoView(View):
    # Defining get method
    def get(self, request):
        emprestimo = Emprestimo.objects.all()
        return render (request, 'emprestimo.html', {'emprestimo': emprestimo})
      # Defining post method
    def post(self, request):
        pass

# Create your views here.