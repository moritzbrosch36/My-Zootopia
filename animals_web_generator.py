import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

animal_data = load_data("animals_data.json")

html_output = """<html>
    <head>
        <style>
        @gray-darker:               #444444;
        @gray-dark:                 #696969;
        @gray:                      #999999;
        @gray-light:                #cccccc;
        @gray-lighter:              #ececec;
        @gray-lightest:             lighten(@gray-lighter,4%);

        html {
          background-color: #ffe9e9;
        }

        h1 {
            text-align: center;
            font-size: 40pt;
            font-weight: normal;
        }

        body {
          font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
          font-style: normal;
          font-weight: 400;
          letter-spacing: 0;
          padding: 1rem;
          text-rendering: optimizeLegibility;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
          -moz-font-feature-settings: "liga" on;
          width: 900px;
          margin: auto;
        }

        .cards {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .cards__item {
          background-color: white;
          border-radius: 0.25rem;
          box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
          overflow: hidden;
          padding: 1rem;
          margin: 50px;
        }

        .card__title {
          color: @gray-dark;
          font-size: 1.25rem;
          font-weight: 300;
          letter-spacing: 2px;
          text-transform: uppercase;
        }

        .card__text {
          flex: 1 1 auto;
          font-size: 0.95rem;
          line-height: 2;
          margin-bottom: 1.25rem;
        }
        </style>
    </head>
    <body>
        <h1>My Animal Repository</h1>
        <ul class="cards">
"""

# für jedes Tier eine "Karte" bauen
for data in animal_data:
    info = {
        "Name": data.get("name"),
        "Diet": data.get("characteristics", {}).get("diet"),
        "Type": data.get("characteristics", {}).get("type"),
        "Locations": ", ".join(data.get("locations", [])) if data.get("locations") else None
    }

    html_output += '<li class="cards__item">\n'
    html_output += f'<h2 class="card__title">{info["Name"]}</h2>\n'
    html_output += '<div class="card__text">\n'
    for key, value in info.items():
        if key != "Name" and value is not None:  # Name schon als Titel oben
            html_output += f'<p><strong>{key}:</strong> {value}</p>\n'
    html_output += "                </div>\n"
    html_output += "            </li>\n"

html_output += """        </ul>
    </body>
</html>"""

# speichern
with open("animals.html", "w") as f:
    f.write(html_output)

print("✅ HTML wurde in animals.html gespeichert")
