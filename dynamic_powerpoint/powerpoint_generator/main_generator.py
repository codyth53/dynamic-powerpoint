from .powerpoint_generator import PowerpointGenerator
from .two_week_generator import generate_two_week
from pptx import Presentation


def generate_powerpoint(pg: PowerpointGenerator):
    pptx = Presentation(pg.config.get_template_path())

    two_week_slide = pptx.slides[2]
    generate_two_week(pg, two_week_slide)

    pptx.save(pg.config.get_save_path())
