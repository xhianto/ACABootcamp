from ..app import app, db_session
from flask import render_template, request, flash
import requests
from ..models.people import People
from datetime import datetime
import os

@app.route("/")
def index():

    if not request.args.get("dir"):
        person = db_session.query(People).order_by(People.id.asc()).first()
    else:
        pass

    return render_template("index.html", person=person)

@app.route("/add-people/", methods=["GET", "POST"])
def add_people():
    template = "add_people.html"
    if request.method == "POST":
        try:
            qty = int(request.form.get("qty"))
        except ValueError:
            flash("Expecting a number", "error")

        if 0 < qty <= 10:
            pass
            for _ in range(qty):
                r = requests.get("https://randomuser.me/api")
                if r.status_code == 200:
                    data = r.json()
                    person = data["results"][0]
                    p = People(
                        person["name"]["first"],
                        person["name"]["last"],
                        person["gender"][:1].upper(),
                        person["email"],
                        datetime.strptime(person["dob"]["date"], '%Y-%m-%dT%H:%M:%S.%fZ')
                    )
                    db_session.add(p)
                    db_session.flush()
                    db_session.commit()

                    person_id = p.id
                    pic_uri = person["picture"]["large"]
                    req_pic = requests.get(pic_uri)
                    pic_ext = pic_uri[pic_uri.rfind(".")+1:]
                    if req_pic.status_code == 200:
                        with open(f".\\flaskr\\static\\img\\people\\{person_id}.{pic_ext}", "wb") as f:
                            f.write(req_pic.content)
                            f.close()
                    """       
                    img_url = person["picture"]["large"]
                    file_ext = img_url[pic_uri.rfind(".")+1:]
                    filename = os.path.join(app.root_path, "static/img/people", "".join([str(person_id), file_ext]))
                    img_resp = requests.get(img_url)
                    if img_resp.status_code == 200
                        with open(filename, "wb") as f:
                            f.write(img_resp.content)
                            f.close
                    """



    return render_template(template)
