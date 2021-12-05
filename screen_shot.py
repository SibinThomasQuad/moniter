import mss
import base64
import os
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
with mss.mss() as sct:
    filename = sct.shot(output="screen/output.png")
print(get_base64_encoded_image("screen/output.png"))
os.remove("screen/output.png")
