from flask import Flask, render_template, request, redirect, url_for, flash
from discord import Webhook, AsyncWebhookAdapter, Colour, Embed, RequestsWebhookAdapter

app = Flask(__name__)


def send_shoes_wh(shoes_name, zalando_link, image_link, pas, hours, price):
    webhook = Webhook.partial(
        1038163316821995581, 'HG9fLuBwgiKwUE-O2BdJCGmaxR--QGGZWD7P4BSuLVmtggrQ5FhqD57EBvw87iufULNe', adapter=RequestsWebhookAdapter())

    try:
        e = Embed(title=shoes_name, color=0xa84300, url=zalando_link)
        e.set_author(
            name="Zalando", icon_url="https://cdn.discordapp.com/attachments/790241201985945601/1040657854073405460/zal.png")
        e.set_thumbnail(url=image_link)
        e.add_field(name=f"**Release**", value="```Zalando```", inline=False)
        e.add_field(name="Retail Price 💶", value=f"{price}€", inline=True)
        e.add_field(name="PAS 💰", value=f"{pas}€", inline=True)
        e.add_field(name="Heures ⏰", value=f"{hours}", inline=True)
        e.set_footer(
            icon_url="https://cdn.discordapp.com/icons/1029014348934426754/4834ab38e38009befc4778123a88a93a.webp?size=96", text="💸💸")
        webhook.send(embed=e, username='planing zal')
    except:
        e = Embed(title="Une erreur est survenue", color=0xa84300)
        e.set_author(
            name="Error webhook", icon_url="https://cdn.discordapp.com/attachments/790241201985945601/1040657854073405460/zal.png")
        e.set_thumbnail(
            url="https://thumbs.dreamstime.com/z/erreur-109026446.jpg")
        e.add_field(name=f"**Error**", value="```Embed```", inline=False)
        e.set_footer(
            icon_url="https://cdn.discordapp.com/icons/1029014348934426754/4834ab38e38009befc4778123a88a93a.webp?size=96", text="💸💸")
        webhook.send(embed=e, username='planing zal')


def send_day_wh(day, date):
    webhook = Webhook.partial(
        1038163316821995581, 'HG9fLuBwgiKwUE-O2BdJCGmaxR--QGGZWD7P4BSuLVmtggrQ5FhqD57EBvw87iufULNe', adapter=RequestsWebhookAdapter())
    try:
        e = Embed(title=f"{day} {date}", color=0xa84300)
        webhook.send(embed=e, username='planing zal')
    except:
        e = Embed(title="Une erreur est survenue", color=0xa84300)
        e.set_author(
            name="Error webhook", icon_url="https://cdn.discordapp.com/attachments/790241201985945601/1040657854073405460/zal.png")
        e.set_thumbnail(
            url="https://thumbs.dreamstime.com/z/erreur-109026446.jpg")
        e.add_field(name=f"**Error**", value="```Embed```", inline=False)
        e.set_footer(
            icon_url="https://cdn.discordapp.com/icons/1029014348934426754/4834ab38e38009befc4778123a88a93a.webp?size=96", text="💸💸")
        webhook.send(embed=e, username='planing zal')


@app.route("/shoes", methods=["GET", "POST"])
def shoes():
    try:
        shoes_name = request.form['name']
        zalando_link = request.form['zlink']
        image_link = request.form['ilink']
        price = request.form['price']
        pas = request.form['pas']
        hours = request.form['hours']
        password = request.form['mdp']

        if password == "kishta":

            send_shoes_wh(shoes_name, zalando_link,
                          image_link, pas, hours, price)

        else:
            return render_template("shoes.html")

        return render_template('index.html')
    except:
        return render_template("shoes.html")


@app.route("/next-day", methods=["GET", "POST"])
def next():
    try:
        day = request.form['day']
        date = request.form['date']

        password = request.form['mdp']
        if password == "kishta":

            send_day_wh(day, date)

        else:
            return render_template("next.html")

        return render_template('index.html')
    except:
        return render_template("next.html")


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
