from rembg import remove
from PIL import Image


input_path = 'sb.jpg'
output_path = 'output.png'

print("Starting removing...\n")
input = Image.open(input_path)
output = remove(input)

output.save(output_path)
print("End\n")
