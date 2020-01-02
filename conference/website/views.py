from django.shortcuts import render
from .models import BannerImage, Counter, Join, DetailOfConferernce, SideImage, ConferenceDay, ConferenceSchedule, Gallery, HappyClients, Pricing, AboutCounter, Speakers, BlogSingle, Comment, Contact
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['detail_of_conference'] = DetailOfConferernce.objects.all()
        context['side_image'] = SideImage.objects.last()
        context['conference_day'] = ConferenceDay.objects.all()
        context['conference_schedule'] =ConferenceSchedule.objects.all()
        context['gallery']= Gallery.objects.all()
        context['happy_clients'] = HappyClients.objects.all()
        context['pricing']= Pricing.objects.all()
        context['blog_single'] = BlogSingle.objects.all()
        

        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['side_image'] = SideImage.objects.last()
        context['about_counter'] = AboutCounter.objects.last()
        context['gallery'] = Gallery.objects.all()
        context['happy_clients'] = HappyClients.objects.all()


        return context


def speakers(request):
    return render(request, "speakers.html") 

class ScheduleView(TemplateView):
    template_name = 'schedule.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['conference_day'] = ConferenceDay.objects.all()
        context['conference_schedule'] =ConferenceSchedule.objects.all()

        return context





class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context= super(BlogView, self).get_context_data(**kwargs)
        context['blog_single'] = BlogSingle.objects.all()

        return context

class BlogSingleView(TemplateView):
    template_name = 'blogSingle.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogSingleView,self).get_context_data(**kwargs)
        context['blog_single'] = BlogSingle.objects.get(id=kwargs.get('pk'))
        context['comment'] = Comment.objects.all()

        return context

def commentview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        blog = BlogSingle.objects.get(pk=kwargs.get('pk'))
        Comment.objects.create(name=name, email=email, message=message, )
        print(kwargs.get('pk'))
        

        return HttpResponseRedirect('/blog/'+ str(kwargs.get('pk')))
    else:
        banner_image = BannerImage.objects.last()
        return render(request,'blogSingle.html',{'banner_image':banner_image})


def contactview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        return HttpResponseRedirect('/')
    else:
        banner_image = BannerImage.objects.last()
        return render(request, 'contact.html', {'banner_image': banner_image}) 

def joinview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email= request.POST.get("email")
        phone = request.POST.get("phone")
        Join.objects.create(name=name, phone=phone, email= email)

        return HttpResponseRedirect('/')
    else:
        banner_image = BannerImage.objects.last()
        return render(request, 'index.html', {'banner_image':banner_image})