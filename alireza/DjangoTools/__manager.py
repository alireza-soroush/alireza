__all__= ['rename_file',]


import uuid






def rename_file(instance,filename,customformats:list=[],filenamemethod:str=uuid.uuid4(),hardpath:str=False,*args,**kwargs) -> str :
    """
    This function is originally made for Django, but you can use it anywhere depending on your needs.
    
    This function will return you a string containing the name and format of the file and you should use this function in upload_file in Django models.
    The files are stored in the MEDIA_ROOT path in your settings.py.
    If you want to use customformat or filenametype or other things in Django models.py , create a separate function in models.py and put the following codes in it.

    def created_function(instance,filename):
        return rename_file(instance,filename,customformats=[give formats here],filenamemethod=give your method for naming files here,hardpath=give path here)

    In your model:
    image = models.ImageField(upload_to=created_function)


    If you want to save the files in another Directory in your MEDIA_ROOT you can give a path to hard path and it will save file in that path .
    
    Example: 

    def created_function(instance,filename):
        return rename_file(instance,filename,hardpath='profiles') --> file saves in -> MEDIA_ROOT/profiles/image.png


    """
    custom_format = ['tar.gz'] + customformats
    sp = [i for i in filename.split('.') if len(i)>0] 
    if len(sp) < 2:
        return None
    elif len(sp) == 2:
        ext = sp[-1]
    else:
        for format in custom_format:
            g = format.split('.')
            lg = len(g) 
            if sp[-lg:] == g:
                ext = format
                break
    if hardpath == False:
        try:
            return '%s.%s' % (filenamemethod,ext)
        except UnboundLocalError:
            return '%s.%s' % (filenamemethod,sp[-1])
    
    else:
        while hardpath[-1] == '/':
            hardpath = hardpath[0:-1:1]
        try:
            return '%s/%s.%s' % (hardpath,filenamemethod,ext)
        except UnboundLocalError:
            return '%s/%s.%s' % (hardpath,filenamemethod,sp[-1])
            











