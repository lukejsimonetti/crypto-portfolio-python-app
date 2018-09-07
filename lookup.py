from Tkinter import *
import requests
import json
import os
os.system('clear')
#####################
def red_green(amount):
    if amount >= 0.00:
        return "green"
    else:
        return "red"

root = Tk()

name = Label(root, text="Luke Simonett", bg="grey", fg="white")
name.grid(row=0, column=0, sticky=N+S+E+W)

name = Label(root, text="Name", bg="white")
name.grid(row=0, column=0, sticky=N+S+E+W)

rank = Label(root, text="Rank", bg="grey")
rank.grid(row=0, column=1, sticky=N+S+E+W)

current_price = Label(root, text=" Current Price", bg="white")
current_price.grid(row=0, column=2, sticky=N+S+E+W)

price_paid = Label(root, text="Price Paid", bg="grey")
price_paid.grid(row=0, column=3, sticky=N+S+E+W)

profit_loss_per_coin = Label(root, text="P/L per Coin", bg="white")
profit_loss_per_coin.grid(row=0, column=4, sticky=N+S+E+W)

one_hr_change = Label(root, text="1hr Change", bg="grey")
one_hr_change.grid(row=0, column=5, sticky=N+S+E+W)

tf_hr_change = Label(root, text="24hr Change", bg="white")
tf_hr_change.grid(row=0, column=6, sticky=N+S+E+W)

seven_day_change = Label(root, text="7 Day Change", bg="grey")
seven_day_change.grid(row=0, column=7, sticky=N+S+E+W)

current_value = Label(root, text="Current Value", bg="white")
current_value.grid(row=0, column=8, sticky=N+S+E+W)

profit_loss_total = Label(root, text="P/L Total", bg="grey")
profit_loss_total.grid(row=0, column=9, sticky=N+S+E+W)

def lookup():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    api = json.loads(api_request.content)
    my_portfolio = [
    {
        "sym": "BTC",
        "amount_owned": 0,
        "price_paid_per": 0
    },
    {
        "sym": "XRP",
        "amount_owned": 5000,
        "price_paid_per": .80
    },
    {
        "sym": "ETH",
        "amount_owned": 2000,
        "price_paid_per": .90 
    },
    {
        "sym": "EOS",
        "amount_owned": 1000,
        "price_paid_per": 2.10 
    },
    {
        "sym": "XLM",
        "amount_owned": 1500,
        "price_paid_per": .35
    }
    ]
    portfolio_profit_loss = 0
    row_index = 1
    total_current_value = 0
    for x in api:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x["price_usd"])
                profit_loss = current_value - total_paid
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x["price_usd"]) - float(coin["price_paid_per"])
                total_current_value += current_value

                name = Label(root, text=x["name"], bg="white")
                name.grid(row=row_index, column=0, sticky=N+S+E+W)

                rank = Label(root, text=x["rank"], bg="grey")
                rank.grid(row=row_index, column=1, sticky=N+S+E+W)

                current_price = Label(root, text=" ${0:.2f}".format(float(x["price_usd"])), bg="white")
                current_price.grid(row=row_index, column=2, sticky=N+S+E+W)

                price_paid = Label(root, text="${0:.2f}".format(coin["price_paid_per"]), bg="grey")
                price_paid.grid(row=row_index, column=3, sticky=N+S+E+W)

                profit_loss_per_coin = Label(root, text="${0:.2f}".format(profit_loss_per_coin), bg="white", fg=red_green(profit_loss_per_coin))
                profit_loss_per_coin.grid(row=row_index, column=4, sticky=N+S+E+W)

                one_hr_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_1h"])), bg="grey", fg=red_green(float(x["percent_change_1h"])))
                one_hr_change.grid(row=row_index, column=5, sticky=N+S+E+W)

                tf_hr_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_24h"])), bg="white", fg=red_green(float(x["percent_change_24h"])))
                tf_hr_change.grid(row=row_index, column=6, sticky=N+S+E+W)

                seven_day_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_7d"])), bg="grey", fg=red_green(float(x["percent_change_7d"])))
                seven_day_change.grid(row=row_index, column=7, sticky=N+S+E+W)

                current_value = Label(root, text="{0:.2f}".format(current_value), bg="white")
                current_value.grid(row=row_index, column=8, sticky=N+S+E+W)

                profit_loss_total = Label(root, text="{0:.2f}%".format(profit_loss), bg="grey", fg=red_green(float(profit_loss)))
                profit_loss_total.grid(row=row_index, column=9, sticky=N+S+E+W)

                row_index += 1

                print("${0:.2f}".format(float(portfolio_profit_loss)))

    portfolio_profits = Label(root, text="P/L ${0:.2f}".format(float(portfolio_profit_loss)), font="Verdana 12 bold", fg=red_green(float(portfolio_profit_loss)))
    portfolio_profits.grid(row=row_index, column=0, sticky=W, padx=10, pady=10)

    root.title("Crypto Currency Portfolio - Portfolio Value: ${0:.2f}".format(float(total_current_value)))
    total_current_value_output = Label(root, text="Portfolio Value ${0:.2f}".format(float(total_current_value)), font="Verdana 12 bold", fg=red_green(float(total_current_value)))
    total_current_value_output.grid(row=row_index+1, column=0, sticky=W, padx=10, pady=10)
    api = ""
    refresh_button = Button(root, text="Refresh Prices", command=lookup)
    refresh_button.grid(row=row_index+2, column=9, sticky=E+S, padx=10, pady=10)
    
lookup()
root.mainloop()