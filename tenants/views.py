from django.shortcuts import render, redirect
from add_property.models import PropertyFlat, Location, FlatImage, PropertyRoom, RoomImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import EmailMessage


def rent_view(request):
    property_flat = PropertyFlat.objects.all()
    property_room = PropertyRoom.objects.all()
    return render(request, 'rent_view.html', {'property_flat': property_flat, 'property_room': property_room})


def search(request):
    if request.method == 'POST':
        search_request = request.POST.get('search', False)
        if search_request:
            match = PropertyFlat.objects.all().filter(
                Q(price__istartswith=search_request) |
                Q(location__state__startswith=search_request) |
                Q(location__district__startswith=search_request) |
                Q(location__municipality__startswith=search_request)

            )
            if match:
                return render(request, 'search_result.html', {'searched': match})

            else:
                match = PropertyFlat.objects.all()
                error = 'No result found !'
                return render(request, 'search_result.html', {'error': error, 'error_view': match})

        elif search_request == '' or search_request == 'None':
            return redirect('/')

        else:
            price = request.POST.get('price', False)
            state = request.POST.get('state', False)
            district = request.POST.get('district', False)
            if price == '' and state == '' and district == '':
                return redirect('/')

            else:
                match = PropertyFlat.objects.all().filter(
                    Q(price__icontains=price) &
                    Q(location__state__icontains=state) &
                    Q(location__district__icontains=district)
                )
                if match:
                    return render(request, 'search_result.html', {'searched': match})
                else:
                    match = PropertyFlat.objects.all()
                    error = 'No result found !'
                    return render(request, 'search_result.html', {'error': error, 'error_view': match})

    return render(request, 'search_result.html')

