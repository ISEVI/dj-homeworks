from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV

DATA = []
with open(BUS_STATION_CSV, encoding='utf-8') as File:
    reader = csv.DictReader(File)
    for row in reader:
        DATA.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    page = request.GET.get('page', 1)
    elements_per_page = 10
    # также передайте в контекст список станций на странице
    paginator = Paginator(DATA, elements_per_page)
    page_ = paginator.get_page(page)

    context = {
         'bus_stations': page_.object_list,
         'page': page_,
    }
    return render(request, 'stations/index.html', context)
