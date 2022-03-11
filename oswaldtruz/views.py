from django.shortcuts import render
from accounts.models import UserProfile

from store.models import Product
from store.models import ReviewRating


def Home(request):
    products = Product.objects.all().filter(
        is_available=True).order_by('created_date')
    # profile = UserProfile.objects.get_or_create(user_id=request.user.id)[0]
    for product in products:
        reviews = ReviewRating.objects.filter(
            product_id=product.id, status=True)
    context = {
        'products': products,
        'reviews': reviews,
        # 'profile': profile
    }
    return render(request, 'home.html', context)


def About(request):
    return render(request, 'About.html')


def Contact(request):
    return render(request, 'Contact.html')
