def get_rates(request, number):
    responce = request.json()
    result = f"{responce[0]['Date']}.\n\n"
    for i in range(0, number):
        dict_id = responce[i]
        nominal, money_type, rate = dict_id['Nominal'], dict_id['Ccy'], dict_id['Rate'] 
        result += f"{i+1}) {nominal} {money_type} - {rate} сум\n"
    return result

def get_images(request):
    responce = request.json()
    return responce['message']
