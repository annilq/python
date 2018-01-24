import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle

from country_code import get_country_code

filename = "population_data.json"

with open(filename) as fileObj:
    pop_data = json.load(fileObj)

populations = {}
for nation in pop_data:
    if nation["Year"] == "2000":
        country_name = nation["Country Name"]
        country_code = get_country_code(country_name)
        if country_code:
            # int不能直接将浮点数的字符串转换为整形
            population = int(float(nation["Value"]))
            print(country_code, population)
            populations[country_code] = population
        else:
            print("error", country_code)
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 10000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'North, Central, and South America'
wm.add('pop less than', cc_pops_1)
wm.add('pop less than', cc_pops_2)
wm.add('others', cc_pops_3)
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#  'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')