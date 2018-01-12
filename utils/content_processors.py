from July import settings

def static_git(request):
    """
    Adds static-related context variables to the context.
    """
    return {'staticgit': settings.STATIC_GIT_URL }
