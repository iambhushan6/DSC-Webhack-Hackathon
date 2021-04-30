from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import(
    TemplateView,
    DetailView,
    View,
    CreateView,
    FormView,
    ListView,
)
from django.contrib.auth.models import User
from main import forms
from main import models
from main.models import Citizen,Vac_center
from django.views.generic.detail import SingleObjectMixin,BaseDetailView



# Create your views here.

class Homehtml(View):
        def get(self,request):
            return render(request,'main/home.html')
            
class Page2html(View):
        def get(self,request):
            return render(request,'main/page2.html')
class Page3html(View):
        def get(self,request):
            return render(request,'main/page3.html')


class Page4html(View):
        def get(self,request):
            return render(request,'main/page4.html')
 
class Vaccinecenter(CreateView):
    model = models.Vac_center
    template_name = 'main/vaccine_center.html'
    fields = '__all__'
    success_url = '/centers'

class Center(DetailView):
    model = models.Vac_center
    context_object_name = 'centers'
    template_name = 'main/centerdetail.html'

class Centerlist(ListView):
    model = models.Vac_center
    context_object_name = 'centers'
    template_name = 'main/centers.html'

def beneficiary(request):

    vaccinecenters = models.Vac_center.objects.all()
    context={
        'vaccinecenters' : vaccinecenters
    }

    if request.method == "POST":
        name = request.POST.get('name')
        mobno = request.POST.get('mobno')
        age = request.POST.get('age')
        state = request.POST.get('state')
        city = request.POST.get('city')
        center = request.POST.get('center')    
        date = request.POST.get('date')    
        timeslot = request.POST.get('timeslot')    

        citizen_detail = Citizen(
        name =      name, 
        mobno =     mobno, 
        age =       age, 
        state =     state, 
        city =      city, 
        center =    center, 
        centername = center,
        date =      date, 
        timeslot =  timeslot 
        )

        citizen_detail.save()


    return render(request,"main/beneficiary.html",context)



def token(request):
    tokens = models.Citizen.objects.all()

    citizen = tokens
    citizen = citizen[::-1]
    context={
        'tokens' : citizen
    }
    return render(request,'main/token.html',context)


    

 















# class Vaccinecenter(CreateView,FormView):

#     model = models.Vac_center
#     form_class = forms.Vac_centerform
#     template_name = 'main/vaccine_center.html'

#     def form_valid(self,form):
#         obj = form.save()
#         obj.citizen = self.get_object()
#         obj.save()
#         return HttpResponseRedirect('/')

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().post(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         context = self.get_context_data(object=self.object)
#         return self.render_to_response(context)
    


# class BaseDetailView(SingleObjectMixin, View):
#     """A base view for displaying a single object."""
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         context = self.get_context_data(object=self.object)
#         return self.render_to_response(context)
 