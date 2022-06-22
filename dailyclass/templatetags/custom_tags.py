from django import template

register = template.Library()


def getFileExtension(value):
    return value.split('.')[-1]


def getImgUrl(extension):
    extension = extension.lower()
    if extension in ('doc', 'docx', 'docm'):
        return "images/docx.png"
    elif extension in ('xls', 'xlsx', 'xlsm', 'xlsb', 'xltm', 'xlam', 'xltx'):
        return "images/excel.png"
    elif extension in ('hwp', 'hwpx'):
        return "images/hwp.png"
    elif extension in ('jpeg', 'jpg', 'gif', 'bmp', 'png', 'tif', 'tiff'):
        return "images/image.png"
    elif extension in ('pdf'):
        return "images/pdf.png"
    elif extension in ('ppt', 'pptx'):
        return "images/ppt.png"
    else:
        return "images/document.png"


register.filter('getFileExtension', getFileExtension)
register.filter('getImgUrl', getImgUrl)
