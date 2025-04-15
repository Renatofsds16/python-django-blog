from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post,Page
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView,DetailView


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    ordering = '-pk'
    paginate_by = 9
    queryset = Post.objects.get_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'page_title':'Home'})
        return context


#def index(request):
    #posts = Post.objects.get_published()
    #paginator = Paginator(posts,9)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #return render(request,'blog/pages/index.html',{'page_obj': page_obj,'page_title':'Home'})
class CreatedByListView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id')
        user = User.objects.filter(pk=id_user).first()
        
        if user is None:
            raise Http404()
        user_full_name = user.username
        if user.first_name:
            user_full_name = f'{user.first_name} {user.last_name}'
            context.update({'page_title':user_full_name})
        return context
    
    def get_queryset(self):
        qs =  super().get_queryset()
        qs.filter(created_by__pk=self.kwargs.get('id'))
        return qs

#def created_by(request,id):
#    user = User.objects.filter(pk=id).first()
#    if user is None:
#        raise Http404()
#    user_full_name = user.username
#    if user.first_name:
#       user_full_name = f'{user.first_name} {user.last_name}'
#   posts = Post.objects.get_published().filter(created_by__pk=id)
#    paginator = Paginator(posts,9)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    return render(request,'blog/pages/index.html',{'page_obj': page_obj,'page_title':user_full_name})
class PostDatailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    slug_field = 'slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.get_object()
        page_title = f'{post.title} - pagina -'
        context.update({'page_title':page_title})
        return context
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


#def post(request,slug):
#    post_obj = Post.objects.get_published().filter(slug=slug).first()
#    if post_obj is None:
#        Http404()

#    page_title = f'{post_obj.title}'
#    return render(request,'blog/pages/post.html',{'post': post_obj,'page_title': page_title})

class PageDatailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        page = self.get_object()
        page_title = f'{page.title} - pagina -'
        context.update({'page_title':page_title})
        return context
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)
#def page(request,slug):
#    page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()
#    if page_obj is None:
#        Http404()

#    page_title = f'{page_obj.title}'
#    return render(request,'blog/pages/page.html',{'page':page_obj,'page_title':page_title})


class CategoryListView(PostListView):
    allow_empty = False
    def get_queryset(self):
        return super().get_queryset().filter(category__slug=self.kwargs.get('slug'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = f'{self.object_list[0].category.name}'
        context.update({'page_title':page_title})
        return context

#def category(request,slug):
#    posts = Post.objects.get_published().filter(category__slug=slug)
#    paginator = Paginator(posts,9)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    if len(posts) == 0:
#        raise Http404()
    
#    page_title = f'{page_obj[0].category.name}'
#    return render(request,'blog/pages/index.html',{'page_obj': page_obj,'page_title':page_title})

class TagListView(PostListView):
    allow_empty = False
    def get_queryset(self):
        return super().get_queryset().filter(tags__slug=self.kwargs.get('slug'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = f'{self.object_list[0].tags.first().name}'
        context.update({'page_title':page_title})
        return context

#def tag(request,slug):
#    posts = Post.objects.get_published().filter(tags__slug=slug)
#    paginator = Paginator(posts,9)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    if len(posts) == 0:
#        raise Http404()
    
#    page_title = f'{page_obj[0].tags.first().name}'
#    return render(request,'blog/pages/index.html',{'page_obj': page_obj,'page_title':page_title})
class SearchListView(PostListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._search_value = ''
    
    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('search','').strip()
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset().filter(
            Q(title__icontains=self._search_value) | Q(content__icontains=self._search_value)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = f'{self._search_value[:10]} - search'
        context.update({'search_value':self._search_value,'page_title':page_title})
        return context
    
    def get(self, request, *args, **kwargs):
        #if self._search_value == '':
        #    return 
        return super().get(request, *args, **kwargs)

#def search(request):
#    search_value = request.GET.get('search','').strip()
#    posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(content__icontains=search_value))
#    paginator = Paginator(posts,9)
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    if len(posts) == 0:
#        raise Http404()
    
#    page_title = f'{search_value[:10]} - search'
#    return render(request,'blog/pages/index.html',{'page_obj': page_obj,'search_value':search_value,'page_title':page_title})