import requests

parse_list = []

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for pars_elem_1 in response_parse:
    if pars_elem_1.startswith("$"):
        for pars_elem_2 in pars_elem_1.split("</span>"):
            if pars_elem_2.startswith("$") and pars_elem_2[1].isdigit():
                parse_list.append(pars_elem_2)


bitcoin_er = parse_list[1]
print("Bitcoin:")
print(bitcoin_er )