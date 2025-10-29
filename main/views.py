from django.shortcuts import render
from .models import GalleryImage, Service, Category, Testimonial

def home(request):
    featured_images = GalleryImage.objects.filter(is_featured=True)[:6]
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()[:3]

    # Default services with category slugs if no services in database
    default_services = [
        {
            'name': 'Human Hair & Wigs',
            'description': 'Premium quality human hair and custom wig installations',
            'icon': 'fas fa-cut',
            'category_slug': 'wigs'
        },
        {
            'name': 'Nails & Pedicure',
            'description': 'Professional nail care and stunning nail art designs',
            'icon': 'fas fa-hand-sparkles',
            'category_slug': 'nails'
        },
        {
            'name': 'Lashes',
            'description': 'Beautiful lash extensions for that perfect flutter',
            'icon': 'fas fa-eye',
            'category_slug': 'lashes'
        },
        {
            'name': 'Makeup',
            'description': 'Expert makeup application for any occasion',
            'icon': 'fas fa-paint-brush',
            'category_slug': 'makeup'
        },
    ]
    
    # Check which default services have galleries
    if not services:
        for service in default_services:
            try:
                category = Category.objects.get(slug=service['category_slug'])
                print("Found category:", category.slug)
                print("Images exist:", hasattr(category, "images"))
                if hasattr(category, "images"):
                    service['has_gallery'] = category.images.exists()
                else:
                    service['has_gallery'] = False
                service['category'] = category
            except Category.DoesNotExist:
                print("Missing category:", service['category_slug'])
                service['has_gallery'] = False
                service['category'] = None

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
