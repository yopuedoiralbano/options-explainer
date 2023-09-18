import streamlit as st
import utils.util_functions as utils
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.write("""### How much should options cost?

What does any of this have to do with the key idea of volatility? 

It mostly comes from how we price these options.

Let's use a very simple underlying asset to start with: a die.

I'm going to roll the die, and the value of the die will be the amount of dots on the face-up side of the die. 

So if the die comes up 6, the asset is worth 6 dollars. 

You can assume the die is fair, so there's an equal chance that each face comes up on top.

How much should the 4 dollar strike be worth (or what is its premium)? Let's say that the multiplier is 1 (just one die) and that the expiration is after the dice is rolled, and its price is determined. 

We'll start by randomly guessing and vibing out some basic ideas. 

Pretend it's worth 1 cent. Seems a bit cheap, right? We could buy it for a cent a bunch of times, and expect to make more than a cent most of the time - so that's probably too cheap. (Why?)

What if it's worth 2 dollars?
That seems a bit high, we could sell it to someone at that price a bunch of times and expect to make money almost every time, since it's never going to pay out more than 2 dollars. (Why?) 

So the answer is somewhere in between these bounds. 

We can try to figure out how much the option is worth by simulating the dice roll a bunch of times, and finding the average value of the option over time.

Let's roll a dice 100,000 times, and plot a histogram of the rolls that we get


""")






dice_strike = st.slider("Select the strike price of the option", 1, 6, 3)

# Generate random dice rolls
rolls = [utils.roll_dice() for _ in range(100000)]

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

st.write("""We'll also plot out the payoff, or profit, of having that option for each roll:

Red means the option ended up being worth 0 after the die roll, and green means it was worth a positive amount, denoted by the value at the bottom of the bar
""")

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
expected_value = np.sum(probabilities * bin_edges_payoffs[:-1])

latex_string_dice = ""

for i in range(len(probabilities)):
    if i == len(probabilities)-1:
        latex_string_dice += f"{probabilities[i]} \\times {bin_edges_payoffs[i]} = {expected_value}"
    else:
        latex_string_dice += f"{probabilities[i]} \\times {bin_edges_payoffs[i]} + "
        
st.write("""
Now we can calculate the average price of the option over the 100,000 rolls, and that should be pretty close to what the option is actually worth!

We multiply each payoff by the probability of getting each of the payoffs, and add them all together, effectively a weighted average

So for each outcome $i$
""")

st.latex('''
\\text{average value} = \\sum_i^n \\text{probability of outcome i} \\times \\text{payoff of outcome i}''')

st.write(""" plugging in the values from the histogram above, we find that the strike selected's average value is: """)

st.latex(latex_string_dice)

st.write("""
This is pretty much how options are priced in the real world, on just about any asset!

1. Come up with a distribution of the possible prices of the asset on the day of the expiry.
2. Estimate or simulate the probability that each price happens
3. Figure out how much the option is worth for each price
4. Find the average value of the option based on the probability distribution of prices

Here, we 
1. Came up with the distribution of possible prices (1-6 are the possible faces of a die)
2. Estimated the probability of each possible price by simulating (roughly 1/6 since it's a fair die)
3. Figured out how much the option is worth for each price (Die Value - Strike Price whenever the Die Value > Strike Price)
4. Found the average value of the option based on the probability distribution of prices (multiplied each outcome by its probability, weighted average)""")
