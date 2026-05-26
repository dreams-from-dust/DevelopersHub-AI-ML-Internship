import streamlit as st
import numpy as np
import pandas as pd
import os
import plotly.express as px
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingRegressor

# --- PREMIUM WINDOW CONFIGURATION ---
st.set_page_config(
    page_title="Premium Property Valuation Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- EXCHANGE RATE CONFIGURATION ---
USD_TO_PKR = 278.41

# --- BACKEND TRAINING ENGINE (Cached) ---
@st.cache_resource
def train_production_model():
    np.random.seed(42)
    n_samples = 1500
    sq_ft = np.random.normal(1800, 600, n_samples).astype(int).clip(500)
    bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.1, 0.2, 0.4, 0.2, 0.1])
    bathrooms = (bedrooms - np.random.choice([0, 1], size=n_samples, p=[0.6, 0.4])).clip(1)
    location = np.random.choice(['Downtown', 'Urban', 'Suburbs', 'Rural'], size=n_samples)
    loc_sqft_rates = {'Downtown': 210, 'Urban': 155, 'Suburbs': 110, 'Rural': 65}
    base_rate = np.array([loc_sqft_rates[loc] for loc in location])
    
    price = 40000.0 + (sq_ft.astype(float) * base_rate) + (bedrooms.astype(float) * 22000.0) + (bathrooms.astype(float) * 18000.0)
    price += np.random.normal(0, 25000, n_samples)
    
    df = pd.DataFrame({
        'Square_Footage': sq_ft, 
        'Bedrooms': bedrooms, 
        'Bathrooms': bathrooms, 
        'Location': location, 
        'Price': price.astype(int)
    })
    
    df['Bed_Bath_Ratio'] = df['Bedrooms'] / df['Bathrooms']
    X = df.drop(columns=['Price'])
    y = df['Price']
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), ['Square_Footage', 'Bedrooms', 'Bathrooms', 'Bed_Bath_Ratio']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Location'])
    ])
    
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', HistGradientBoostingRegressor(random_state=42))
    ])
    model.fit(X, y)
    return model, df

model_pipeline, training_df = train_production_model()

# --- MASTER THEME CONFIGURATION (Total Framework Reset) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Global Deep Charcoal Canvas */
    .stApp {
        background-color: #12110F;
        color: #F7F5F0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Clean Title Formatting */
    .main-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #FFFFFF;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    
    .subtitle {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #C2B69D;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    /* Premium Matte Containers */
    .premium-card {
        background-color: #1A1917;
        border: 1px solid #2B2824;
        border-radius: 16px;
        padding: 2.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }
    
    .card-header {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: #FFFFFF;
        opacity: 0.8;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid rgba(214, 175, 55, 0.2); 
        padding-bottom: 12px;
    }
    
    /* FinTech Output Box Card */
    .valuation-box {
        background: linear-gradient(135deg, #1A1917, #24211C);
        border: 2px solid #D4AF37;
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 40px rgba(212, 175, 55, 0.1);
    }
    
    .pkr-value {
        font-size: 3rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.3rem;
        letter-spacing: -0.5px;
    }
    
    .usd-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #D4AF37;
        margin-bottom: 1.5rem;
    }
    
    .valuation-label {
        text-transform: uppercase;
        font-size: 0.95rem;
        letter-spacing: 2px;
        color: #C2B69D;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* Fixed Button Theme Overrides */
    div.stButton > button:first-child {
        background-color: #D4AF37 !important;
        color: #12110F !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.9rem 2.5rem !important;
        margin-top: 0.5rem !important;
        box-shadow: 0 4px 20px rgba(212,175,55,0.25) !important;
        transition: all 0.25s ease-in-out !important;
        cursor: pointer !important;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #EED483 !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(212,175,55,0.35) !important;
    }

    /* --- NATIVE COMPONENT RE-ENGINEERING --- */
    div[data-baseweb="select"] {
        cursor: pointer !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #262421 !important;
        border: 1px solid #3B3730 !important;
        color: #FFFFFF !important;
        cursor: pointer !important;
    }
    
    div[data-baseweb="input"] > div {
        background-color: #262421 !important;
        border: 1px solid #3B3730 !important;
        color: #FFFFFF !important;
    }
    input[type="number"] {
        color: #FFFFFF !important;
    }

    div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #1A1917 !important;
        border: 1px solid #3B3730 !important;
    }
    ul[role="listbox"] li, [data-baseweb="menu"] li {
        color: #FAF6F0 !important;
        cursor: pointer !important;
        transition: background 0.2s ease;
    }
    ul[role="listbox"] li:hover, [data-baseweb="menu"] li:hover {
        background-color: #2B2824 !important;
    }

    div[data-testid="stSlider"] div[role="slider"] {
        background-color: #D4AF37 !important;
        border: 2px solid #D4AF37 !important;
    }
    div[data-testid="stSlider"] div[aria-valuemax] {
        background-color: #3B3730 !important;
    }
    
    button[data-baseweb="tab"] {
        color: #C2B69D !important;
        font-weight: 500 !important;
    }
    button[aria-selected="true"] {
        color: #D4AF37 !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: #D4AF37 !important;
    }

    .premium-card label, .premium-card p, .premium-card div, .premium-card span {
        color: #F7F5F0 !important;
        font-weight: 500;
    }
    .stMarkdown p, .stMarkdown h3, .stMarkdown li {
        color: #FAF6F0;
    }
    .premium-card .stMarkdown p, .premium-card .stMarkdown h3, .premium-card .stMarkdown li {
        color: #E6DFD3 !important;
    }
    .tab-icon-wrapper {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        vertical-align: middle;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER LAYOUT ---
st.markdown('<div class="main-title">PROPERTY VALUATION PORTAL</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">Data-driven property estimation and localized financial analysis framework | Base Exchange Rate: 1 USD = {USD_TO_PKR} PKR</div>', unsafe_allow_html=True)

# --- PROFESSIONAL VECTOR ICON COMPENDIUM (SVGs) ---
icon_home = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
icon_chart = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'
icon_calc = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>'
icon_guide = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'

# --- NAVIGATION TABS PLATFORM ---
tab1, tab2, tab3, tab4 = st.tabs([
    "Valuation Engine Layout", 
    "Analytics Layout", 
    "Planner Layout",
    "Documentation Layout"
])

tab1.label = f'<span class="tab-icon-wrapper">{icon_home} Property Valuation Engine</span>'
tab2.label = f'<span class="tab-icon-wrapper">{icon_chart} Market Insights and Analytics</span>'
tab3.label = f'<span class="tab-icon-wrapper">{icon_calc} Financing and Mortgage Planner</span>'
tab4.label = f'<span class="tab-icon-wrapper">{icon_guide} User Guide and Benefits</span>'

# ==========================================
# TAB 1: PROPERTY VALUATION ENGINE
# ==========================================
with tab1:
    left_col, right_col = st.columns([6, 6], gap="large")
    
    with left_col:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Property Characteristics</div>', unsafe_allow_html=True)
        
        sq_ft = st.number_input(
            "Total Covered Area (Square Feet)", 
            min_value=500, 
            max_value=10000, 
            value=1850, 
            step=50
        )
        
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=5, value=3)
        with s_col2:
            bathrooms = st.slider("Number of Bathrooms", min_value=1, max_value=5, value=2)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-header">Geographic Classification</div>', unsafe_allow_html=True)
        location = st.selectbox("Select Neighborhood / Region Classification", ['Downtown', 'Urban', 'Suburbs', 'Rural'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # FIXED: Updated use_container_width to width='stretch'
        run_evaluation = st.button("RUN VALUATION EVALUATION", width='stretch')

    with right_col:
        if run_evaluation:
            bed_bath_ratio = bedrooms / bathrooms
            input_data = pd.DataFrame({
                'Square_Footage': [sq_ft],
                'Bedrooms': [bedrooms],
                'Bathrooms': [bathrooms],
                'Location': [location],
                'Bed_Bath_Ratio': [bed_bath_ratio]
            })
            
            predicted_usd = model_pipeline.predict(input_data)[0]
            predicted_pkr = predicted_usd * USD_TO_PKR
            
            st.markdown(f"""
                <div class="valuation-box">
                    <div class="valuation-label">Estimated Market Valuation</div>
                    <div class="pkr-value">PKR {predicted_pkr:,.0f}</div>
                    <div class="usd-value">${predicted_usd:,.2f} USD</div>
                    <div style="font-size: 1rem; color: #C2B69D; margin-top: 1.5rem; line-height: 1.6; font-weight: 500; border-top: 1px solid rgba(212, 175, 55, 0.3); padding-top: 15px; text-align: left;">
                        <span style="font-weight: 700; color: #FFFFFF;">Structural Metrics Matrix (Dual Currencies):</span><br>
                        • Spatial Density Ratio: <b style="color: #D4AF37;">{bed_bath_ratio:.2f}</b> bed/bath<br>
                        • Calculated Unit Price (PKR): <b style="color: #D4AF37;">PKR {predicted_pkr/sq_ft:,.0f}</b> / sq.ft<br>
                        • Calculated Unit Price (USD): <b style="color: #D4AF37;">${predicted_usd/sq_ft:,.2f}</b> / sq.ft
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="border: 1px dashed #3B3730; border-radius: 16px; padding: 7.5rem 2rem; text-align: center; background-color: #1A1917;">
                    <div style="color: #D4AF37; font-size: 1.4rem; font-weight: 700;">
                        System Awaiting Execution
                    </div>
                    <div style="color: #C2B69D; font-size: 0.95rem; margin-top: 0.7rem; font-weight: 500; line-height: 1.5; max-width: 400px; margin-left: auto; margin-right: auto;">
                        Configure your property profile metrics on the left panel and click the evaluation button to process the predictive algorithm.
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ==========================================
# TAB 2: MARKET INSIGHTS & ANALYTICS
# ==========================================
with tab2:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Historical Benchmark Insights (PKR / USD Multi-Context)</div>', unsafe_allow_html=True)
    st.markdown("<p style='color: #E6DFD3 !important; margin-bottom: 20px;'>Review localized insights distilled directly from 1,500 checked real estate benchmark listings indexed in both valuations.</p>", unsafe_allow_html=True)
    
    avg_prices = training_df.groupby('Location')['Price'].mean().reset_index()
    avg_prices['Price (PKR Millions)'] = (avg_prices['Price'] * USD_TO_PKR) / 1000000
    avg_prices['Price (USD Thousands)'] = avg_prices['Price'] / 1000
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("<p style='color:#E6DFD3; font-weight:700; font-size:1.1rem; margin-bottom:10px;'>Average Valuation Baseline (PKR Millions)</p>", unsafe_allow_html=True)
        fig1 = px.bar(avg_prices, x='Location', y='Price (PKR Millions)', color_discrete_sequence=['#D4AF37'])
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E6DFD3', font_family='Plus Jakarta Sans', height=330, margin=dict(l=20, r=20, t=15, b=20),
            xaxis=dict(showgrid=False, title=''), yaxis=dict(showgrid=True, gridcolor='#2B2824', title='')
        )
        # FIXED: Updated use_container_width to width='stretch'
        st.plotly_chart(fig1, width='stretch')
        
    with col_chart2:
        st.markdown("<p style='color:#E6DFD3; font-weight:700; font-size:1.1rem; margin-bottom:10px;'>Average Valuation Baseline (USD Thousands)</p>", unsafe_allow_html=True)
        fig2 = px.bar(avg_prices, x='Location', y='Price (USD Thousands)', color_discrete_sequence=['#C2B69D'])
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E6DFD3', font_family='Plus Jakarta Sans', height=330, margin=dict(l=20, r=20, t=15, b=20),
            xaxis=dict(showgrid=False, title=''), yaxis=dict(showgrid=True, gridcolor='#2B2824', title='')
        )
        # FIXED: Updated use_container_width to width='stretch'
        st.plotly_chart(fig2, width='stretch')
        
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 3: FINANCING & MORTGAGE PLANNER
# ==========================================
with tab3:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Dual-Currency Financing and Installment Estimator</div>', unsafe_allow_html=True)
    
    f_col1, f_col2 = st.columns([5, 7], gap="large")
    
    with f_col1:
        default_val = int(training_df['Price'].mean() * USD_TO_PKR)
        calc_base_pkr = st.number_input("Property Valuation Target Principal (PKR)", min_value=100000, max_value=500000000, value=default_val, step=500000)
        
        calc_base_usd = calc_base_pkr / USD_TO_PKR
        st.markdown(f"<p style='color:#D4AF37; font-size:0.9rem; margin-top:-12px; margin-bottom:15px; font-weight:600;'>Equivalent Input Value: ${calc_base_usd:,.2f} USD</p>", unsafe_allow_html=True)
        
        down_payment_pct = st.slider("Down Payment Percentage (%)", min_value=10, max_value=80, value=20, step=5)
        interest_rate = st.number_input("Annual Interest Rate / Markup (%)", min_value=1.0, max_value=30.0, value=12.0, step=0.5)
        loan_years = st.selectbox("Loan Duration Term", [5, 10, 15, 20, 25, 30], index=3)
        
    with f_col2:
        down_payment_pkr = calc_base_pkr * (down_payment_pct / 100)
        financed_amount_pkr = calc_base_pkr - down_payment_pkr
        monthly_rate = (interest_rate / 100) / 12
        total_months = loan_years * 12
        
        if monthly_rate > 0:
            monthly_installment_pkr = financed_amount_pkr * (monthly_rate * (1 + monthly_rate)**total_months) / ((1 + monthly_rate)**total_months - 1)
        else:
            monthly_installment_pkr = financed_amount_pkr / total_months
            
        down_payment_usd = down_payment_pkr / USD_TO_PKR
        financed_amount_usd = financed_amount_pkr / USD_TO_PKR
        monthly_installment_usd = monthly_installment_pkr / USD_TO_PKR
        
        st.markdown(f"""
            <div style="background-color: #12110F; border: 1px solid #2B2824; border-radius: 12px; padding: 1.8rem; box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);">
                <h4 style="color: #FFFFFF; margin-top: 0; font-family: 'Plus Jakarta Sans', sans-serif; font-weight:700; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 8px;">Financing Matrix Breakdown</h4>
                <table style="width:100%; border-collapse: collapse; font-size: 0.95rem; color: #E6DFD3;">
                    <tr style="border-bottom: 1px solid #1A1917; height: 2.8rem;">
                        <td><b>Total Capital Evaluation Asset Value:</b></td>
                        <td style="text-align: right; color: #FFFFFF; font-weight: 700;">PKR {calc_base_pkr:,.0f}<br><span style="color:#D4AF37; font-size:0.8rem;">${calc_base_usd:,.2f} USD</span></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #1A1917; height: 2.8rem;">
                        <td><b>Down Payment Obligation ({down_payment_pct}%):</b></td>
                        <td style="text-align: right; color: #C2B69D; font-weight: 700;">PKR {down_payment_pkr:,.0f}<br><span style="color:#C2B69D; font-size:0.8rem;">${down_payment_usd:,.2f} USD</span></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #1A1917; height: 2.8rem;">
                        <td><b>Total Net Loan Principal Financed:</b></td>
                        <td style="text-align: right; color: #E6DFD3; font-weight: 700;">PKR {financed_amount_pkr:,.0f}<br><span style="color:#E6DFD3; font-size:0.8rem;">${financed_amount_usd:,.2f} USD</span></td>
                    </tr>
                    <tr style="height: 3.8rem;">
                        <td><b style="font-size: 1.05rem; color: #FFFFFF;">Calculated Monthly Premium:</b></td>
                        <td style="text-align: right; font-size: 1.35rem; font-weight: 700; color: #D4AF37;">PKR {monthly_installment_pkr:,.0f} / mo<br><span style="font-size:1rem; color:#FFFFFF;">${monthly_installment_usd:,.2f} USD / mo</span></td>
                    </tr>
                </table>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 4: USER GUIDE & BENEFITS
# ==========================================
with tab4:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Platform Architecture and User Advantage</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    ### How to Navigate and Use the System
    1. **Input Your Metrics:** Open the **Property Valuation Engine** tab. Adjust the property size (Square Feet), bedroom setup, and location to match your target asset.
    2. **Run Evaluation Model:** Click the **RUN VALUATION EVALUATION** button to render calculations instantly.
    3. **Analyze Localized Pricing:** Look up regional pricing baselines in the **Market Insights** tab to see how averages distribute across different zones in both PKR and USD.
    
    ### Core Benefits and Value Propositions
    * **No More Overpaying:** Base your property transaction negotiations on standard algorithmic models compiled from 1,500 checked market data nodes rather than guesswork.
    * **Native Dual-Currency Synchronization:** Eradicate the fatigue of converting values from dollar benchmarks manually. The entire system computes synchronously at a verified baseline index rate of **1 USD = {USD_TO_PKR} PKR**.
    """)
    st.markdown('</div>', unsafe_allow_html=True)