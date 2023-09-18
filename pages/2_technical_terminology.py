import streamlit as st

st.write("""

### What does this have to do with options?

What we've just described here **are** options!

Options come in two types, **Calls** and **Puts**.

Like with the Nike Coupons, Call Options allow you to buy a fixed amount of some asset (for example, stocks), at a specified price until an expiration date.

And like with the Coworker Handbag Deal, Put Options allow you to sell a fixed amount of some asset (for example, stocks), at a specified price until an expiration date.

They're called 'options' because you don't have to exercise them! 

If the LeBrons had never increased in price, we wouldn't want or need to use them, so all we'd lose is the amount we paid for the coupon.

Same situation for the handbag, we didn't exercise the option to sell it to our coworker because it wouldn't be profitable for us.

Before we move on, let's quickly go over some terminology, so that everyone is on the same page. 

### Terminology

- The specified price that we transact at in an option is its **STRIKE PRICE**

- The price that we pay for an option is its **PREMIUM**

- The amount of the asset that we trade in an option is its **MULTIPLIER** (stock options are usually 100)

- The expiration date is the ... **EXPIRATION DATE** (no fancy name here)

We can describe an option by using the following structure

{Asset} {Expiration Date or Days to Expiry} {Strike Price} {Call/Put} @ {Premium}

Think about what the options we talked about earlier might be described as

LeBron 30DTE 200c @ 10 dollars

Handbag 365DTE 1500p @ 100 dollars
