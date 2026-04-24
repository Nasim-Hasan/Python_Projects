import qrcode
import aisuite as ai
from qrcode.image.styledpil import StyledPilImage
from IPython.display import Image
from dotenv import load_dotenv
_ = load_dotenv()
# Create an instance of the AISuite client
client = ai.Client()

# Create a QR code
def generate_qr_code(data: str, filename: str, image_path: str):
    """Generate a QR code image given data and an image path.
    Args:
    data: Text or URL to encode
    filename: Name for the output PNG file (without extension)
    image_path: Path to the image to be used in the QR code
    """
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    img = qr.make_image(image_factory=StyledPilImage, embedded_image_path=image_path)
    output_file = f"{filename}.png"
    img.save(output_file)
    return f"QR code saved as {output_file} containing: {data[:50]}..."

prompt = "Can you make a QR code for me using my company's logo that goes to www.deeplearning.com from the image dl_logo.jpg?"
response = client.chat.completions.create(
model="openai:o4-mini",
messages=[{"role": "user", "content": (
prompt
)}],
tools=[generate_qr_code],
max_turns=5
)
print(response)
# Display image directly
Image('dl_qr_code.png')