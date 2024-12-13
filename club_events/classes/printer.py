import csv
from django.http import HttpResponse
from club_events.models import Venue
from club_events.classes.file_extension import FileExtension
from club_events.classes.pdf import PDF


class Printer:

    def _venues(self, is_sep=False) -> list[str]:
        lines = []
        for venue in Venue.objects.all():
            lines.append(venue.name)
            lines.append(venue.address)
            lines.append(venue.zip_code)
            if is_sep:
                lines.append('================')
        return lines

    def txt(self) -> HttpResponse:
        response = HttpResponse(content_type="text/plain")
        response["Content-Disposition"] = self._attachment(FileExtension.TEXT_FILE)

        for venue in self._venues():
            response.write(f'{venue}\n')
            response.write('\n')
        return response

    def csv(self) -> HttpResponse:
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = self._attachment(FileExtension.CSV)
        writer = csv.writer(response)
        writer.writerow(['Venue Name', 'Address', 'Zip Code'])
        for venue in Venue.objects.all():
            writer.writerow([venue.name, venue.address, venue.zip_code])
        return response

    def _attachment(self, extension: FileExtension) -> str:
        return f'attachment; filename="venue.{extension}"'

    def pdf(self):
        return PDF(venues=self._venues(is_sep=True)).generate_pdf()
