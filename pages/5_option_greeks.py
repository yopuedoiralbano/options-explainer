import streamlit as st

st.write("""

### Lessons from Histograms

What did you learn? 

Well, you should've noticed the following

1. Option Price Depends on the Current Price

2. Option Price Depends on the Strike Price

3. Option Price Depends on the Time to Expiry

4. Option Price Depends on the Volatility of a Stock

Intuitively, all of these should make sense!

TODO: make these sentences better

A better discount (or lower relative price to buy an asset at) should mean that a coupon is worth more than another coupon, because it's profitability threshold lower down on the range of prices possible, so the probability of it ending up profitable is higher!

A coupon that expires later than another one should be more valuable than one that expires later, since price has more time to move around, causing the probability of it ending up profitable to be higher!

A coupon that is for an asset that has a very jumpy price should be more valuable, because the range of prices it can reach is wider, so the probability of it ending up profitable is higher!

These values are known as **Option Greeks**

### What are Option Greeks? 

Option greeks are just greek letters that represent how an option's price changes as some other variable changes

The basic ones you need to know about are:

Theta, Delta, and Vega:

**Theta** is the time value of an option: since more time to expiry increases the width of the ending price distribution, so the probability of ending above the strike is higher

**Delta** is the option's sensitivity to the stock price movement: as a stock goes up, its probability of ending above the strike is higher

**Vega** is the option's sensitivity to volatility: as a stock gets more volatile, the width of its distribution increases, so the probability of ending above the strike is higher""")
