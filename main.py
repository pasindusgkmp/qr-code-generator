from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog
import qrcode
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\A.My Projects\python projects\qr code generator\qr app\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def generate_qr_code():
    # Get the text from the Entry widget
    text = entry_1.get()

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Display the image on the canvas
    global image_image_1
    image_image_1 = ImageTk.PhotoImage(qr_image)
    canvas.itemconfig(qr_image_id, image=image_image_1)

    # Save the QR code image to a global variable for future use
    global generated_qr_code
    generated_qr_code = qr_image


def save_qr_code():
    if generated_qr_code:
        # Ask user to choose a file location to save the QR code image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            generated_qr_code.save(file_path)


window = Tk()
window.geometry("932x600")
window.configure(bg="#FFFFFF")

# Set the title of the application window
window.title("QR Code Generator")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=567,
    width=932,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create a red rectangle on the canvas
canvas.create_rectangle(
    0.0,
    0.0,
    519.0,
    567.0,
    fill="#FF0000",
    outline=""
)

canvas.create_text(
    126.0,
    284.0,
    anchor="nw",
    text="Generator",
    fill="#FFFFFF",
    font=("Poppins Regular", 30 * -1)
)

canvas.create_text(
    126.0,
    222.0,
    anchor="nw",
    text="QR CODE",
    fill="#FFFFFF",
    font=("Poppins Regular", 48 * -1)
)

# Create Entry widget for text input
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=579.0,
    y=112.0,
    width=300.0,
    height=47.0
)

# Create image widget
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
qr_image_id = canvas.create_image(
    729.0,
    388.0,
    image=image_image_1
)

canvas.create_text(
    579.0,
    18.0,
    anchor="nw",
    text="QR Code generator",
    fill="#000000",
    font=("Poppins Regular", 30 * -1)
)

canvas.create_text(
    579.0,
    63.0,
    anchor="nw",
    text="Please enter a URL or text to create a QR Code",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

# Create button to generate QR code
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generate_qr_code,
    relief="flat"
)
button_1.place(
    x=579.0,
    y=185.0,
    width=300.0,
    height=49.0
)

# Create button to save QR code
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=save_qr_code,
    relief="flat"
)
button_2.place(
    x=684.0,
    y=525.0,
    width=90.0,
    height=32.566375732421875
)

# Keep a reference to the button images to prevent them from being garbage collected
button_1.image = button_image_1
button_2.image = button_image_2

window.resizable(False, False)
window.mainloop()
