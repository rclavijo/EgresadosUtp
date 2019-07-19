from django.shortcuts import get_object_or_404,  render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Usuarios.models import Profile, Follower, User
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, User__username=self.kwargs['username'])
      

def agregar(request,  profile):
    profile = Profile.objects.filter(pk=profile)
    if profile.count() != 0 :
        follower = Follower.objects.create(
        user= request.user.profile,
        account=profile[0]
         )
        follower.save()
        return redirect('profiles:detail', profile[0].User)
    else:
        return  redirect('profiles:list')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     profile = Profile.objects.get(user=user)
    #     context['following'] = Follower.objects.filter(user=self.request.user.profile, account=profile).count() != 0
    #     return context    

def eliminar(request, user):
    profile = Profile.objects.filter(pk=user)
    if profile.count() != 0:
        follower = Follower.objects.filter(
               user=request.user.profile,
               account=profile[0]
               )
        if follower.count() != 0:
            follower[0].delete()
        return redirect('profiles:detail', profile[0].User)
    else:
        return  redirect('profiles:list')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     profile = Profile.objects.get(user=user)
    #     context['following'] = Follower.objects.filter(user=self.request.user.profile, account=profile).count() != 0 
    #     return context      
  
