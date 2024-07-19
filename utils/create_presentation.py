from pptx import Presentation
from pptx.util import Inches
import os


presentation = Presentation()

slide_layout = presentation.slide_layouts[2]

directory = "first slide"
files = os.listdir(directory)
slide = presentation.slides.add_slide(slide_layout)

for file in files:
    img_path = f'first slide/{file}'
    left = top = Inches(1)
    slide.shapes.add_picture(img_path, left, top)

presentation.save("test_presentation.pptx")
