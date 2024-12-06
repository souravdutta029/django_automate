from django.shortcuts import render, redirect
from .forms import CompressImageForm
from .models import CompressImage
from PIL import Image
import io
from django.http import HttpResponse
from django.contrib import messages


def compress(request):
    user = request.user
    if request.method == 'POST':
        form = CompressImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_img = request.FILES['original_img']
            quality = form.cleaned_data['quality']
            compressed_image = form.save(commit=False)
            compressed_image.user = user

            # Perform Compression
            img = Image.open(original_img)
            output_format = img.format
            buffer = io.BytesIO()
            img.save(buffer, output_format, quality=quality)
            buffer.seek(0)
            
            # Save the compressed image inside the model
            compressed_image.compressed_img.save(
                f"compressed_{original_img}",
                buffer,
            )
            
            # Automatically download the compressed file
            response = HttpResponse(buffer.getvalue(), content_type=f"image/{output_format.lower()}")
            response['Content-Disposition'] = f'attachment; filename="compressed_{original_img}"'
            return response
    else:
        form = CompressImageForm()
        context = {
            'form': form
        }
        return render(request, 'image_compression/compress.html', context)