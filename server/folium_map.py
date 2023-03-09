import folium
from folium import plugins
from geopy.geocoders import Nominatim
import webbrowser

def folium_map(locations):

    geolocator = Nominatim(user_agent='myapp')

    # create the map
    m = folium.Map(location=locations[0], zoom_start=13)

    for i in range(0,len(locations)-1):

        # Define a custom icon with the number
        icon = plugins.BeautifyIcon(number=i, icon_shape='marker', background_color='#00FF00', inner_icon_style='font-size:14px;')

        # get the location name
        location = geolocator.reverse('{}, {}'.format(locations[i][0], locations[i][1]))
        place_name = location.address

        # create the Marker for stops
        if i == 0 :
            folium.Marker(
                locations[i],
                popup=folium.Popup(f"{i}", parse_html=True), 
                tooltip=place_name,
                icon=folium.CustomIcon('images/icon.png', icon_size=(40,40))
            ).add_to(m)
        else:
            folium.Marker(
                locations[i], 
                popup=folium.Popup(f"{i}",parse_html=True),
                tooltip=place_name,
                icon = icon
            ).add_to(m)

    # draw a line between stops
    for i in range(0,len(locations)-1):
        color = "red" if i == 0 else "blue"
        folium.PolyLine(locations=[locations[i],
                locations[i+1]],
                color= color,
                weight=5,).add_to(m)
        
    # generate and save the map as html file
    m.save('route.html')
    
    # open the html file in the browser
    webbrowser.open_new_tab("route.html")
