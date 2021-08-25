from django.shortcuts import render,redirect,HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views import View
from .form import LoginForm,ProfileForm,NewsUploads
from .models import Profile,NewsAndUpdates,UniversityCatalogue
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from tablib import Dataset
# from resource import UniCatalogueAdmin

def index(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                msg = messages.error(request, "Invalid username or password.")
                return redirect("userdash", {'msg': msg})
            else:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("userdash")
    form = LoginForm()
    return render(request, 'index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registered successfully")
            return redirect("login")
    # messages.error(request, "Invalid Username or Password")
    form = RegisterForm()
    return render(request, 'register.html', {
        'form': form
    })
class Catalogue(View):
    def get(self, request):
        newsUpload = NewsUploads()
        catalogue = NewsAndUpdates()
        return render(request, 'catalogue.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class AdminDash(View):
    def get(self, request):
        newsform = NewsUploads()
        catalogues = get_list_or_404(UniversityCatalogue)
        docTitle = get_list_or_404(NewsAndUpdates)
        # form = InvoiceDocument()
        # invModel = InvDoc.objects.all()
        # # total amount within each document
        # total_amount = invModel.aggregate(Sum('amount')).get('amount__sum')
        # # Count Invoices in the objects
        # countInvoice = InvDoc.objects.count()
        # regNumber = "INV" + uuid.uuid4().hex[:6].upper()
        context = {'newsform': newsform,'catalogue':catalogues,'docTitle':docTitle }
        return render(request, 'userdash.html',context)

    def post(self, request):
        if request.method == 'POST':
            form = NewsUploads(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                msg = messages.success(request,'A new Document Inserted')
                return redirect('userdash')
            else:
                newsform = NewsUploads()
                msg = messages.success(request, 'Faied to insert Document')
            context = {'newsform': newsform,'messages':msg }
            return render(request, 'userdash.html', context)

    def file_upload(self, request):
        if request.method == 'POST':
                form = ProgrammeRequirement(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    msg = messages.success(request, 'A new Document Inserted')
                    return redirect('userdash')
                else:
                    newsform = NewsUploads()
                    msg = messages.success(request, 'Faied to insert Document')
                context = {'newsform': newsform, 'messages': msg}
                return render(request, 'userdash.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None
    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ProfileForm()
        context = {'profile': self.profile, 'pform': form}
        return render(request, 'user_profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)
        if form.is_valid():
            profiles = form.save()
            # to save user model info
            profiles.user.first_name = form.cleaned_data.get('first_name')
            profiles.user.last_name = form.cleaned_data.get('last_name')
            profiles.user.email = form.cleaned_data.get('email')
            profiles.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))

        return redirect('profile')
