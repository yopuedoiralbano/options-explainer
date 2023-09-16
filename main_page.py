import streamlit as st
import numpy as np
import plotly.express as px

# Define the Streamlit app
st.title("Options Explainer")


st.write("""## 1 minute: Key Idea

Options let us express views on how wiggly a stock is

## Intuition

Options are kind of like coupons. 

Let’s say Nike is selling coupons for a pair of basketball shoes, at **10 dollars per coupon**. 

Each coupon will let you buy **2 pairs of LeBron shoes** for **200 dollars each**. 

The coupons **expire in 1 month**, so you have some time to decide to use the coupon. 

These coupons have:
- **a price** (you have to pay money for the coupon)
- **a way to transact** (you get to buy something for a specified price)
- **an underlying asset** (you get to buy LeBrons)
- **an expiry date** (you get to buy LeBrons until 1 month from now)
- **a price to transact at** (you get to buy LeBrons at 200 dollars until 1 month from now)
- **a quantity** (you get to buy 2 pairs of LeBrons at 200 dollars each until 1 month from now)

How do we know how much these coupons are worth? 

If the Lebrons cost 190 dollars each right now, do you really want to use the coupon? Probably not, since you can just buy the shoes from Nike instead. So the coupon likely isn’t worth much. 

But let’s say LeBron wins the finals with the Lakers next week (hypothetically). Suddenly, the LeBrons are flying off the shelves, and Nike jacks up the prices to 300 dollars a pair!

How are we feeling? Pretty good I’d imagine! We can buy each pair of LeBrons for 100 dollars off the retail price.

Since we expect there's a lot of people willing to buy the shoe, we might even buy the 2 pairs of shoes for 200 dollars, and sell them to someone else for 300 dollars each. 
This means we'd make 190 dollars! 

Can you see why? 

""")

st.latex('''(300-200) \\times 2 - 10 = 100 \\times 2 - 10 = 200 - 10 = 190''')

st.write("""
Generalizing this formula:
""")

st.latex('''(\\text{Nike Price} - \\text{Discounted Price}) \\times (n \\text{ pairs of shoes per coupon}) - (\\text{coupon price})''')


st.write("""
So if we know the coupon is expiring today, we can pretty easily plot out the profit we might get from the using the coupon, as a function of Nike's retail price.
""")


min_price_initial = 50
max_price_initial = 400

strike_price_initial = 200
premium_initial = 10

underlying_prices_plot = np.linspace(min_price_initial, max_price_initial, 8)

def calculate_long_call_payoff(underlying_prices, strike_price, premium):
    payoffs = np.where(underlying_prices <= strike_price, -premium, (underlying_prices - strike_price) - premium)
    return payoffs

payoffs_plot = calculate_long_call_payoff(underlying_prices_plot, strike_price_initial, premium_initial)

fig = px.line(x=underlying_prices_plot, y=payoffs_plot, labels={"x": "LeBron Shoe Value", "y": "Profit"})
fig.update_layout(
    title=f"Coupon Profit Diagram",
    xaxis_title="LeBron Shoe Value",
    yaxis_title="Profit"
)

st.plotly_chart(fig)


st.write("""
This is pretty cool! Looks like we have a ton of upside (potentially infinite), and not very much downside (what we paid for the coupon, 10 dollars). 

Play around with the parameters a bit, try to answer the following questions/do the following:

TODO: make these exploration questions better lol

- what happens when the coupon price is above the maximum of the price range?
- what happens when the coupon price is below the minimum of the price range?
- what's the relation between the price paid for the coupon, coupon price, and the min/max price range?
""")

strike_price_input = st.slider(
    'Select the discounted price to buy shoes at!',
    0, 1000, 200)

premium_input = st.slider(
    'Select the price we paid for the coupon!',
    0, 1000, 10)

underlying_prices_shoes = np.linspace(0, 1000, (1000))

payoffs_shoes = calculate_long_call_payoff(underlying_prices_shoes, strike_price_input, premium_input)

fig2 = px.line(x=underlying_prices_shoes, y=payoffs_shoes, labels={"x": "LeBron Shoe Value", "y": "Profit"})
fig2.update_layout(
    title=f"Coupon Profit Diagram",
    xaxis_title="LeBron Shoe Value",
    yaxis_title="Profit"
)

st.plotly_chart(fig2)

st.write("""
Now that we've done some exploration, let's talk about another variant of an option. 

Imagine instead of being able to buy an object for a specified price before some specified expiration date, we can sell an object instead. 

For example, imagine you have a designer handbag that a coworker of yours has always wanted. 

She's saving up for her own bag, but she's willing to buy your bag off of you anytime within the next year, for 1500 dollars. 
She'll guarantee to do this trade with you, if you pay her 100 dollars up front. 

The handbag is worth 2000 dollars right now, so you have no reason to sell it to her for 1500 dollars. 
But like before with the LeBron shoes - something might happen that could cause your handbag's value to drop dramatically. 

Let's say you agree to her deal. 

A few months later, handbags are falling out of fashion. In a shocking twist, backpacks have become all the rage, and the one-sided handbags are seen as trashy. 
Your handbag is only worth 200 dollars now! (it is still very high quality)

You call your coworker and give her the handbag. She's a bit upset, but upholds her end of the bargain. 

How much money did you just make, in theory? 
You sold something that was worth 200 dollars for 1500 dollars, and you only paid 100 dollars to be able to do that, so you've made 1200 dollars!
""")

st.latex('''(1500-200) \\times 1 - 100 = 1300 \\times 1 - 100 = 1300 - 100 = 1200''')

st.write("""
Generalizing this formula:
""")

st.latex('''(\\text{Coworker Price} - \\text{Handbag Price}) \\times (n \\text{ handbags per deal}) - (\\text{deal price})''')

st.write(""" Just like before, we can plot the theoretical profit we'd have had one year out, depending on how much our handbag ended up being worth.""")

min_price_bag = 100
max_price_bag = 2000

strike_price_bag = 1500
premium_bag = 200

underlying_prices_bag = np.linspace(min_price_bag, max_price_bag, max_price_bag-min_price_bag)

def calculate_long_put_payoff(underlying_prices, strike_price, premium):
    put_payoffs = np.where(underlying_prices <= strike_price, (strike_price - underlying_prices) - premium, -premium)
    return put_payoffs

payoffs_bag = calculate_long_put_payoff(underlying_prices_bag, strike_price_bag, premium_bag)

fig_bag = px.line(x=underlying_prices_bag, y=payoffs_bag, labels={"x": "Designer Handbag Value", "y": "Profit"})
fig_bag.update_layout(
    title=f"Coworker Deal Profit Diagram",
    xaxis_title="Designer Handbag Value",
    yaxis_title="Profit"
)

st.plotly_chart(fig_bag)


