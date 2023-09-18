import streamlit as st

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

def simulate_gbm_paths(s0, mu, sigma, n=24, T=30, num_paths=1000, plot=True):
    dt = 1/n
    t = np.linspace(0, T, n*T+1)
    S = np.zeros((num_paths, n*T+1))
    
    for i in range(num_paths):
        W = np.random.standard_normal(size=n*T+1)
        W = np.cumsum(W)*np.sqrt(dt)
        X = (mu-0.5*sigma**2)*t + sigma*W
        S[i,:] = s0*np.exp(X)
        
        
    fig_paths = go.Figure()
    for i in range(num_paths):
        fig_paths.add_trace(go.Scatter(x=t, y=S[i,:], mode='lines', name=f'Path {i+1}'))

    fig_paths.update_layout(
        title='Simulated Stock Paths',
        xaxis_title='Time',
        yaxis_title='Price',
        showlegend=True,
        width=800,
        height=500,
    )
    if plot:
        st.plotly_chart(fig_paths)


simulate_gbm_paths(s0=200, mu=0.0005, sigma=0.005, n=24, T=30, num_paths=10, plot=True)

st.write("""Now that we've simulated some paths, let's look at the distribution of outcomes these paths might create! 

Let's generate a lot more paths: 100 should be a good number to start with
""")



def simulate_gbm_paths_plotly_histogram_with_bins(s0, mu, sigma, n=24, T=30, num_paths=1000, num_bins=20):
    dt = 1/n
    t = np.linspace(0, T, n*T+1)
    S = np.zeros((num_paths, n*T+1))
    
    for i in range(num_paths):
        W = np.random.standard_normal(size=n*T+1)
        W = np.cumsum(W)*np.sqrt(dt)
        X = (mu-0.5*sigma**2)*t + sigma*W
        S[i,:] = s0*np.exp(X)
    
    # Calculate end values
    end_values = S[:, -1]
    
    # Calculate histogram data
    hist_values, bin_edges = np.histogram(end_values, bins=num_bins)
    
    # Create subplots with one row and two columns
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Stock Paths', 'End Value Histogram'), column_widths=[0.7, 0.3])
    
    # Add GBM paths to the first subplot
    for i in range(num_paths):
        fig.add_trace(go.Scatter(x=t, y=S[i,:], mode='lines', name=f'Path {i+1}'), row=1, col=1)

    
    # Add a bar chart with bins and counts to the second subplot
    fig.add_trace(go.Bar(y=bin_edges[:-1], x=hist_values, orientation='h', name='End Values'), row=1, col=2)
    
    # Update layout
    fig.update_layout(
        title='Simulated Stock Paths and Expiration Price Distribution',
        xaxis_title='Counts',
        yaxis_title='Price',
        xaxis2=dict(domain=[0.75, 1.0]),
        yaxis2=dict(anchor='x2'),
        showlegend=False,  # Set to False to avoid legend duplication
        width=1000,
        height=500,
    )
    
    st.plotly_chart(fig)

simulate_gbm_paths_plotly_histogram_with_bins(s0=200, mu=0.0005, sigma=0.005, n=24, T=30, num_paths=100)

# Example usage:
# simulate_gbm_paths_plotly_with_histogram(s0=100, mu=0.05, sigma=0.2, n=24, T=30, num_paths=5)


st.write("""

Awesome! We've got a nice distribution that shows the different outcomes of our stock series.

3. Figure out how much the option is worth for each price

Let's do it again, and clearly mark the 'profitable' and 'unprofitable' zones: or where the price goes above the strike price.

For now, we'll set the strike price to be 210.""")

def simulate_gbm_paths_plotly_histogram_with_bins_and_color(s0, mu, sigma, n=24, T=30, num_paths=1000, num_bins=20, strike_threshold=200):
    dt = 1/n
    t = np.linspace(0, T, n*T+1)
    S = np.zeros((num_paths, n*T+1))
    
    for i in range(num_paths):
        W = np.random.standard_normal(size=n*T+1)
        W = np.cumsum(W)*np.sqrt(dt)
        X = (mu-0.5*sigma**2)*t + sigma*W
        S[i,:] = s0*np.exp(X)
    
    # Calculate end values
    end_values = S[:, -1]
    
    # Calculate histogram data
    hist_values, bin_edges = np.histogram(end_values, bins=num_bins)
    
    # Create subplots with one row and two columns
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Stock Paths', 'End Value Histogram'), column_widths=[0.7, 0.3])
    
    # Add GBM paths to the first subplot
    for i in range(num_paths):
        fig.add_trace(go.Scatter(x=t, y=S[i,:], mode='lines', name=f'Path {i+1}'), row=1, col=1)

    colors_strike = ['red' if x < strike_threshold else 'green' for x in bin_edges[:-1]]
    
    # Add a bar chart with bins and counts to the second subplot
    fig.add_trace(go.Bar(y=bin_edges[:-1], x=hist_values, orientation='h', marker_color=colors_strike, name='End Values'), row=1, col=2)
    
    # Update layout
    fig.update_layout(
        title='Simulated Stock Paths and Colored Expiration Price Distribution',
        xaxis_title='Counts',
        yaxis_title='Price',
        xaxis2=dict(domain=[0.75, 1.0]),
        yaxis2=dict(anchor='x2'),
        showlegend=False,  # Set to False to avoid legend duplication
        width=1000,
        height=500,
    )
    
    st.plotly_chart(fig)

    return end_values, strike_threshold


end_prices, strike_value = simulate_gbm_paths_plotly_histogram_with_bins_and_color(s0=200, mu=0.0005, sigma=0.005, n=24, T=30, num_paths=100, strike_threshold=210)

st.write("""

4. Find the average value of the option based on the probability distribution of prices

Let's not look at the calculation exactly here, since it would be a bit long, but the price would be: """)

def call_option_asset(end_values, strike_value):
    payoffs = end_values - strike_value
    payoffs = np.clip(payoffs, 0, None)
    st.latex("\\text{Simulated Fair Price: }")
    st.latex(payoffs.mean())
    return payoffs.mean()

call_option_asset(end_prices, strike_value)
