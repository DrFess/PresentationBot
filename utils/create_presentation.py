from pptx import Presentation

presentation = Presentation()

slide_layout = presentation.slide_layouts[2]
slide = presentation.slides.add_slide(slide_layout)

presentation.save("test_presentation.pptx")
