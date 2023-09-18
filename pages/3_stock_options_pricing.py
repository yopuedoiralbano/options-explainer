import streamlit as st
import utils.util_functions as utils
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.write("""### What does this have to do with stocks?

It's the exact same process!

1. Come up with a distribution of the possible prices of the asset on the day of the expiry.
2. Estimate or simulate the probability that each price happens

Here's how we're going to simulate a stock's potential future paths:

- start with the current price of the stock
- for each time step:
  - we choose an amount for the stock to move (the stock's return at the current timestep)
  - we choose the amount for the stock to move from a symmetrical bell curve of possible amounts (sampling fro a normal distribution)
  - the width of the bell curve is the stock's 'volatility' (this is the standard deviation of the return distribution)
  - a higher volatility means a wider bell curve, so the movements will usually be further from the average (higher volatility -> the stock path will jump around more)
  - a lower volatility means a tighter bell curve, so the movements will usually be closer to the average (lower volatility -> the stock path will be more smooth)
  - simulate the stock moving that amount
  - set the new current price to be the price after the stock moved
  


There's some technical detail being glossed over in the above explanation, but feel free to look up geometric brownian motion if you want to learn more about the specifics!
""")

utils.simulate_gbm_paths(s0=200, mu=0.0, sigma=0.005, n=24, T=30, num_paths=10, plot=True)

st.write("""Now that we've simulated some paths, let's look at the distribution of outcomes these paths might create! 

Let's generate a lot more paths: 100 should be a good number to start with
""")

utils.simulate_gbm_paths_plotly_histogram_with_bins(s0=200, mu=0.0, sigma=0.005, n=24, T=30, num_paths=100)

# Example usage:
# simulate_gbm_paths_plotly_with_histogram(s0=100, mu=0.05, sigma=0.2, n=24, T=30, num_paths=5)


st.write("""

Awesome! We've got a nice distribution that shows the different outcomes of our stock series.

3. Figure out how much the option is worth for each price

Let's do it again, and clearly mark the 'profitable' and 'unprofitable' zones: or where the price goes above the strike price.

For now, we'll set the strike price to be 210.""")



end_prices, strike_value = utils.simulate_gbm_paths_plotly_histogram_with_bins_and_color(s0=200, mu=0.0, sigma=0.005, n=24, T=30, num_paths=100, strike_threshold=210)

st.write("""

4. Find the average value of the option based on the probability distribution of prices

Let's not look at the calculation exactly here, since it would be a bit long, but the price would be: """)

utils.call_option_asset(end_prices, strike_value)
