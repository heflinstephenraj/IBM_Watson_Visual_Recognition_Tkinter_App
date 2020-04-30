from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter.font as font
from ibm_watson import VisualRecognitionV3 as vr
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tkinterhtml import HtmlFrame

authenticator = IAMAuthenticator("API Key") #paste your API Key
vr1=vr(version="2018-03-19",authenticator=authenticator)
vr1.set_service_url("Service URL") #paste your service URL

def urlclassify():
    try:
        result=vr1.classify(url=url.get()).get_result()
        result1='''<html><head></head><body><table style="width:100%" border="1"><tr><th>Classification</th><th>Confident Score</th></tr> 
    
'''
    except:
        wrg=messagebox.showwarning(title="URL Error", message=f'''
Please enter the proper image URL to classify. 

The given URl is not a image URL.

The given URL is "{url.get()}".
''').iconphoto(False,p1)  
    for i in range(len(result["images"][0]["classifiers"][0]["classes"])):
        result1=result1+f'<tr><td><center>{result["images"][0]["classifiers"][0]["classes"][i]["class"]} </center></td><td><center> {str(round(result["images"][0]["classifiers"][0]["classes"][i]["score"]*100))}% </center></td></tr>'
    result1=result1+f'</table><p><h3 style="color:Blue"><center>Please Close and run the application to Classify another image.<br>Thank You<center></h3><p></body></html>'
    frame = HtmlFrame(root)
    frame.set_content(result1)
    frame.pack()

def imageLocalClassify():
    try:
        filelocation = askopenfilename()
        with open(filelocation,"rb") as img:
            result=vr1.classify(images_file=img).get_result()
    except:
        wrg=messagebox.showwarning(title="Image Error", message=f'''
Please select the proper image to classify. 

The given file is not a image file.

The given file is "{filelocation}".
''').iconphoto(False,p1)
    result1='''<html><head></head><body><table style="width:100%" border="1"><tr><th>Classification</th><th>Confident Score</th></tr> 
'''
    for i in range(len(result["images"][0]["classifiers"][0]["classes"])):
        result1=result1+f'<tr><td><center>{result["images"][0]["classifiers"][0]["classes"][i]["class"]} </center></td><td><center> {str(round(result["images"][0]["classifiers"][0]["classes"][i]["score"]*100))}% </center></td></tr>'
    result1=result1+f'</table><p><h3 style="color:Blue"><center>Please Close and run the application to Classify another image.<br>Thank You<center></h3><p></body></html>'
    frame = HtmlFrame(root)
    frame.set_content(result1)
    frame.pack()
    

root = Tk()
root.title("Image Classification")
p1 = PhotoImage(file = "icon.png")
root.iconphoto(False, p1)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()-70
root.geometry("%dx%d+0+0" % (w, h))
welcome = Label(root,text="Image Classification ")
welcome["font"] = font.Font(family='Courier', size=30, weight='bold', underline=True)
welcome.pack()
description = Label(text="""
We do not save your image to clasiify.
The image will be sent to IBM Watson Visual Recognition service for classification through IBM Watson Python SDK.

This application was developed by Heflin Stephen Raj S. To contact the developer, Please visit www.heflin.dev
""",fg="#0F216C")
description["font"]=font.Font(family='Courier', size=14, weight='bold', underline=True)
description.pack()
button0 = Button(root, text="Choose the Image and Classify", command=imageLocalClassify,bg="#0000FF", fg="#FFFFFF") 
button0["font"]=font.Font(family='Courier', size=12, weight='bold')
button0.pack(side=TOP)
emp = Label(text="")
emp.pack()
url = Entry(root) 
url.pack()
button1 = Button(root, text="Enter the URL and Classify", command =urlclassify, bg="#FF0000", fg="#FFFFFF")
button1["font"]= font.Font(family='Courier', size=12, weight='bold')
button1.pack(side=TOP)
emp1=Label(text="")
emp1.pack()
close = Button(root,text="Close",command = root.destroy, bg="#000000", fg="#FFFFFF",)
close.pack()
emp2=Label(text="")
emp2.pack()
root.mainloop()
