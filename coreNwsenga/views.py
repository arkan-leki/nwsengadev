from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django_htmx.http import HttpResponseClientRefresh, reswap
from coreNwsenga.forms import BaxForm, CityForm, CountryForm, HouseForm, NeighborhoodForm, PswlaForm, ZawiForm, \
    BuySearchForm
from .models import Buy, City, Country, Neighborhood
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    context = {'form': BuySearchForm()}
    return render(request, "index.html", context)


def get_house_context(request, type):
    houses = Buy.objects.filter(type=type)

    query = request.GET.get("query")
    selected_city = request.META.get("HTTP_X_SELECTED_CITY", "all")
    selected_country = request.META.get("HTTP_X_SELECTED_COUNTRY", "all")
    selected_neighborhood = request.META.get("HTTP_X_SELECTED_NEIGHBORHOOD", "all")

    if selected_city != "all":
        houses = houses.filter(city_id=selected_city)
    if selected_country != "all":
        houses = houses.filter(country_id=selected_country)
    if selected_neighborhood != "all":
        houses = houses.filter(neighborhood_id=selected_neighborhood)
    if query is not None:
        search_query = (Q(owner_name__icontains=query) | Q(owner_phone__icontains=query) | Q(area__icontains=query)
                        | Q(documentation__icontains=query) | Q(direction__icontains=query)
                        | Q(max_price__icontains=query) | Q(min_price__icontains=query))
        houses = houses.filter(search_query)

    paginator = Paginator(houses.order_by("-date"), 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    context = {
        "title": f"{type} List",
        "page": page,
        "neighborhoods": Neighborhood.objects.all(),
        "countries": Country.objects.all(),
        "cities": City.objects.all(),
    }
    return context


class GetBuyList(View):
    def get(self, request):
        context = {'buys': Buy.objects.all()}
        return render(request, "list.html", context)


class BuySearchListView(ListView):
    model = Buy
    template_name = 'list.html'
    context_object_name = 'buys'

    def get_queryset(self):
        form = BuySearchForm(self.request.GET or None)

        if form.is_valid():
            type_value = form.cleaned_data['type']
            city_value = form.cleaned_data['city']
            country_value = form.cleaned_data['country']
            neighborhood_value = form.cleaned_data['neighborhood']
            area_value = form.cleaned_data['area']
            max_price_value = form.cleaned_data['max_price']
            min_price_value = form.cleaned_data['min_price']
            direction_value = form.cleaned_data['direction']
            documentation_value = form.cleaned_data['documentation']
            fence = form.cleaned_data['fence']
            electric = form.cleaned_data['electric']
            water = form.cleaned_data['water']
            water_depth = form.cleaned_data['water_depth']
            house = form.cleaned_data['house']
            tree = form.cleaned_data['tree']
            bill = form.cleaned_data['bill']

            filters = {
                key: value for key, value in {
                    'type': type_value,
                    'city': city_value,
                    'country': country_value,
                    'neighborhood': neighborhood_value,
                    'area__lte': area_value if area_value else None,
                    'max_price__lte': max_price_value if max_price_value else None,
                    'min_price__gte': min_price_value if min_price_value else None,
                    'direction': direction_value,
                    'documentation': documentation_value,
                    'fence': fence,
                    'electric': electric,
                    'water': water,
                    'water_depth__gte': water_depth,
                    'house': house,
                    'tree': tree,
                    'bill__lte': bill,
                }.items() if value is not None
            }

            queryset = Buy.objects.filter(**filters)
            return queryset

        else:
            return Buy.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BuySearchForm(self.request.GET or None)
        return context


class HouseView(ListView):
    def get(self, request):
        context = get_house_context(request, Buy.XANU)
        return render(request, "nwsenga/house/houses.html", context)


class GeHousesView(View):
    def get(self, request):
        context = get_house_context(request, Buy.XANU)
        return render(request, "nwsenga/house/list.html", context)


class AddHouseForm(View):
    def post(self, request):
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/house/add.html", {"form": form})

    def get(self, request):
        form = HouseForm()
        return render(request, "nwsenga/house/add.html", {"form": form})


class UpdateHouseForm(View):
    def post(self, request, pk):
        house = Buy.objects.get(id=pk)
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/house/update.html", {"form": form})

    def get(self, request, pk):
        house = Buy.objects.get(id=pk)
        form = HouseForm(instance=house)
        return render(request, "nwsenga/house/update.html", {"form": form, "house": house})


class PswlaView(ListView):
    def get(self, request):
        context = get_house_context(request, Buy.PSWLA)
        return render(request, "nwsenga/pswla/pswlas.html", context)


class GetPswlaView(View):
    def get(self, request):
        context = get_house_context(request, Buy.PSWLA)
        return render(request, "nwsenga/pswla/list.html", context)


class AddPswlaForm(View):
    def post(self, request):
        form = PswlaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/pswla/add.html", {"form": form})

    def get(self, request):
        form = PswlaForm()
        return render(request, "nwsenga/pswla/add.html", {"form": form})


class UpdatePswlaForm(View):
    def post(self, request, pk):
        pswla = Buy.objects.get(id=pk)
        form = PswlaForm(request.POST, instance=pswla)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/pswla/update.html", {"form": form})

    def get(self, request, pk):
        pswla = Buy.objects.get(id=pk)
        form = PswlaForm(instance=pswla)
        return render(request, "nwsenga/pswla/update.html", {"form": form, "pswla": pswla})


class BaxView(ListView):
    def get(self, request):
        context = get_house_context(request, Buy.BAX)
        return render(request, "nwsenga/bax/bax.html", context)


class GetBaxView(View):
    def get(self, request):
        context = get_house_context(request, Buy.BAX)
        return render(request, "nwsenga/bax/list.html", context)


class AddBaxForm(View):
    def post(self, request):
        form = BaxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/bax/add.html", {"form": form})

    def get(self, request):
        form = BaxForm()
        return render(request, "nwsenga/bax/add.html", {"form": form})


class UpdateBaxForm(View):
    def post(self, request, pk):
        bax = Buy.objects.get(id=pk)
        form = BaxForm(request.POST, instance=bax)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/bax/update.html", {"form": form})

    def get(self, request, pk):
        bax = Buy.objects.get(id=pk)
        form = BaxForm(instance=bax)
        return render(request, "nwsenga/bax/update.html", {"form": form, "bax": bax})


class ZawiView(ListView):
    def get(self, request):
        context = get_house_context(request, Buy.ZAWI)
        return render(request, "nwsenga/zawi/zawis.html", context)


class GetZawiView(View):
    def get(self, request):
        context = get_house_context(request, Buy.ZAWI)
        return render(request, "nwsenga/zawi/list.html", context)


class AddZawiForm(View):
    def post(self, request):
        form = ZawiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/zawi/add.html", {"form": form})

    def get(self, request):
        form = ZawiForm()
        return render(request, "nwsenga/zawi/add.html", {"form": form})


class UpdateZawiForm(View):
    def post(self, request, pk):
        zawi = Buy.objects.get(id=pk)
        form = ZawiForm(request.POST, instance=zawi)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "nwsenga/zawi/update.html", {"form": form})

    def get(self, request, pk):
        zawi = Buy.objects.get(id=pk)
        form = ZawiForm(instance=zawi)
        return render(request, "nwsenga/zawi/update.html", {"form": form, "zawi": zawi})


class CityList(ListView):
    def get(self, request):
        cities = City.objects.all()

        query = request.GET.get("query")
        if query is not None:
            cities = cities.filter(name__icontains=query).order_by("-id")
        paginator = Paginator(cities, 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "cities List",
            "page": page,
        }
        return render(request, "management/cities.html", context)


class GetCityList(View):
    def get(self, request):
        cities = City.objects.all()

        query = request.GET.get("query")
        if query is not None:
            cities = cities.filter(name__icontains=query).order_by("-id")
        paginator = Paginator(cities, 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "cities List",
            "page": page,
        }
        return render(request, "management/city/list.html", context)


class AddCityForm(View):
    def post(self, request):
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/city/add.html", {"form": form})

    def get(self, request):
        form = CityForm()
        return render(request, "management/city/add.html", {"form": form})


class UpdateCityForm(View):
    def post(self, request, pk):
        city = City.objects.get(id=pk)
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/city/update.html", {"form": form})

    def get(self, request, pk):
        city = City.objects.get(id=pk)
        form = CityForm(instance=city)
        return render(request, "management/city/update.html", {"form": form, "city": city})


class CountryList(ListView):
    def get(self, request):
        countries = Country.objects.all()

        query = request.GET.get("query")
        if query is not None:
            countries = countries.filter(name__icontains=query).order_by("-id")
        paginator = Paginator(countries, 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "countries List",
            "page": page,
            "cities": City.objects.all(),
        }
        return render(request, "management/countries.html", context)


class GetCountryList(View):
    def get(self, request):
        countries = Country.objects.all()
        selected_city = request.META.get("HTTP_X_SELECTED_CITY", "all")

        query = request.GET.get("query")
        if query is not None:
            countries = countries.filter(name__icontains=query)
        if selected_city != "all":
            countries = countries.filter(city_id=selected_city)
        paginator = Paginator(countries.order_by("-id"), 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "cities List",
            "page": page,
        }
        return render(request, "management/country/list.html", context)


class AddCountryForm(View):
    def post(self, request):
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/country/add.html", {"form": form})

    def get(self, request):
        form = CountryForm()
        return render(request, "management/country/add.html", {"form": form})


class UpdateCountryForm(View):
    def post(self, request, pk):
        country = Country.objects.get(id=pk)
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/country/update.html", {"form": form})

    def get(self, request, pk):
        country = Country.objects.get(id=pk)
        form = CountryForm(instance=country)
        return render(request, "management/country/update.html", {"form": form, "country": country})


class GarakList(ListView):
    def get(self, request):
        garaks = Neighborhood.objects.all()

        query = request.GET.get("query")
        selected_city = request.META.get("HTTP_X_SELECTED_CITY", "all")
        selected_country = request.META.get("HTTP_X_SELECTED_COUNTRY", "all")

        if selected_city != "all":
            garaks = garaks.filter(country__city_id=selected_city)
        if selected_country != "all":
            garaks = garaks.filter(country_id=selected_country)

        if query is not None:
            garaks = garaks.filter(name__icontains=query)

        paginator = Paginator(garaks.order_by("-id"), 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "garak List",
            "page": page,
            "countries": Country.objects.all(),
            "cities": City.objects.all(),
        }
        return render(request, "management/garaks.html", context)


class GetGarakList(View):
    def get(self, request):
        garaks = Neighborhood.objects.all()

        query = request.GET.get("query")
        if query is not None:
            garaks = garaks.filter(name__icontains=query).order_by("-id")

        selected_city = request.META.get("HTTP_X_SELECTED_CITY", "all")
        selected_country = request.META.get("HTTP_X_SELECTED_COUNTRY", "all")
        if selected_city != "all":
            garaks = garaks.filter(country__city_id=selected_city)
        if selected_country != "all":
            garaks = garaks.filter(country_id=selected_country)
        paginator = Paginator(garaks, 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)

        context = {
            "title": "garak List",
            "page": page,
        }
        return render(request, "management/garak/list.html", context)


class AddGarakForm(View):
    def post(self, request):
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/garak/add.html", {"form": form})

    def get(self, request):
        form = NeighborhoodForm()
        return render(request, "management/garak/add.html", {"form": form})


class UpdateGarakForm(View):
    def post(self, request, pk):
        garak = Neighborhood.objects.get(id=pk)
        form = NeighborhoodForm(request.POST, instance=garak)
        if form.is_valid():
            form.save()
            return HttpResponseClientRefresh()
        else:
            return render(request, "management/garak/update.html", {"form": form})

    def get(self, request, pk):
        garak = Neighborhood.objects.get(id=pk)
        form = NeighborhoodForm(instance=garak)
        return render(request, "management/garak/update.html", {"form": form, "garak": garak})
