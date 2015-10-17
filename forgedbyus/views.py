from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from forgedbyus.utils import get_mailchimp_api
import mailchimp

from products.models import Product, Collection

def index(request):
    products = Product.objects.all().order_by('-created')[:48]
    collections = Collection.objects.filter(featured=True)
    if request.is_ajax():
        template = 'item_page.html'
    else:
        template = 'index.html'
    return render(request, template, {'products':products, 'collections':collections})

def subscribe(request, list_id):
    try:
        m = get_mailchimp_api()
        m.lists.subscribe(list_id, {'email':request.POST['email']})
        messages.success(request,  "The email has been successfully subscribed")
    except mailchimp.ListAlreadySubscribedError:
        messages.error(request,  "That email is already subscribed to the list")
        return redirect('/lists/'+list_id)
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/lists/'+list_id)
    return redirect(reverse('lists.views.view', args=(list_id,)))
