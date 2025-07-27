import qrcode
from PIL import Image

def generate_qr_code():
    # Get URL from user
    url = input("Enter the URL or text to generate QR code: ")
    
    # Get filename from user
    filename = input("Enter filename (without extension): ")
    if not filename:
        filename = "qr_code"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Generate and save image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")
    
    print(f"QR code generated successfully and saved as {filename}.png")

if __name__ == "__main__":
    generate_qr_code()
