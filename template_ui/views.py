from django.shortcuts import render
from .models import user_collection
# Create your views here.


def crud(request):
    records = user_collection.find()
    update = None
    if request.method == 'POST':
        if 'save' in request.POST:
            if request.POST.get('save'):
                id = int(request.POST.get('save'))
                name = request.POST.get('name')
                score = request.POST.get('score')
                user_collection.update_one({'id':id}, {'$set':{'name':name, 'score':score}})
            else:
                id = user_collection.count_documents({}) + 1
                data = {
                    'id':id,
                    'name':request.POST.get('name'),
                    'score': request.POST.get('score')
                }
                user_collection.insert_one(data)
        
        elif 'delete' in request.POST:
            print("inside delete")
            id = int(request.POST.get('delete'))
            user_collection.delete_one({'id':id})
        else: 
            id = int(request.POST.get('edit'))
            update = user_collection.find_one({'id':id})

    return render(request, 'index.html', {
        'records':records,
        'update':update
    })