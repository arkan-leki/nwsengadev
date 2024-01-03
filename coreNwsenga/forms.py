from django import forms
from django.forms import ModelForm
from .models import Buy, City, Country, Neighborhood


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        labels = {
            "name": "ناو",
        }

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["name"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ["name", "city"]
        labels = {
            "name": "ناو",
            "city": "شار",
        }

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["name", "city"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False


class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ["name", "country"]
        labels = {
            "name": "ناو",
            "country": "ناحیە",
        }

    def __init__(self, *args, **kwargs):
        super(NeighborhoodForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["name", "country"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False


class HouseForm(ModelForm):
    class Meta:
        model = Buy
        fields = [
            # "type",
            "city",
            "country",
            "neighborhood",
            "area",
            "documentation",
            "direction",
            "max_price",
            "min_price",
            "owner_name",
            "owner_phone",
            "link",
            "notes",
        ]
        labels = {
            "type": "جۆر",
            "city": "شار",
            "country": "ناحیە",
            "neighborhood": "گەڕەک",
            "area": "روبەر",
            "documentation": "سەند",
            "direction": "ئاراستە",
            "max_price": "بەرزترین نرخ",
            "min_price": "کەمترین نرخ",
            "owner_name": "ناوی خاوەن",
            "owner_phone": "ژ.م خاوەن",
            "notes": "تێبینی",
            "link": "راپێچ",
        }

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["type", "city", "country", "neighborhood"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False

    def save(self, commit=True):
        # Set home_phone_leader to "OFF" before saving
        instance = super(HouseForm, self).save(commit=False)
        instance.type = Buy.XANU

        if commit:
            instance.save()

        return instance


class PswlaForm(ModelForm):
    class Meta:
        model = Buy
        fields = [
            # "type",
            "city",
            "country",
            "neighborhood",
            "area",
            "documentation",
            "direction",
            "max_price",
            "min_price",
            "owner_name",
            "owner_phone",
            "bill",
            "installment",
            "advance_payment",
            "link",
            "notes",
        ]
        labels = {
            "type": "جۆر",
            "city": "شار",
            "country": "ناحیە",
            "neighborhood": "گەڕەک",
            "area": "روبەر",
            "documentation": "سەند",
            "direction": "ئاراستە",
            "max_price": "بەرزترین نرخ",
            "min_price": "کەمترین نرخ",
            "owner_name": "ناوی خاوەن",
            "owner_phone": "ژ.م خاوەن",
            "bill": "جۆری پسولە",
            "installment": "پێشەکی",
            "advance_payment": "کۆی پسولە",
            "notes": "تێبینی",
            "link": "راپێچ",
        }

    def __init__(self, *args, **kwargs):
        super(PswlaForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["type", "city", "country", "neighborhood"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False

    def save(self, commit=True):
        # Set home_phone_leader to "OFF" before saving
        instance = super(PswlaForm, self).save(commit=False)
        instance.type = Buy.PSWLA

        if commit:
            instance.save()

        return instance


class BaxForm(ModelForm):
    class Meta:
        model = Buy
        fields = [
            # "type",
            "city",
            "country",
            "neighborhood",
            "area",
            "documentation",
            "direction",
            "max_price",
            "min_price",
            "owner_name",
            "owner_phone",
            "fence",
            "electric",
            "water",
            "water_depth",
            "house",
            "tree",
            "link",
            "notes",
        ]
        labels = {
            "type": "جۆر",
            "city": "شار",
            "country": "ناحیە",
            "neighborhood": "گەڕەک",
            "area": "روبەر",
            "documentation": "سەند",
            "direction": "ئاراستە",
            "max_price": "بەرزترین نرخ",
            "min_price": "کەمترین نرخ",
            "owner_name": "ناوی خاوەن",
            "owner_phone": "ژ.م خاوەن",
            "fence": "حسار",
            "electric": "کارەبا",
            "water": "ئاو",
            "water_depth": "قوڵی ئاو",
            "house": "خانوو",
            "tree": "درەخت",
            "notes": "تێبینی",
            "link": "راپێچ",
        }

    def __init__(self, *args, **kwargs):
        super(BaxForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["type", "city", "country", "neighborhood"]
        chekcboxs = ["fence", "electric", "water", "house", "tree"]

        for field_name, field in self.fields.items():
            if field_name not in chekcboxs:
                field.widget.attrs.update({"class": common_class})
            else:
                field.widget.attrs.update({
                                              "class": " w-6 h-6 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False

    def save(self, commit=True):
        # Set home_phone_leader to "OFF" before saving
        instance = super(BaxForm, self).save(commit=False)
        instance.type = Buy.BAX

        if commit:
            instance.save()

        return instance


class ZawiForm(ModelForm):
    class Meta:
        model = Buy
        fields = [
            # "type",
            "city",
            "country",
            "neighborhood",
            "area",
            "documentation",
            "direction",
            "max_price",
            "min_price",
            "owner_name",
            "owner_phone",
            "link",
            "notes",
        ]
        labels = {
            "type": "جۆر",
            "city": "شار",
            "country": "ناحیە",
            "neighborhood": "گەڕەک",
            "area": "روبەر",
            "documentation": "سەند",
            "direction": "ئاراستە",
            "max_price": "بەرزترین نرخ",
            "min_price": "کەمترین نرخ",
            "owner_name": "ناوی خاوەن",
            "owner_phone": "ژ.م خاوەن",
            "notes": "تێبینی",
            "link": "راپێچ",
        }

    def __init__(self, *args, **kwargs):
        super(ZawiForm, self).__init__(*args, **kwargs)

        # Add custom classes to widget's attrs dictionary
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["type", "city", "country", "neighborhood"]

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": common_class})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False

    def save(self, commit=True):
        # Set home_phone_leader to "OFF" before saving
        instance = super(ZawiForm, self).save(commit=False)
        instance.type = Buy.ZAWI

        if commit:
            instance.save()

        return instance


class BuySearchForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['type', 'city', 'country', 'neighborhood', 'area',  'documentation', 'direction',
                  'max_price', 'min_price',
                  'bill', 'fence', 'electric', 'water', 'water_depth', 'house', 'tree']
        
        labels = {
            "type": "جۆر",
            "city": "شار",
            "country": "ناحیە",
            "neighborhood": "گەڕەک",
            "area": "روبەر",
            "documentation": "سەند",
            "direction": "ئاراستە",
            "max_price": "بەرزترین نرخ",
            "min_price": "کەمترین نرخ",
            "fence": "حسار",
            "electric": "کارەبا",
            "water": "ئاو",
            "house": "خانوو",
            "tree": "درەخت",
            "bill": "جۆری پسولە",
            "installment": "پێشەکی",
            "advance_payment": "کۆی پسولە",
        }

    def __init__(self, *args, **kwargs):
        super(BuySearchForm, self).__init__(*args, **kwargs)
        common_class = "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"

        # Set only specific fields as required
        required_fields = ["type", "city"]
        chekcboxs = ["fence", "electric", "water", "house", "tree"]

        for field_name, field in self.fields.items():
            if field_name not in chekcboxs:
                field.widget.attrs.update({"class": common_class})
            else:
                field.widget.attrs.update({"class": " w-6 h-6 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"})

            if field_name in required_fields:
                field.required = True
            else:
                field.required = False