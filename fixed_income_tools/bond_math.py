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

    for n in range(1, n_period +1):
        # computation is done once, outside of the loop as it's only needed to be computed once & saves CPU
        cf = coupon_payment
        
        #to capture the final cash flow at maturity, interest  + face value
        if n == n_period:
            cf += face_value
        cf_dict[n] = round(cf, 2)
    return cf_dict

#--- DISCOUNTED CASH FLOW ---

def bond_dcf(cf_dict, discount_rate, frequency):
    """
    Calculate the present value of a bond using DCF.

    Parameters:
    -----------
    cash_flows : list of floats
        Cash flows per period (e.g. from generate_cash_flows).
    discount_rate : float
        Periodic discount rate (e.g. 0.02 for 2% per period).
    frequency : int
        Number of periods per year (e.g. 2 for semiannual)

    Returns:  
        float
        Present value of the bond.
    """
    #captures if discount rate is entered as a whole number. 
    if discount_rate > 1:
        discount_rate /= 100

    r = discount_rate / frequency
    return round(sum(cf/(1 + r)**t for t, cf in cf_dict.items()), 2)



# --- SPOT RATE FUNCTIONS ---
def calc_spot_rate(clean_price, term, face_value):
    """
    Compute the spot rate for a zero-coupon bond.
    
    Parameters:
    -----------
    clean_price : float
        Price of the zero-coupon bond
    term : int or float
        Time to maturity (in years)
    face_value : float
        Par value of the bond (default = 1000)

    Returns:
    --------
    float
        Spot rate as a decimal (e.g., 0.05 for 5%)
    """
    discount_factor = face_value / clean_price
    spot_rate = discount_factor ** (1 / term) - 1
    return round(spot_rate, 6)


# --- BOOTSTRAPPING SPOT RATES FROM PAR RATES ---
def bootstrap_spot_rates(par_rates, frequency=2, face_value=100):
    """
    Bootstraps spot rates from par rates.
    
    Parameters:
    - par_rates: list of par rates (as decimals, e.g., 0.026)
    - frequency: compounding frequency (1 = annual, 2 = semiannual, etc.)
    - face_value: default 100, can be adjusted if needed
    
    Returns:
        - dict: {term_in_years: spot_rate}
    """
    spot_rates = {}
    for i, rate in enumerate(par_rates):
        periods = (i + 1) * frequency
        coupon = (rate * face_value) / frequency
        price = face_value

        # Present value of known coupons using previously bootstrapped spot rates
        pv_coupons = sum([
            coupon / (1 + spot_rates[t])**(t + 1)
            for t in range(periods - 1)
        ])

        numerator = coupon + face_value
        denominator = price - pv_coupons

        spot_periodic  = (numerator / denominator)**(1 / periods) - 1
        spot_annual = frequency * spot_periodic

        term = (i + 1)
        spot_curve[term] = round(spot_annual, 6)

    return spot_rates


# --- BOOTSTRAPPING SPOT RATES FROM CLEAN PRICES ---
def bootstrap_from_bond_prices(bond_list, frequency = 2):
    """
    Bootstrap zero rates from bond prices.
    
    Parameters:
    bond_list: List of dictionaries containing bond information
    
    Returns:
    Dictionary mapping terms to zero rates
    """
    periodic_zeros = {}
    
    # Sort bonds by term
    sorted_bonds = sorted(bond_list, key=lambda x: x['term'])
    
    for bond in sorted_bonds:
        term = bond['term']
        price = bond['price']
        cash_flows = bond['cash_flows']
        periods = int(term * frequency)
        
        # Calculate present value of known cash flows
        # Only sum over periods for which we already have zero rates
        pv_known = 0
        for t in range(1, periods):
            if t in periodic_zeros:  # Only use periods we've already calculated
                pv_known += cash_flows[t] / ((1 + periodic_zeros[t])**t)
        
        # 4) final cash flow at full maturity
        final_cf = cash_flows[periods]
        total_pv = price - pv_known
        
        # 5) solve for periodic zero rate
        r_periodic = (final_cf / total_pv)**(1/periods) - 1
        
        periodic_zeros[periods] = r_periodic
    
    # 6) annualize and map back to years
    zero_rates = {
        periods / frequency: round(r * frequency, 6)
        for periods, r in periodic_zeros.items()
    }
    return zero_rates


    



# --- FORWARD RATE FUNCTIONS ---
def forward_rate_1y1y(...):
    """Compute 1-year forward rate 1 year from now..."""

# --- BOND PRICING USING SPOT RATES ---
def bond_price_from_spots(...):
    """Calculate bond price using spot rates and cash flows..."""
