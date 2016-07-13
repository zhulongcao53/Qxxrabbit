from django.shortcuts import render,render_to_response  
from django.http import HttpResponse  
from django.template import loader, Context  
from blog.models import BlogPost  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.  
  
#def archive(request):  
#    if request.method == "GET":
#        data = request.GET.get('id', 0)
#        if data == 0:
#            posts = BlogPost.objects.all()  
#            t = loader.get_template('archive.html')  
#            c = Context({'posts':posts})  
#            return HttpResponse(t.render(c)) 
#        else:  
#            posts = BlogPost.objects.filter(id = data)
#            t = loader.get_template('page.html')  
#            c = Context({'posts':posts}) 
#            return HttpResponse(t.render(c))

def archive(request):
    if request.method == "GET":
        data = request.GET.get('id', 0)
        if data == 0:   
            posts = BlogPost.objects.all()
            paginator = JuncheePaginator(posts, 8)
            page = request.GET.get('page')
            try :
                post_list = paginator.page(page)
            except PageNotAnInteger :
                post_list = paginator.page(1)
            except EmptyPage :
                post_list = paginator.paginator(paginator.num_pages)
            return render(request, 'archive.html', {'post_list' : post_list})
        else:
            posts = BlogPost.objects.filter(id = data)
            return render(request, 'page.html', {'posts' : posts})
            #t = loader.get_template('page.html')
            #c = Context({'posts':posts})
            #return HttpResponse(t.render(c))

def customConfig(request):
    params = request.GET
    if params['action'] == 'uploadimage':
        return ueditor_ImgUp(request)
    return HttpResponse(json.dumps(config))

def search_tag(request, tag):
    try:
        post_list = BlogPost.objects.filter(category = tag)
        print post_list
    except BlogPost.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'archive.html')
        else:
            post_list = BlogPost.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

def archives(request):
    try:
        post_list = BlogPost.objects.all()
    except BlogPost.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

class JuncheePaginator(Paginator):
      def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
          Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
          self.range_num = range_num
  
      def page(self, number):
          self.page_num = number
          return super(JuncheePaginator, self).page(number)
 
      def _page_range_ext(self):
          num_count = 2 * self.range_num + 1
          if self.num_pages <= num_count:
              return range(1, self.num_pages + 1)
          num_list = []
          num_list.append(self.page_num)
          for i in range(1, self.range_num + 1):
              if self.page_num - i <= 0:
                  num_list.append(num_count + self.page_num - i)
              else:
                  num_list.append(self.page_num - i)
 
              if self.page_num + i <= self.num_pages:
                  num_list.append(self.page_num + i)
              else:
                  num_list.append(self.page_num + i - num_count)
          num_list.sort()
          return num_list
      page_range_ext = property(_page_range_ext)

