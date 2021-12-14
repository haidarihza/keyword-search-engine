import win32com.client

def readtext() :
    word = win32com.client.Dispatch("Word.Application")
    word.visible = False
    wb = word.Documents.Open("filename")
    doc = word.ActiveDocument
    text = doc.Range().Text
    return text
