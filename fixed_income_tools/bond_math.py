# bond_math.py

# --- PRESENT VALUE FUNCTIONS ---

def present_value(n, fv, r):
    """
    Calculate the present value of a single future cash flow.

    Parameters:
    n (int): Number of periods (e.g., years)
    fv (float): Future value (amount to be received)
    r (float): Interest rate per period (e.g., 0.05 for 5%)

    Returns:
    float: Present value of the future cash flow
    """
    pv = fv / ((1 + r) ** n)
    return pv


# --- Futre VALUE FUNCTIONS ---

def future_value(n, pv, r):
    """
    Calculate the future value of a single future cash flow.

    Parameters:
    n (int): Number of periods (e.g., years)
    pv (float): present value (amount to be received)
    r (float): Interest rate per period (e.g., 0.05 for 5%)

    Returns:
    float: Present value of the future cash flow
    """
    fv = pv * ((1 + r) ** n)
    return fv

# --- CASH FLOW FUNCTION ---
def generate_cash_flows(coupon_rate, face_value, term, frequency):
    """
    Generate the periodic cash flows for a plain-vanilla bond.

    Parameters:
    -----------
    coupon_rate : float
        Annual coupon rate (e.g. 0.03 for 3%).
    face_value : float
        Par value of the bond (e.g. 1000).
    term : int or float
        Total life of the bond in years (e.g. 3).
    frequency : int
        Number of coupon payments per year (e.g. 2 for semiannual).

    Returns:
    --------
    List[float]
        Cash flows in each period, with principal added in the final period.
    """


    n_period = int(term * frequency)
    cf_dict = {}
    coupon_payment = (coupon_rate * face_value)/frequency

    for n in range(n_period):
        # computation is done once, outside of the loop as it's only needed to be computed once & saves CPU
        cf = coupon_payment
        
        #to capture the final cash flow at maturity, interest  + face value
        if n == n_period -1:
            cf += face_value
        cf_dict[n] = round(cf, 2)
    return cf_dict

#--- DISCOUNTED CASH FLOW ---




# --- SPOT RATE FUNCTIONS ---
def calc_spot_rate(...):
    """Compute the spot rate from zero-coupon bond price"""

# --- BOOTSTRAPPIGN SPOT RATES ---

# --- FORWARD RATE FUNCTIONS ---
def forward_rate_1y1y(...):
    """Compute 1-year forward rate 1 year from now..."""

# --- BOND PRICING USING SPOT RATES ---
def bond_price_from_spots(...):
    """Calculate bond price using spot rates and cash flows..."""
