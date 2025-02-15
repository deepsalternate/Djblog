from.models import Category
from aaboutus.models import sociallink

def get_Categories(request):
    categories=Category.objects.all()
    # return dict(categories=categories)
    return {'categories':categories} 
       
def get_sociallinks(request):
    sociallinks=sociallink.objects.all()
    return {'sociallinks':sociallinks}