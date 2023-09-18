import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def calculate_long_call_payoff(underlying_prices, strike_price, premium):
    payoffs = np.where(underlying_prices <= strike_price, -premium, (underlying_prices - strike_price) - premium)
    return payoffs

def calculate_long_put_payoff(underlying_prices, strike_price, premium):
    put_payoffs = np.where(underlying_prices <= strike_price, (strike_price - underlying_prices) - premium, -premium)
    return put_payoffs

def roll_dice():
    return np.random.randint(1, 7)

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


def call_option_asset(end_values, strike_value):
    payoffs = end_values - strike_value
    payoffs = np.clip(payoffs, 0, None)
    st.latex("\\text{Simulated Fair Price: }")
    st.latex(payoffs.mean())
    return payoffs.mean()
