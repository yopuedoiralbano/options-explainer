import streamlit as st

st.write(""" 

### Price your own options! 

There's a bunch of parameters here that can change the distribution and the final price a lot, here's your chance to get a feel for it!

Start by playing around with one at a time, and then observe the relationships between them:

Some questions to answer: 

How does the option value usually change as a function of the current price?

How does the option value usually change as a function of the strike price?

How does the option value usually change as a function of the time to expiry?

How does the option value usually change as a function of the stock's volatility?

""")

st.write("""Current Price (what price is the stock at right now?)""")

s0_input = st.slider(
    'Select the price the stock is currently at!',
    100, 1000, 200)


st.write("""Strike Value (what price do we get the option to buy the stock at?)""")

strike_val_input = st.slider(
    'Select the strike price of the option!',
    int(s0_input*0.8), int(s0_input*1.2), s0_input)

st.write("""Time to Expiry (how many days until the option expires?)""")

time_to_expiry_input = st.slider(
    'Select the amount of days until the option expires!',
    1, 90, 30)

# st.write("""Stock Drift (does it tend to go up or down?)""")
# mu_input = st.slider(
#     'Select how much the stock trends up or down!',
#     -25, 25, 5)

st.write("""Stock Volatility (how wiggly are the price movements?)""")

sigma_input = st.slider(
    'Select how volatile the stock is!',
    0, 25, 5)

end_prices_interactive, strike_val_input = simulate_gbm_paths_plotly_histogram_with_bins_and_color(s0=s0_input, 
                                                                                                   mu=0.0005, sigma=sigma_input/1e3, 
                                                                                                   n=24, T=time_to_expiry_input, 
                                                                                                   num_paths=200, 
                                                                                                   strike_threshold=strike_val_input)

call_option_asset(end_prices_interactive, strike_val_input)
