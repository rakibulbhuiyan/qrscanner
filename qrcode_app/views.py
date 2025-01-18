import qrcode
from io import BytesIO
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .forms import CardFormModel
from .models import YouTubeVideo


def card_form_view(request):
    if request.method == 'POST':
        form = CardFormModel(request.POST)
        if form.is_valid():
            form.save()
            # After form submission, you can redirect to a success page or back to the form
            return redirect('card_form')  # or redirect to a success page if desired
    else:
        form = CardFormModel()

    return render(request, 'card_form.html', {'form': form})


def generate_qr(request):
    # Direct URLs (These will be clickable once scanned)
    links = [
        "Search Location: \nhttps://www.google.com/maps/place//@13.7411763,100.5564365,17z\n",
        "Visit Our Facebook Page: \nhttps://web.facebook.com/littlespicy/\n",
        "Visit Our Website: https://www.tripadvisor.com/Restaurant_Review-g293916-d17779861-Reviews-Little_Spicy_Restaurant-Bangkok.html"
    ]
    
    # Join the URLs with newlines to give the scanner multiple clickable links
    data = "\n".join(links)
    
    # Generate QR code for the data
    qr = qrcode.make(data)
    
    # Save the QR code as a PNG
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    filename = default_storage.save("qr_code.png", ContentFile(buffer.read()))
    buffer.close()

    # Return the URL of the saved QR code image
    return JsonResponse({"qr_url": default_storage.url(filename)})


def youtube_video_view(request):
    # Fetch the first YouTube video URL from the database (can be modified to fetch all videos)
    video = YouTubeVideo.objects.first()
    
    # Check if the video exists, if not, show a message
    if not video:
        video = None
        message = "No video available."
    else:
        message = None

    return render(request, 'youtube_video.html', {'video': video, 'message': message})




def card_form_view(request):
    if request.method == "POST":
        form = CardFormModel(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return redirect('form_submitted')  # Redirect after successful submission
    else:
        form = CardFormModel()

    return render(request, 'card_form.html', {'form': form})