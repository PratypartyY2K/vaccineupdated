from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserAttributeForm,HospitalForm
from .models import User_Attributes,Hospital,Request
from django.views.generic import FormView,TemplateView
from django.views import View
from django.contrib import messages
import datetime



def home(request):
    return render(request,'app/home.html')
class Enrollment(View):
    def post(self,request):
        form = UserAttributeForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = self.request.user.id
            newform.date = datetime.datetime.now()
            newform.details_filled = 1
            newform.save()
            if(newform.age>50):
                return redirect('book')
            else:
                return redirect('phase2')
        return render(request, 'app/enrollment.html', {'form': form})
    def get(self,request):
        form=UserAttributeForm()
        return render(request,'app/enrollment.html',{'form':form})
class HospitalPageView(FormView):
    template_name = 'app/book.html'
    form_class = HospitalForm

    def get_context_data(self, **kwargs):
        context = super(HospitalPageView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['hospitals'] = Hospital.objects.all()
        return context
    def form_valid(self, form):
        request = self.request
        user = self.request.user.id
        hospital = form.cleaned_data['hospital']
        fulfilled = 0
        pref_hospital = Hospital.objects.filter(id=hospital)[0]
        confirmtime = "NA"
        if pref_hospital.available_Vaccine  > 0:

            pref_hospital.available_Vaccine -= 1
            pref_hospital.save()
            fulfilled = 1
            confirmtime = (pref_hospital.total_Vaccine-pref_hospital.available_Vaccine)*0.5+9
        Request.objects.create_data(user, hospital,fulfilled, confirmtime)
        messages.success(
            request, ('Your request for bed has been confirmed.'))

        return redirect('final')
class Final(TemplateView):
    template_name = 'app/final.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['filled_form'] = User_Attributes.objects.filter(user=context['user'].id)[0]
        context['booked_hospital'] = Request.objects.filter(user=context['user'].id)[0]
        context['hospital'] = Hospital.objects.filter(id=context['booked_hospital'].hospital)[0]
        return context
def phase2(request):
    return render(request,'app/phase2.html')