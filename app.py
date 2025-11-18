from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "124123131221"   


@app.route("/", methods=["GET", "POST"])
@app.route("/search", methods=["GET", "POST"])
def search():
    resultados = None

    if request.method == "POST":
        buscar = request.form.get("buscar")

        
        if not buscar:
            flash(" Debes escribir un alimento para buscar.", "warning")
            return redirect(url_for("search"))

       
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={buscar}&search_simple=1&action=process&json=1"

        try:
            resp = requests.get(url)
            data = resp.json()
        except Exception:
            flash(" Error al conectar con la API.", "danger")
            return redirect(url_for("search"))

        
        if "products" in data and len(data["products"]) > 0:
            resultados = data["products"]
        else:
            flash(" No se encontraron resultados.", "danger")

    return render_template("search.html", resultados=resultados)


if __name__ == "__main__":
    app.run(debug=True)

# Profesor, 
# Quiero aclarar por qué algunos cambios dentro del repositorio aparecen con el nombre de Nolasco. En una ocasión pasada, 
# desde mi computadora le ayudé a Nolasco a revisar un código que no le funcionaba, y para poder apoyarlo inicié sesión con su cuenta en Git. Debido a eso, 
# Git guardó de forma automática su información en la configuración global del sistema (git config --global), y por eso los commits posteriores quedaron registrados bajo su nombre en lugar del mío, aunque yo los haya realizado.
# Ya corregí la configuración para que los futuros cambios aparezcan correctamente a mi nombre.
