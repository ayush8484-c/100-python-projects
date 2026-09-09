import colorgram

rgb_colors = []

colors = colorgram.extract('Damien_Hirst_Spot_Painting.jpeg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

color_list = rgb_colors
print(color_list)