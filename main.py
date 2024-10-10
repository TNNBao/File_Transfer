from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.title("ShareIt")
root.geometry("450x560+500+200")
root.config(bg="#f4fdfe")
root.resizable(False, False)

def send_view():
    send_window = Toplevel(root)
    send_window.title("Send")
    send_window.geometry("450x560+500+200")
    send_window.config(bg="#f4fdfe")
    send_window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(), 
            title="Select Image File", 
            filetypes=(("file_type", "*.txt"), ("all files", "*.*"))
            )

    def send_file():
        s = socket.socket()
        port = 8080
        host = socket.gethostname()
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Waiting for incoming connection....')
        conn, addr = s.accept()
        file = open(filename, "rb")
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully..")

    # icon
    send_image_icon = ImageTk.PhotoImage(Image.open("images/send.png").resize((10, 10)))
    send_window.iconphoto(False, send_image_icon)

    send_bg = ImageTk.PhotoImage(Image.open("images/send_bg.jpg").resize((450, 240)))
    Label(send_window, image=send_bg).place(x=-2, y=0)

    host = socket.gethostname()
    Label(send_window, text=f"ID: {host}", bg="white", fg="black").place(x=140, y=290)

    Button(send_window, text="+ Select file", width=10, height=1, font=("",14,"bold"), bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(send_window, text="Send", width=8, height=1, font=("",14,"bold"), bg="#000", fg="#fff", command=send_file).place(x=300, y=150)

    send_window.mainloop()

def receive_view():
    receive_window = Toplevel(root)
    receive_window.title("Receive")
    receive_window.geometry("450x560+500+200")
    receive_window.config(bg="#f4fdfe")
    receive_window.resizable(False, False)

    def receive_file():
        id = sender_id.get()
        file_received = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((id, port))
        file = open(file_received, "wb")
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    # icon
    receive_image_icon = ImageTk.PhotoImage(Image.open("images/receive.png").resize((10, 10)))
    receive_window.iconphoto(False, receive_image_icon)

    receive_bg = ImageTk.PhotoImage(Image.open("images/bg.jpg").resize((450, 240)))
    Label(receive_window, image=receive_bg).place(x=-2, y=0)

    Label(receive_window, text="Receive", font=("", 20), bg="#f4fdfe").place(x=100, y=280)

    Label(receive_window, text="Input sender id", font=("", 10, "bold"), bg="#f4fdfe").place(x=20, y=340)
    sender_id = Entry(receive_window, width=25, fg="black", border=2, bg="white", font=("", 15))
    sender_id.place(x=20, y=370)
    sender_id.focus()

    Label(receive_window, text="Filename for the incoming file:", font=("", 10, "bold"), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(receive_window, width=25, fg="black", border=2, bg="white", font=("", 15))
    incoming_file.place(x=20, y=450)

    download_icon = ImageTk.PhotoImage(Image.open("images/download.png").resize((20, 20)))
    receive_file_btn = Button(receive_window, text="Receive", compound=LEFT, image=download_icon, width=130, bg="#39c790", font=("", 14, "bold"), command=receive_file)
    receive_file_btn.place(x=20, y=500)

    receive_window.mainloop()

# icon
image_icon = ImageTk.PhotoImage(Image.open("images/icon.png").resize((10, 40)))
root.iconphoto(False, image_icon)

Label(root, text="File Sharing", font=("", 20, "bold"), bg="#f4fdfe").place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_image = ImageTk.PhotoImage(Image.open("images/send.png").resize((100, 100)))
send_btn_nav = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=send_view)
send_btn_nav.place(x=50, y=100)

receive_image = ImageTk.PhotoImage(Image.open("images/receive.png").resize((100, 100)))
receive_btn_nav = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=receive_view)
receive_btn_nav.place(x=300, y=100)

# label
Label(root, text="Send", font=("", 17, "bold"), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=("", 17, "bold"), bg="#f4fdfe").place(x=300, y=200)

bg_image = ImageTk.PhotoImage(Image.open("images/bg.jpg").resize((450, 240)))
Label(root, image=bg_image).place(x=-2, y=323)



root.mainloop()