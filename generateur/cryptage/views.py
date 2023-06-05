from django.shortcuts import render
import qrcode
import random as rd
import os
from io import BytesIO
from django.conf import settings
from cryptage.models import Stock
from django.core.files.base import ContentFile


def home(request):

    if request.method=='POST':
        prenom=request.POST.get('prenom')
        nom=request.POST.get('nom')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        profession=request.POST.get('profession')
        couleur=[
            'blue',
            'black',
            'red',
            'yellow',
            
        ]

        table=Stock()

        qr=qrcode.QRCode()
        data=f"Prénom:{prenom}\nNom:{nom}\nEmail:{email}\nTéléphone:{telephone}\nProfession:{profession}"
        qr.add_data(data)
        qr.make()
        img=qr.make_image(fill_color=rd.choice(couleur),back_color='white')
        binaire=BytesIO()
        img.save(binaire,format='PNG')
        binaire.seek(0)
        table.image.save(f"{prenom}_{nom}_{rd.randint(1,1000)}.png", ContentFile(binaire.read()))
        table.save()

        image_afficher=Stock.objects.last()
        context={
            'img':image_afficher
        }
        
       




       
        return render(request,'cryptage/index.html',context)



    return render(request,'cryptage/index.html')



def list(request):

    images=Stock.objects.all()

    return render(request,'cryptage/list.html',{'images':images})