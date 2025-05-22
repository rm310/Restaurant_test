from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdersPage,  ContactInfoPage, BookingPage, OrderDetailsFormSet
from .models import DishesMenu, BookingPlace, ContactInfo,OrderDetails, Orders
from rest_framework import viewsets
from .serializers import DishesMenuSerializer

class DishesMenuSet(viewsets.ModelViewSet):
    queryset = DishesMenu.objects.all()
    serializer_class = DishesMenuSerializer
    


def contactinfo(request):
    if request.method == 'POST':
        form = ContactInfoPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactinfo')
        if 'edit' in request.POST:
            contact_id = request.POST.get('contact_id')
            print(f"Editing contact with ID: {contact_id}")
            if contact_id:  
                contact = get_object_or_404(ContactInfo, id=contact_id)
                form = ContactInfoPage(request.POST, instance=contact)
                if form.is_valid():
                    form.save()
                    return redirect('contactinfo')
                else:
                    print("Edit form errors:", form.errors)
            else:
                print("No contact_id provided for editing.")

        elif 'delete' in request.POST:
            contact_id = request.POST.get('contact_id')
            print(f"Deleting contact with ID: {contact_id}")
            if contact_id:
                contact = get_object_or_404(ContactInfo, id=contact_id)
                contact.delete()
                return redirect('contactinfo')
            else:
                print("No contact_id provided for deletion.")
    else:
        form = ContactInfoPage()
    contacts = ContactInfo.objects.all()
    return render(request, 'restaurant/ContactInformation.html', {'form': form, 'contacts': contacts})

def booking(request):
    if request.method == 'POST':
        form = BookingPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
        elif 'edit' in request.POST:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(BookingPlace, id=booking_id)
            form = BookingPage(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                return redirect('booking')
            else:
                print("Edit form errors:", form.errors)

        elif 'delete' in request.POST:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(BookingPlace, id=booking_id)
            booking.delete()
            return redirect('booking')
    else:
        form = BookingPage()
    bookings = BookingPlace.objects.all()
    return render(request, 'restaurant/BookingSystem.html', {'form': form, 'bookings': bookings})

def orders(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        order_id = request.POST.get('order_id')

        if action == 'delete':
            order = get_object_or_404(Orders, id=order_id)
            order.delete()
            return redirect('orders')
        elif action == 'update':
            order = get_object_or_404(Orders, id=order_id)
            form = OrdersPage(request.POST, instance=order)
            order_details = OrderDetails.objects.filter(order=order)
            formset = OrderDetailsFormSet(request.POST)
            if form.is_valid():
                form.save()
                for order_detail_form in formset:
                    if order_detail_form.cleaned_data:
                        order_detail = order_detail_form.save(commit=False)
                        order_detail.order = order
                        order_detail.save()
                return redirect('orders')
        form = OrdersPage(request.POST)
        formset = OrderDetailsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            order = form.save()
            for order_detail_page in formset:
                if order_detail_page.cleaned_data:
                    order_detail = order_detail_page.save(commit = False)
                    order_detail.order = order
                    order_detail.save()
            return redirect('orders')
    else:
        form = OrdersPage()
        formset = OrderDetailsFormSet(queryset=OrderDetails.objects.none())
    orders = Orders.objects.all()
    dishes = DishesMenu.objects.all()
    return render(request, 'restaurant/Orders.html', {'form': form, 'formset': formset, 'dishes': dishes, 'orders': orders})



