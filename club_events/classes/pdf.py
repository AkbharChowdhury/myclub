import io

from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

BLUE = (0.14, 0.59, 0.74)
BLACK = (0, 0, 0)


class PDF:
    def __init__(self, venues: list[str]):
        self._venues = venues
        self._buffer = io.BytesIO()
        self._my_canvas = canvas.Canvas(self._buffer, pagesize=letter, bottomup=0)

    def _title(self):
        my_canvas = self._my_canvas
        text_obj = my_canvas.beginText()
        text_obj.setFillColorRGB(*BLUE)
        text_obj.setFont("Courier", 28)
        text_obj.setTextOrigin(inch, inch)
        text_obj.textLine("all venues".title())
        return text_obj

    def _venue_details(self):
        text_obj = self._my_canvas.beginText()
        text_obj.setFillColorRGB(*BLACK)
        text_obj.setFont('Helvetica', 12)
        text_obj.setTextOrigin(70, 100)

        for venue in self._venues:
            text_obj.textLine(venue)
        return text_obj

    def generate_pdf(self):
        my_canvas = self._my_canvas
        my_canvas.drawText(self._title())
        my_canvas.drawText(self._venue_details())
        my_canvas.showPage()
        my_canvas.save()
        self._buffer.seek(0)
        return FileResponse(self._buffer, as_attachment=True, filename='venue.pdf')
