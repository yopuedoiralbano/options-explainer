import streamlit as st

st.write("""### Some FAQ I didn't cover:

#### How do I sell an option I don't have? 

Remember how Nike gave us coupons, and our coworker offered us a deal? 

Just like how you can buy these contracts, you can write one up for someone else to buy!

There are times where you might want to be the one writing the contract, usually when you think that someone else is overestimating future 'realized volatility' versus your expectation

#### What if I'm right about volatility, but wrong about the price movement? 

This is a bit out of scope but if you think about it, you would want to offset the risk of the stock moving somehow. 

If you're long a put option, then your option doesn't just make money when realized volatility is higher than implied, you also make money when the stock goes down. But this means you'll also lose money if the stock goes up. 

To offset this risk that comes from the direction of the stock movement, you'll likely want to buy enough shares to offset the price change of your option.

The effect 'Delta' that we explored earlier, the option's sensitivity to price change in the underlying stock, is the effect we want to cancel out. 

If an option has 0.5 delta, then it moves 50 cents for each dollar movement in the underlying stock.

So if your option has 0.5 delta, and moves 50 cents for every dollar movement in the underlying stock, you probably want to buy 50 shares of the stock. (this is because a stock option multiplier is 100 shares, 100 x 0.5 = 50)

This means, in order to purely trade volatility, we can 'delta hedge' our risk due to the underlying stock's movement by buying shares (or selling them)""")
