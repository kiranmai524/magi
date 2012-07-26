from pygithub3.services.repos import Commits
from django import template

register = template.Library()

@register.inclusion_tag('commits.html')
def get_list_of_commits(repo, user):
    try:
        repo_commit = Commits(user=user, repo=repo)
        commit_list = repo_commit.list(sha='master', path=None).all()
    except:
        commit_list = []
    context = {'commit_list':commit_list}
    return context
        
