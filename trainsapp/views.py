from django.shortcuts import render
from trainsapp.seriallizer import AllTrainSerializers
from trainsapp.models import AllTrain
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def AllTrainsApi(request,id=0):

    if request.method == 'GET':
        trains = AllTrain.objects.all()
        train_serialiser = AllTrainSerializers(trains,many=True)
        return JsonResponse(train_serialiser.data,safe=False)

    elif request.method == 'POST':
        trains = JSONParser().parse(request)
        train_serialiser = AllTrainSerializers(data = trains)
        if train_serialiser.is_valid():
            train_serialiser.save()
            return JsonResponse("Record Added Successfully",safe=False)

    elif request.method == 'PUT':
        newtrains = JSONParser().parse(request)
        old_record = AllTrain.objects.get(id=id)
        train_serialiser = AllTrainSerializers(old_record,data=newtrains)
        if train_serialiser.is_valid():
            train_serialiser.save()
            return JsonResponse("Record Modified Successfully",safe=False)
        return JsonResponse(train_serialiser.errors,status=400)  #this one line for error correction purpuse
    
    elif request.method == 'DELETE':
        old_record = AllTrain.objects.get(id=id)
        old_record.delete()
        return JsonResponse("Record Delated Successfully",safe=False)
    





