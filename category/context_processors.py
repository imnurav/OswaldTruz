from .models import Category


def menu_links(request):
    links = Category.objects.all()
    # print("Categories are : ", links)
    return dict(links=links)
