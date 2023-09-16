import streamlit as st
import numpy as np
import plotly.express as px

# Define the Streamlit app
st.title("Options Explainer")


st.write("""## 1 minute: Key Idea

Options let us express views on how wiggly a stock is

## Intuition

Options are kind of like coupons. 

Let’s say Nike is selling coupons for a pair of basketball shoes. They’re selling coupons that will let you buy 2 pairs of LeBron shoes for 200 dollars. The coupons expire in 1 month, so you have some time to decide to use the coupon. 

These coupons have:

- a way to transact (you get to buy something for a specified price)
- an underlying asset (you get to buy LeBrons)
- an expiry date (you get to buy LeBrons until 1 month from now)
- a price to transact at (you get to buy LeBrons at 200 dollars until 1 month from now)
- a quantity (you get to buy 2 pairs of LeBrons at 200 dollars until 1 month from now)

How do we know how much these coupons are worth? 

If the Lebrons cost 190 dollars right now, do you really want to use the coupon? Probably not, since you can just buy the shoes from Nike instead. So the coupon likely isn’t worth much. 

But let’s say LeBron wins the finals with the Lakers next week (hypothetically). Suddenly, the LeBrons are flying off the shelves, and Nike jacks up the prices to 300 dollars a pair!

How are we feeling? Pretty good I’d imagine! We can buy LeBrons for 100 dollars off the retail price. 

If we know the coupon is expiring today, we can pretty easily plot out its value as a function of Nike's retail price

We'll assume we got the coupon for 10 dollars, just as an example""")

min_price = 50
max_price = 500

strike_price = 200
premium = 10

underlying_prices = np.linspace(min_price, max_price, 9)

def calculate_long_call_payoff(underlying_price, strike_price, premium):
    payoffs = np.where(underlying_prices <= strike_price, -premium, (underlying_prices - strike_price) - premium)
    return payoffs

# Calculate the option strategy payoffs for each price point
payoffs = calculate_long_call_payoff(underlying_prices, strike_price, premium)

# Create a Plotly figure
fig = px.line(x=underlying_prices, y=payoffs, labels={"x": "Underlying Asset Price", "y": "Payoff"})
fig.update_layout(
    title=f"{strategy_type} Payoff Diagram",
    xaxis_title="Underlying Asset Price",
    yaxis_title="Payoff"
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
