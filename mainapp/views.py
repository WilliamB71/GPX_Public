# Create your views here.
from django.shortcuts import render
from .forms import GpxForm
from .utils import get_coordinates, write_gpx_file
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
import googlemaps
import re


def create_gpx(request):
    error_message = None
    if request.method == "POST":
        form = GpxForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                data = form.cleaned_data
                coordinates = get_coordinates(
                    data["start_location"],
                    data["end_location"],
                    data["transport_method"],
                )

                gpx_content = write_gpx_file(coordinates)

                response = HttpResponse(gpx_content, content_type="application/gpx+xml")
                response[
                    "Content-Disposition"
                ] = f'attachment; filename="{smart_str(data["start_location"]) + "_to_" + smart_str(data["end_location"])}.gpx"'
                response["Content-Length"] = len(gpx_content)
                return response
            except googlemaps.exceptions.ApiError:
                error_message = "Error occurred while generating the route. Please check your location inputs and try again."
                form.add_error(None, error_message)
        else:
            error_message = "Invalid form data. Please fill in all the required fields."
            form.add_error(None, error_message)
    else:
        form = GpxForm()

    context = {
        "form": form,
        "error_message": error_message if error_message else None,
    }
    return render(request, "mainapp/create_gpx.html", context)


def home(request):
    return render(request, "mainapp/home.html")
