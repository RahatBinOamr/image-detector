# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
import pytesseract
from langdetect import detect
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image = Image.open(image)  # Convert to PIL Image
            text = pytesseract.image_to_string(image)
            language = detect(text)
            return render(request, 'result.html', {'text': text, 'language': language})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
