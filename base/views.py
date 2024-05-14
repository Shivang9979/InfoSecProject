from django.shortcuts import render,HttpResponse
import sys
from .Algo import Main
import zipfile
from io import BytesIO
import os
def index(request):
    if request.method=='POST':
        if 'Encrypt' in request.POST:
            uploaded_file = request.FILES.get('FileEncrypt', None)
            if uploaded_file is None:
                print("No file")
            if uploaded_file:
             data = uploaded_file.read().decode('utf-8')
             Main.EncryptInput(data)
        if 'Decrypt' in request.POST:
            uploaded_file = request.FILES.get('FileDecrypt', None)
            if uploaded_file is None:
                print("No file")
            if uploaded_file:
             data = uploaded_file.read().decode('utf-8')
             print(data)
             Main.DecryptMessage(data)

                 
                 
                          
            # Process or save the uploaded .txt file here
            # You can access the file using the 'uploaded_file' variable
            # Example: with open('uploaded_file.txt', 'wb') as destination:
            #              for chunk in uploaded_file.chunks():
            #                  destination.write(chunk)
    # Main.main()
    return render(request,'index.html')
# Create your views here.
def serve_file(request, file_path):
    file_full_path = os.path.join(os.getcwd()+"\\base\Algo",file_path) 
    if os.path.exists(file_full_path):
        with open(file_full_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        return HttpResponse("File not found", status=404)
def create_zip_and_download(request):
    # List of files to include in the zip folder
    path1=os.getcwd()+"\\base\Algo\Segments"
    files_in_folder_1 = [f'{path1}\\0.txt', f'{path1}\\1.txt', f'{path1}\\2.txt',f'{path1}\\3.txt',f'{path1}\\4.txt']
    path2=os.getcwd()+"\\base\Algo\Infos"
    files_in_folder_2 = [f'{path2}\\IV.txt', f'{path2}\\KEY1.txt', f'{path2}\\KEY2.txt',f'{path2}\\Log.txt']
    # File to include outside the folder
    file_outside_folder = os.getcwd()+"\\base\\Algo\\New.txt"

    # Create an in-memory zip file
    memory_buffer = BytesIO()
    with zipfile.ZipFile(memory_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add files within the folder
        for file_path in files_in_folder_1:
            file_name = os.path.basename(file_path)
            zf.write(file_path, f'Segments/{file_name}')
        for file_path in files_in_folder_2:
            file_name = os.path.basename(file_path)
            zf.write(file_path, f'Infos/{file_name}')

        # Add the file outside the folder
        outside_file_name = os.path.basename(file_outside_folder)
        zf.write(file_outside_folder, outside_file_name)

    memory_buffer.seek(0)
    response = HttpResponse(memory_buffer.read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=Encrypted_file.zip'
    return response