import requests
from bs4 import BeautifulSoup

FREEZER = 'https://www.sulpak.kz/g/holodilnik_samsung_rb33a32n0sawt_25_1183/astana'
SAMSUNG = 'https://www.sulpak.kz/g/smartfoniy_samsung_galaxy_z_fold4_5g_512gb_gray/astana'
IPHONE = 'https://www.sulpak.kz/g/smartfoniy_apple_iphone_14_pro_max_128gb_space_black_mqc63rua/astana'
ROUTER = 'https://www.sulpak.kz/g/modemiy_i_setevoe_oborudovanie_tp_link_archer_ax53/astana'
VICTUS = 'https://www.sulpak.kz/g/noutbuki_victus_16_e1047ci__725w5ea/astana'
MACBOOK = 'https://www.sulpak.kz/g/noutbuk_apple_macbook_air_13_8gb256gb_ssd_space_gray_mgn63_62_2067/astana'
VACUUM_CLEANER = 'https://www.sulpak.kz/g/piylesos_tefal_tw3731/astana'
MULTICOOKER = 'https://www.sulpak.kz/g/multivarka_moulinex_fuzzy_logic_mk707832/astana'
PLATE = ' https://www.sulpak.kz/g/plita_kombinirovannaya_dauscher_e9416lx_16_666/astana'
RECTIFIER = 'https://www.sulpak.kz/g/viypryamitel_dlya_volos_remington_s9500/astana'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'}

def get_price(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.find_all("div", {"class": "product__price"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('нет данных')
    return result