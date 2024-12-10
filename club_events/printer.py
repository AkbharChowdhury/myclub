import csv
from django.http import HttpResponse
from .models import Venue
from .file_extension import FileExtension
from .content_type import ContentType


class Printer:

    def _venue_details(self) -> list[str]:

        lines = []
        for venue in Venue.objects.all():
            lines.append(venue.name)
            lines.append(venue.address)
            lines.append(venue.zip_code)
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

    def pdf_file(self):
        pass
