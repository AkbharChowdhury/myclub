import csv
from django.http import HttpResponse
from .models import Venue
from .file_extension import FileExtension
from .content_type import ContentType
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


class Printer:

    def _venue_details(self, is_sep=False) -> list[str]:
        lines = []
        for venue in Venue.objects.all():
            lines.append(venue.name)
            lines.append(venue.address)
            lines.append(venue.zip_code)
            if is_sep:
                lines.append('================')
        return lines

    def text_file(self) -> HttpResponse:
        response = HttpResponse(content_type=ContentType.TEXT_FILE)
        response['Content-Disposition'] = self._attachment(extension=FileExtension.TEXT_FILE)
        for venue in self._venue_details():
            response.write(f'{venue}\n')
            response.write('\n')
        return response

    def csv(self) -> HttpResponse:
        response = HttpResponse(content_type=ContentType.CSV)
        response['Content-Disposition'] = self._attachment(extension=FileExtension.CSV)
        writer = csv.writer(response)
        writer.writerow(['Venue Name', 'Address', 'Zip Code'])
        for venue in Venue.objects.all():
            writer.writerow([venue.name, venue.address, venue.zip_code])
        return response

    def _attachment(self, extension: FileExtension) -> str:
        return f'attachment; filename="venue.{extension}"'

    def pdf(self):
        buf = io.BytesIO()
        my_canvas = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        text_obj = my_canvas.beginText()
        text_obj.setTextOrigin(inch, inch)
        text_obj.setFont('Helvetica', 12)

        for venue in self._venue_details(is_sep=True):
            text_obj.textLine(venue)

        my_canvas.drawText(text_obj)
        my_canvas.showPage()
        my_canvas.save()
        buf.seek(0)
        return FileResponse(buf, as_attachment=True, filename='venue.pdf')
