from flask import Flask, render_template, request,  redirect
import csv


def write_to_file(data):
    with open("save.txt", mode="a") as mydata:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        return mydata.write(f"\n Email:{email}, subject:{subject}, Message :{message}")


def write_to_csv(data):
    with open("savefile.csv", "a", newline="") as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        info_writer = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        info_writer.writerow([email, subject, message])


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submitt():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "something went wrong"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
