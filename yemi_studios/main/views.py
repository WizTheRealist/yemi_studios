from django.shortcuts import render
from .models import GalleryImage, Service, Category, Testimonial

def home(request):
    featured_images = GalleryImage.objects.filter(is_featured=True)[:6]
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()[:3]
    context = {
        'featured_images': featured_images,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def gallery(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_slug:
        images = GalleryImage.objects.filter(category__slug=category_slug)
        active_category = Category.objects.get(slug=category_slug)
    else:
        images = GalleryImage.objects.all()
        active_category = None
    
    context = {
        'images': images,
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'gallery.html', context)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')
