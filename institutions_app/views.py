from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages, admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from institution_project.settings import SESSION_COOKIE_DOMAIN

from institutions_app.forms import ProfileForm, RegisterForm
# from institutions_app.utils import set_cookie
# from forms import RegisterForm, ProfileForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.
def register_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.groups.add(Group.objects.filter(name="Usuario").first())
            user.save()
        else:
            messages.error(response, f'Hubo errores en el formulario de registros. Detalles: \n{form.error_messages}')
        return redirect("/admin")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        user = request.POST['username']
        passw = request.POST['password']
        access = authenticate(username=user, password=passw)
        if access is not None:
            if access.is_active:
                login(request, access)
                # admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True
                url_response = '/admin/'
                next = request.POST.get('next', None)
                url_response = next if next else url_response
                response = HttpResponseRedirect(url_response)
                # set_cookie(response, 'user', user)
                return response
            else:
                messages.error(request, "Usuario inactivo")
        else:
            modelUser = User.objects.filter(username=user)
            if modelUser.count() > 0 and modelUser.get().is_active == False:
                messages.error(request, "Usuario inactivo, confirme su email")
            else:
                messages.error(request, "Nombre de usuario y/o contraseña inválidos")
    return HttpResponseRedirect('/admin/login')


def logout_view(request):
    response = HttpResponseRedirect('/admin/')
    logout(request)
    # response.delete_cookie('user', domain=SESSION_COOKIE_DOMAIN)
    return response

class user_update(UpdateView):
    form_class = ProfileForm
    model = User
    success_url = reverse_lazy('admin:index')
    template_name = 'profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(User, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, "Usuario editado con éxito")
        return super(User, self).post(request, *args, **kwargs)
