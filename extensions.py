q=".gif"
w=".jpg"
e=".jpeg"
r=".png"
t=".pdf"
y=".txt"
u=".zip"

x=(input("File name: "))
if q in x:
    print("image/gif")
elif w in x:
    print("image/jpeg")
elif e in x:
    print("image/jpeg")
elif r in x:
    print("image/png")
elif t in x:
    print("application/pdf")
elif y in x:
    print("text/plain")
elif u in x:
    print ("application/zip")
else:
    print ("application/octet-stream")