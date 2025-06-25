from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

# def home(request):
#     return render(request,'home.html',{})
# Example view



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name="article.html"
    

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'  # create this template
    fields = ['title', 'author', 'comment']  # adjust fields as needed
    success_url = reverse_lazy('home')  # redirect after successful post
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ['title', 'comment']
    success_url = reverse_lazy('home') 
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


