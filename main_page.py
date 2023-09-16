import streamlit as st
import numpy as np
import plotly.express as px

# Define the Streamlit app
st.title("Options Explainer")


st.write("""## 1 minute: Key Idea

Options let us express views on how wiggly a stock is

## Intuition

Options are kind of like coupons. 

Let’s say Nike is selling coupons for a pair of basketball shoes, at 10 dollars per coupon. 
They’re selling coupons that will let you buy 2 pairs of LeBron shoes for 200 dollars. 
The coupons expire in 1 month, so you have some time to decide to use the coupon. 

These coupons have:
- **a price** (you have to pay money for the coupon)
- **a way to transact** (you get to buy something for a specified price)
- **an underlying asset** (you get to buy LeBrons)
- **an expiry date** (you get to buy LeBrons until 1 month from now)
- **a price to transact at** (you get to buy LeBrons at 200 dollars until 1 month from now)
- **a quantity** (you get to buy 2 pairs of LeBrons at 200 dollars until 1 month from now)

How do we know how much these coupons are worth? 

If the Lebrons cost 190 dollars right now, do you really want to use the coupon? Probably not, since you can just buy the shoes from Nike instead. So the coupon likely isn’t worth much. 

But let’s say LeBron wins the finals with the Lakers next week (hypothetically). Suddenly, the LeBrons are flying off the shelves, and Nike jacks up the prices to 300 dollars a pair!

How are we feeling? Pretty good I’d imagine! We can buy LeBrons for 100 dollars off the retail price.

Since we expect there's a lot of people willing to buy the shoe, we might even buy the 2 pairs of shoes for 200 dollars, and sell them to someone else for 300 dollars each. 
This means we'd make 190 dollars! 
Can you see why? 

""")

st.latex('''(300-200) \\times 2 - 10 = 100 \\times 2 - 10 = 200 - 10 = 190''')

st.write("""
Generalizing this formula:
""")

st.latex('''(\\text{Nike Price} - \\text{Coupon Price}) \\times (n \\text{ shoes per coupon}) - (\\text{coupon price})''')


st.write("""
So if we know the coupon is expiring today, we can pretty easily plot out the profit we might get from buying and using it as a function of Nike's retail price.
""")


min_price = 50
max_price = 400

strike_price = 200
premium = 10

underlying_prices_plot = np.linspace(min_price, max_price, 8)

def calculate_long_call_payoff(underlying_price, strike_price, premium):
    payoffs = np.where(underlying_prices <= strike_price, -premium, (underlying_prices - strike_price) - premium)
    return payoffs

payoffs_plot = calculate_long_call_payoff(underlying_prices_plot, strike_price, premium)

fig = px.line(x=underlying_prices_plot, y=payoffs_plot, labels={"x": "LeBron Shoe Value", "y": "Profit"})
fig.update_layout(
    title=f"Coupon Profit Diagram",
    xaxis_title="LeBron Shoe Value",
    yaxis_title="Profit"
)

st.plotly_chart(fig)


st.write("""
This is pretty cool! Looks like we have a ton of upside, and not very much downside. 

Play around with the parameters a bit if you'd like: 
""")

min_max_price_input = st.slider(
    'Select the price range to plot!',
    0, 1000, (50, 400))

step_size_input = st.slider(
    'Select the step size to plot with!',
    0, 100, 50)

strike_price_input = st.slider(
    'Select the coupon price to buy shoes at!',
    0, 1000, 200)

premium_input = st.slider(
    'Select the price we paid for the coupon!',
    0, 1000, 10)



underlying_prices_shoes = np.linspace(min_max_price_input[0], min_max_price_input[1], (min_max_price_input[1]-min_max_price_input[0])//step_size_input)

payoffs_shoes = calculate_long_call_payoff(underlying_prices_shoes, strike_price_input, premium_input)

st.write(underlying_prices_plot)
st.write(payoffs_plot)
st.write(underlying_prices_shoes)
st.write(payoffs_shoes)

fig2 = px.line(x=underlying_prices_shoes, y=payoffs_shoes, labels={"x": "LeBron Shoe Value", "y": "Profit"})
fig2.update_layout(
    title=f"Coupon Profit Diagram",
    xaxis_title="LeBron Shoe Value",
    yaxis_title="Profit"
)

st.plotly_chart(fig2)



