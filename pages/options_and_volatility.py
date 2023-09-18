import streamlit as st

st.write("""### Option Prices as a function of Volatility

Notice how, at any given time, we will always know:
- the option's strike price
- the option's days to expiry
- the stock's current price

But what we don't know is:
- the stock's volatility

If we know an option's volatility, we can work out what the price of the option should be. 

Vice versa, if we know the price of an option, we can work out the 'implied volatility' of an option. 

### Why and how do we trade volatility?

Unlike in the model shown above, volatility is not constant over time. 

One obvious example of stock volatility changing is news announcements. Apple's share price is likely to be more volatile when a new iPhone releases, than when nothing big and interesting is happening with the company. 

While the market has an implied volatility that we can infer from the option's price, what actually happens might be different. 

We call the volatility that actually happens 'realized volatility'. 

- If we think a stock's 'realized volatility' will be higher than the market's 'implied volatility' derived from the option price, we should buy the option
  - This is because if the volatility that ends up occurring is higher than what the market predicted, the option is more valuable on average, so we make money!
  - Circling back to our coupon example, this means that we should buy coupons from Nike only if we think they're understimating how much their shoes might fluctuate in value. 
  - We should only agree to the deal with our coworker if we think she's underestimating how much the handbag might fluctuate in value. 

- Likewise, if we think a stock's 'realized volatility' will be lower than market's 'implied volatility' derived from the option price, we should sell the option
  - Now, if the volatility that ends up occurring is lower than what the market predicted, the option will be less valuable on average, so we make money!
  - Nike probably sold the coupons because they thought that we'd overestimate the volatility of the shoe price
  - Our coworker probably made the deal with us because she thought we'd overestimate the volatility of the handbag

This is why options are so intertwined with our beliefs about the volatility of a stock: their price is a direct expression of what the market expects a stock's volatility to be. """)
