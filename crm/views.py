from django.shortcuts import render

# Create your views here.
from .models import (
    Customer
) 

# Create your views here.

def get_customers(request):
    """get all customers in db"""
    customers = Customer.objects.all()
    return render(request, 'crm/customers.html', {
        'customers': customers
    })


def save_customer(request):
    if request.POST:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        rec = Customer(name=name,phone= phone,email=email)
        try:
            rec.save()
            if rec :
                customers = Customer.objects.all()
                return render(request, 'crm/customers.html', {
                    'customers': customers,
                    'message': 'customer added successfully'
                })
            else:
                customers = Customer.objects.all()
                return render(request, 'crm/customers.html', {
                    'customers': customers,
                    'error': 'customer not added'
                })
        except Exception as e:
            customers = Customer.objects.all()
            return render(request, 'crm/customers.html', {
                'customers': customers,
                'error': 'customer not added: '+ str(e)
            })
    else:
        customers = Customer.objects.all()
        return render(request, 'crm/customers.html', {
            'customers': customers
        })


def delete_customer(request, id):
    customer = Customer.objects.filter(id=int(id))
    if customer:
        customer.delete()
        customers = Customer.objects.all()
        return render(request, 'crm/customers.html', {
            'customers': customers,
            'message': 'customer removed'
        })
    else:
        customers = Customer.objects.all()
        return render(request, 'crm/customers.html', {
            'customers': customers,
            'error': 'customer not found'
        })