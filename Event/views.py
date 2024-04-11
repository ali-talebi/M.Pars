from django.shortcuts import render , redirect
from .models import Event_Information , Event_Comment
from django.views import View
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import  method_decorator
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
# Create your views here.


class EventListView(View) :
    template_name = 'Event/event-list-1.html'

    def setup(self, request, *args, **kwargs):
        self.total_event = Event_Information.objects.all()

        try :
            self.paginator = Paginator(self.total_event , 9 )
            self.sent_events = self.paginator.page(kwargs['page'])

        except PageNotAnInteger:
            self.sent_events = self.paginator.page(self.paginator.num_pages)

        except EmptyPage:
            self.sent_events = self.paginator.page(1)


        return super().setup(request, *args, **kwargs)



    def get(self, request , page=1) :



        content = {'total_event': self.sent_events}
        return render(request, self.template_name, content)

    def post(self , request , page = 1 ) :
        print( "***"*20 , self.sent_events)

        content = {'total_event': self.sent_events}
        return render(request, self.template_name, content)



class Event_DetailView(View):

    template_name = 'Event/event-single.html'
    form = EventForm

    def setup(self, request, *args, **kwargs):
        self.event = Event_Information.objects.get(id = kwargs['id'])
        self.comments = Event_Comment.objects.filter(event = self.event)
        return super().setup(request, *args, **kwargs)

    def get(self , request , id ) :
        content = {'event':self.event , 'form':self.form() }
        return render(request , self.template_name , content)
    @method_decorator(login_required)
    def post(self , request , id ) :

        form = self.form(request.POST )
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.event  = self.event
            new_form.Person = request.user
            new_form.save()


            messages.success(request, 'کامنت شما با موفقیت ثبت شد' , 'success')
            return redirect('Event:Event_Detail' , id )


        else :
            messages.error(request , "در ثبت کامنت شما مشکلی داریم" , 'error' )


        content = {'event':self.event  , 'form':self.form}
        return render(request , self.template_name , content)


