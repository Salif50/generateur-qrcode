from django.shortcuts import render
import qrcode
import os
from django.conf import settings

def home(request):

    if request.method=='POST':
        prenom=request.POST.get('prenom')
        nom=request.POST.get('nom')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        profession=request.POST.get('profession')

        qr=qrcode.QRCode()
        data=f"Prénom:{prenom}\nNom:{nom}\nEmail:{email}\nTéléphone:{telephone}\nProfession:{profession}"
        qr.add_data(data)
        qr.make()
        img=qr.make_image(fill_color='blue',back_color='white')
        image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'image.png')
        img.save(image_path)
        return render(request,'cryptage/index.html')



    return render(request,'cryptage/index.html')