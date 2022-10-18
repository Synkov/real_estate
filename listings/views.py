from django.shortcuts import render, redirect

from .forms import ListingForm
from .models import Listing


def listing_list(request):
    listings = Listing.objects.all()
    content = {'listings': listings}
    return render(request, 'listings.html', content)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(pk=pk)
    content = {'listing': listing}
    return render(request, 'listing.html', content)


def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {'form': form}
    return render(request, 'listing_create.html', content)


def listing_update(request, pk):
    listing = Listing.objects.get(pk=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/')
    content = {'form': form}
    return render(request, 'listing_update.html', content)


def listing_delete(request, pk):
    listing = Listing.objects.get(pk=pk)
    listing.delete()
    return redirect('/')
