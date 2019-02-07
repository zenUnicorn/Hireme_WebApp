from django.shortcuts import render,get_object_or_404
from hireme.form import UserForm,UserProfileInfoForm
from hireme.models import UserProfileInfo
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(TemplateView):
    template_name = 'hireme/index.html'

# class UserListView(ListView):
#     template_name = 'hireme/developers.html'
#     model = UserProfileInfo

#     def get_queryset(self):
#         return UserProfileInfo.objects.order_by('user_id')

# def developers(request):
#     webpage_list = UserProfileInfo.objects.order_by('user_id')
#     date_dict = {'access_records': webpage_list}
#     return render(request,'hireme/developers.html', context=date_dict)
class developersView(ListView):
    model = UserProfileInfo
    #template_name = 'hireme/developers.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return UserProfileInfo.objects.all()

class UserDetailView(DetailView):
    context_object_name = 'user_detail'
    model = UserProfileInfo
    template_name = 'hireme/detail.html'
    
    


def register(request):
    
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
    
        #to check if both form are valid
        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.save()
            #commit is false bcos we dnt want errors of collision when we send to database
            profile = profile_form.save(commit=False)
            #its defining the onetooneuser = models.OneToOneField(User) in models.py
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'hireme/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})