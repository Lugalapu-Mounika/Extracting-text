import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import boto3
import boto3.session
from docx import Document

my_win = tk.Tk()
my_win.geometry("1250x1200")
my_win.title("AWS Textract")

l1 = tk.Label(
    my_win, text="Upload an Image or Document", width=30, font=("times", 18, "bold")
)
l1.pack()
text_output = tk.Text(my_win, height=15, width=80)
text_output.pack()
b1 = tk.Button(
    my_win, text="Upload file & analyze text", width=30, command=lambda: uploadfile()
)
b1.pack()


def uploadfile():
    aws_console = boto3.session.Session(profile_name="user")
    client = aws_console.client(service_name="textract", region_name="us-east-1")

    global img
    f_types = [
        ("Image Files", "*.jpg *.png"),
        ("Text Files", "*.txt"),    
        ("PDF Files", "*.pdf"),
        ("Doc Files", "*.docx"),
    ]
    filename = filedialog.askopenfilename(filetypes=f_types)

    if filename:
        text_output.delete("1.0", tk.END)
        detected_text = ""  # Initialize detected_text here
        response = None  # Initialize response to avoid UnboundLocalError

        if filename.lower().endswith((".jpg", ".png")):  # IMAGE
            img = Image.open(filename)
            img_resize = img.resize((800, 600))
            img = ImageTk.PhotoImage(img_resize)
            img_label = tk.Button(my_win, image=img)
            img_label.image = img
            img_label.pack()
            imgbytes = get_image_byte(filename)
            response = client.detect_document_text(Document={"Bytes": imgbytes})
            messagebox.showinfo("Success", "Image submitted successfully!")

        elif filename.lower().endswith(".txt"):  # TEXT FILE
            with open(filename, "r") as txt_file:
                content = txt_file.read()
                text_output.insert(tk.END, content)
            messagebox.showinfo("Success", "Text submitted successfully!")

        elif filename.lower().endswith(".pdf"):  # PDF FILE
            with open(filename, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
            response = client.analyze_document(
                Document={"Bytes": pdf_bytes}, FeatureTypes=["TABLES", "FORMS"]
            )
            messagebox.showinfo("Success", "PDF submitted successfully!")

        elif filename.lower().endswith(".docx"):  # WORD FILE
            doc = Document(filename)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            text_output.insert(tk.END, "\n".join(full_text))
            messagebox.showinfo("Success", "Word document submitted successfully!")

        if response:
            for item in response["Blocks"]:
                if item["BlockType"] == "LINE":
                    detected_text += item["Text"] + "\n"
            
            if detected_text.strip():  # Check if detected_text is not empty
                text_output.insert(tk.END, detected_text)
            else:
                messagebox.showwarning("No Text Detected", "No text was detected in the image or document.")

def get_image_byte(filename):
    with open(filename, "rb") as imagefile:
        return imagefile.read()


my_win.mainloop()
