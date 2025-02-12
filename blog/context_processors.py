from.models import Category

def get_Categories(request):
    categories=Category.objects.all()
    # return dict(categories=categories)
    return {'categories':categories} 
       
