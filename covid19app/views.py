from django.shortcuts import render
import requests

# Create your views here.
# def homepage(request):
#     return render(request, 'index.html')


covid_api = 'https://covid-api.mmediagroup.fr/v1/cases'
covid_api_country = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'


def homepage(request):
    covid_all = requests.get(covid_api)
    covid_dict = covid_all.json()
    no_fatalities = []
    for i in covid_dict:
        if covid_dict[i]['All']['deaths'] == 0:
            no_fatalities.append(i)

    return render(request, 'index.html', {
        # 'all_data':all_data,
        'covid_dict': covid_dict,
        'no_fatalities': no_fatalities,
    })


def get_data(request):
    covid_all = requests.get(covid_api)
    covid_dict = covid_all.json()

    inputed_country = request.POST.get("selected_counrty")

    selected_counrty = covid_api_country.format(country=inputed_country)
    get_data = requests.get(selected_counrty)
    get_data_dict = get_data.json()
    if inputed_country == "Country's name":
        country = "not selected"
        confirmed = ""
        recovered = ""
        deaths = ""
        population = ""
        capital_city = ""
    else:
        country = get_data_dict['All']['country']
        confirmed = get_data_dict['All']['confirmed']
        recovered = get_data_dict['All']['recovered']
        deaths = get_data_dict['All']['deaths']
        population = get_data_dict['All']['population']
        capital_city = get_data_dict['All']['capital_city']
    return render(request, 'get_data.html', {
        # 'all_data':all_data,
        'covid_dict': covid_dict,
        'get_data_dict': get_data_dict,
        'country': country,
        'confirmed': confirmed,
        'recovered': recovered,
        'deaths': deaths,
        'population': population,
        'deaths': deaths,
        'capital_city': capital_city,
    })
