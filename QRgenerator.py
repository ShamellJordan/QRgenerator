import qrcode
import os

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#6aff9b", back_color="white")
    img.save(file_name)

def main():
    text = "https://github.com/" # Input WEBSITE URL to generate QR Code 

    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # File name to save the QR Code image with full path
    file_name = os.path.join(script_dir, "qr_code.png")

    # Generate the QR code
    generate_qr_code(text, file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    main()

