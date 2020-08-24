import folium
from folium.plugins import MarkerCluster
import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    marker_data = pd.read_csv('data/locations.csv')
    marker_data.columns = marker_data.columns.str.strip()
    marker_dataset = marker_data.sample(n=20)
    ua_if = [marker_dataset["Y"].mean(), marker_dataset["X"].mean()]
    ua_if_map = folium.Map(
        location=ua_if,
        zoom_start=9
    )

    # WITHOUT CLUSTERING
    # for row in marker_dataset.itertuples():
    #     ua_if_map.add_child(
    #         folium.Marker(
    #             location=[row.Y, row.X],
    #             popup=row.ID,
    #             tooltip=row.NAME,
    #             icon=folium.Icon(
    #                 icon=row.ICON,
    #                 color=row.COLOR
    #             )
    #         )
    #     )

    # W/ CLUSTERING
    mc = MarkerCluster()
    for row in marker_dataset.itertuples():
        marker_html = """<div class="marker_popup" style="min-width: 320px;"><div class="title" style="padding: 10px;"><h1>""" \
                      + row.NAME + """</h1><br><p style="font-size: 20px;font-style: italic;">""" \
                      + row.DESC + """</p></div><div class="contacts"><ul style="list-style-type: none;"><li style="font-size: 15px;"><b>Phone: </b>""" \
                      + str(row.PHONE) + """</li><li style="font-size: 15px;"><b>Email: </b>""" \
                      + str(row.EMAIL) + """</li><li style="font-size: 15px;"><b>Website: </b>""" \
                      + str(row.WEBSITE) + """</li><li style="font-size: 15px;"><b>Instagram: </b>""" \
                      + str(row.INSTAGRAM) + """</li><li style="font-size: 15px;"><b>Facebook: </b>""" \
                      + str(row.FB) + """</li></ul></div>"""
        mc.add_child(
            folium.Marker(
                location=[row.Y, row.X],
                popup=marker_html,
                tooltip=row.ID
            )
        )
    ua_if_map.add_child(mc)

    return ua_if_map._repr_html_()


    # with open("data/marker-1.json", "r") as marker:
    #     # marker_data = json.loads(marker.read())
    #     json_object = json.load(marker)
    #     # print(json_object[0]['tooltip'])
    #     for title in json_object:
    #         print(title['title'])
    #     for tooltip in json_object:
    #         print(tooltip['tooltip'])
        # title = marker_data['marker_001']['title']
        # description = marker_data['marker_001']['description']
        # phone = marker_data['marker_001']['contacts']['phone']
        # email = marker_data['marker_001']['contacts']['email']
        # website = marker_data['marker_001']['contacts']['website']
        # instagram = marker_data['marker_001']['contacts']['instagram']
        # facebook = marker_data['marker_001']['contacts']['facebook']

        # html = """<div class="marker_popup" style="min-width: 320px;"><div class="title" style="padding: 10px;"><h1>""" \
               # + str(title) +"""</h1><br><p style="font-size: 20px;font-style: italic;">""" \
               # + description +"""</p></div><div class="contacts"><ul style="list-style-type: none;"><li style="font-size: 15px;">""" \
               # + phone +"""</li><li style="font-size: 15px;">""" \
               # + email +"""</li><li style="font-size: 15px;">""" \
               # + website +"""</li><li style="font-size: 15px;">""" \
               # + instagram +"""</li><li style="font-size: 15px;">""" \
               # + facebook +"""</li></ul></div>"""
        # marker_one = folium.Marker(
        #     location=location_one,
        #     popup=html,
        #     tooltip=tooltip
        # )
    # marker_one.add_to(folium_map)


if __name__ == '__main__':
    app.run(debug=True)
