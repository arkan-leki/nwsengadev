"""
URL configuration for Nwsenga app.
"""
from coreNwsenga import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("buy/list", views.GetBuyList.as_view(), name="buys-list"),
    path("buy/search", views.BuySearchListView.as_view(), name="search_view"),

    path("city/list", views.CityList.as_view(), name="city-list"),
    path("city/get", views.GetCityList.as_view(), name="get-city"),
    path("city/add", views.AddCityForm.as_view(), name="add-city"),
    path("city/update/<int:pk>", views.UpdateCityForm.as_view(), name="update-city"),

    path("country/list", views.CountryList.as_view(), name="country-list"),
    path("country/get", views.GetCountryList.as_view(), name="get-country"),
    path("country/add", views.AddCountryForm.as_view(), name="add-country"),
    path("country/update/<int:pk>", views.UpdateCountryForm.as_view(), name="update-country"),

    path("garak/list", views.GarakList.as_view(), name="garak-list"),
    path("garak/get", views.GetGarakList.as_view(), name="get-garak"),
    path("garak/add", views.AddGarakForm.as_view(), name="add-garak"),
    path("garak/update/<int:pk>", views.UpdateGarakForm.as_view(), name="update-garak"),

    # house
    path("house/list", views.HouseView.as_view(), name="house-list"),
    path("house/get", views.GeHousesView.as_view(), name="get-house"),
    path("house/add", views.AddHouseForm.as_view(), name="add-house"),
    path("house/update/<int:pk>", views.UpdateHouseForm.as_view(), name="update-house"),

    # pswla
    path("pswla/list", views.PswlaView.as_view(), name="pswla-list"),
    path("pswla/get", views.GetPswlaView.as_view(), name="get-pswla"),
    path("pswla/add", views.AddPswlaForm.as_view(), name="add-pswla"),
    path("pswla/update/<int:pk>", views.UpdatePswlaForm.as_view(), name="update-pswla"),

    # bax
    path("bax/list", views.BaxView.as_view(), name="bax-list"),
    path("bax/get", views.GetBaxView.as_view(), name="get-bax"),
    path("bax/add", views.AddBaxForm.as_view(), name="add-bax"),
    path("bax/update/<int:pk>", views.UpdateBaxForm.as_view(), name="update-bax"),

    # zawi
    path("zawi/list", views.ZawiView.as_view(), name="zawi-list"),
    path("zawi/get", views.GetZawiView.as_view(), name="get-zawi"),
    path("zawi/add", views.AddZawiForm.as_view(), name="add-zawi"),
    path("zawi/update/<int:pk>", views.UpdateZawiForm.as_view(), name="update-zawi"),

]
