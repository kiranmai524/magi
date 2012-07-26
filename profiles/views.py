from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from pygithub3 import Github

def login(request):

    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)
        
    if request.method == 'POST':

        gh = Github(login=request.POST['username'], password=request.POST['password'])

        number_of_followers = len(gh.users.followers.list().all())
        
        user_repos = gh.repos.list().all()
        number_of_user_repos = len(user_repos)
        user_org = gh.orgs.list().all()
        
        c = {'user_repos':user_repos,
                'user_name':request.POST['username'],
                'number_of_followers':number_of_followers,
                'number_of_user_repos':number_of_user_repos,
                'user_org':user_org,}
                
        return render_to_response('home.html', c)

