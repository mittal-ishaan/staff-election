from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from .models import posts, candidates, booths

def email_check(user):
    return user.username.startwith('booth')

@user_passes_test(email_check, login_url="/login/")
def home(request):
    booth = booths.objects.get(name=request.user.username)
    if booth.submitted:
         return render(request, 'home.html', {'submitted': True}) 
    if request.method == 'POST':
        vote1 = request.POST.get('vote1')
        vote2 = request.POST.get('vote2')
        vote3 = request.POST.get('vote3')
        vote4 = request.POST.get('vote4')
        vote5 = request.POST.get('vote5')
        vote6 = request.POST.get('vote6')
        vote7 = request.POST.get('vote7')
        vote8 = request.POST.get('vote8')
        vote9 = request.POST.get('vote9')
        vote10 = request.POST.get('vote10')
        vote11 = request.POST.get('vote11')
        candidate1 = candidates.objects.get(name=vote1,posts__name="post1")
        candidate1.votes += 1
        candidate1.save()
        candidate2 = candidates.objects.get(name=vote2,posts__name="post1")
        candidate2.votes += 1
        candidate2.save()
        candidate3 = candidates.objects.get(name=vote3,posts__name="post1")
        candidate3.votes += 1
        candidate3.save()
        candidate4 = candidates.objects.get(name=vote4,posts__name="post1")
        candidate4.votes += 1
        candidate4.save()
        candidate5 = candidates.objects.get(name=vote5,posts__name="post1")
        candidate5.votes += 1
        candidate5.save()
        candidate6 = candidates.objects.get(name=vote6,posts__name="post1")
        candidate6.votes += 1
        candidate6.save()
        candidate7 = candidates.objects.get(name=vote7,posts__name="post1")
        candidate7.votes += 1
        candidate7.save()
        candidate8 = candidates.objects.get(name=vote8,posts__name="post1")
        candidate8.votes += 1
        candidate8.save()
        candidate9 = candidates.objects.get(name=vote9,posts__name="post2")
        candidate9.votes += 1
        candidate9.save()
        candidate10 = candidates.objects.get(name=vote10,posts__name="post2")
        candidate10.votes += 1
        candidate10.save()
        candidate11 = candidates.objects.get(name=vote11,posts__name="post2")
        candidate11.votes += 1
        candidate11.save()
        booth.submitted = True
        booth.save()
        return redirect(request, 'home.html', {'submitted': True})
    return render(request, 'home.html', {'posts': posts.objects.all(), 'candidates': candidates.objects.all()})
