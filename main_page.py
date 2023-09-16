import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# Define the Streamlit app
st.title("Options Explainer")


st.write("""## 1 minute: Key Idea

Options let us express beliefs on how wiggly the price of a stock is (also known as its 'volatility')

### What's an Option?

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

You decide to buy some coupons

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

Notice that when the shoes are worth anything less than 200 dollars, we simply don't use our coupon - since we'd just be losing money. 
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

st.write(""" Just like before, we can plot the theoretical profit we'd have had one year out, depending on how much our handbag ended up being worth.

Notice again that when the handbag is worth anything more than 1500 dollars, we simply don't sell it to our coworker - since we'd just be losing money. 

""")

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

st.write("""

What we've just described here are call and put options. 

Like with the Nike Coupons, Call Options allow you to buy a fixed amount of some asset (for example, stocks), at a specified price until an expiration date.

And like with the Coworker Handbag Deal, Put Options allow you to sell a fixed amount of some asset (for example, stocks), at a specified price until an expiration date.

They're called 'options' because you don't have to do them! If the LeBrons had never increased in price, all we lose is the amount we paid for the option, same situation for the handbag. 

Let's quickly go over some terminology, so that everyone is on the same page. 

- The specified price that we transact at in an option is its **STRIKE PRICE**

- The price that we pay for an option is its **PREMIUM**

- The amount of the asset that we trade in an option is its **MULTIPLIER**

- The expiration date is the ... **EXPIRATION DATE** (no fancy name here)

We can describe an option by using the following structure

{Asset} {Expiration Date or Days to Expiry} {Strike Price} {Call/Put} @ {Premium}

Think about what the options we talked about earlier might be described as

LeBron 30DTE 200c @ 10 dollars

Handbag 365DTE 1500p @ 100 dollars

What does any of this have to do with volatility? 

Well, it mostly comes from how we price these options

I'm going to roll a die, and the value of the die will be the amount of dots on the face-up side of the die. 

You can assume the die is fair, and there's an equal chance that each face comes up on top.

How much should the 4 dollar strike be worth (or what is its premium)? 

Let's say that the multiplier is 1 (just one die) and that the expiration is after the dice is rolled, and its price is determined. 

One way that we typically figure out a 'fair' value for an asset is by calculating the expected value of the asset. 

We know that any time the die rolls below or at 4, we wouldn't make any money. We also wouldn't lose any money, since we just wouldn't use our option to buy the die for 4 dollars. 

We also know that if the die rolls a 5, we could make 1 dollar on our call. Similarly, if the die rolls a 6, we could make 2 dollars on our call. 

So 1/6 of the time, we make 1 dollar, and 1/6 of the time, we make 2 dollars. 

We sum our profit, weighted by the probability it happens, so we do 1/6 * 1 + 1/6 * 2, which amounts to 1/2. 

So the fair price of this dice 4 dollar call should be 0.5 dollars. 

We can visualize this as a histogram of outcomes: 

We'll roll a dice 1000 times, and plot a histogram of the rolls that we get

""")



def roll_dice():
    return np.random.randint(1, 7)


dice_strike = st.slider("Select the strike price of the option", 1, 6, 3)

# Generate random dice rolls
rolls = [roll_dice() for _ in range(1000)]

hist, bin_edges = np.histogram(rolls, bins=6, range=(1, 7))

# Define colors based on bin values
colors = ['green' if bin_value > dice_strike else 'red' for bin_value in bin_edges[0:]]

# Create a bar chart using Plotly
fig_dice = go.Figure()
fig_dice.add_trace(go.Bar(
    x=bin_edges[0:],
    y=hist,
    marker_color=colors,
    text=hist,
    textposition='outside'
))

# Update the layout
fig_dice.update_layout(
    title=f"Dice Roll Histogram (Strike Price: {dice_strike})",
    xaxis_title="Dice Value",
    yaxis_title="Frequency"
)

# Display the histogram
st.plotly_chart(fig_dice)

dice_payoffs = [roll-dice_strike if roll > dice_strike else 0 for roll in rolls]

hist_payoffs, bin_edges_payoffs = np.histogram(dice_payoffs, bins=7-dice_strike, range=(0, 7-dice_strike))

# Define colors based on bin values
colors_dice_payoffs = ['green' if bin_value > 0 else 'red' for bin_value in bin_edges_payoffs[0:]]

# Create a bar chart using Plotly
fig_dice_payoff = go.Figure()
fig_dice_payoff.add_trace(go.Bar(
    x=bin_edges_payoffs[0:],
    y=hist_payoffs,
    marker_color=colors_dice_payoffs,
    text=hist_payoffs,
    textposition='outside'
))

# Update the layout
fig_dice_payoff.update_layout(
    title=f"Dice Call Option Payoff Histogram (Strike Price: {dice_strike})",
    xaxis_title="Option Payoff",
    yaxis_title="Frequency"
)

st.plotly_chart(fig_dice_payoff)

probabilities = hist_payoffs / np.sum(hist_payoffs)
expected_value = np.sum((bin_edges_payoffs[:-1] + bin_edges_payoffs[1:]) / 2 * probabilities)
st.write(expected_value)




st.write("""TODO: visualize the die call option
ideal visualization: histogram colored such that the values above 4 are green and the others aren't
give students a slider to change the strike and see how the fair value changes

This is pretty much how options are priced in the real world, on just about any asset!

We come up with some distribution of potential prices at the time the option expires, and we get the option's price by calculating what we expect the value of the option to be at the expiration date

do the thing where we plot a spaghetti chart of possible stock price series

Explain Theta is just time value - more time increases width of distribution and amount of distribution above strike
Explain Delta, higher starting price means more likely to end profitable
Explain Vega, higher volatility means wider range of distribution and more likely to end profitable



MAYBE: 
put call parity

second order greeks




""")


