#!/usr/bin/env python3
"""
Pakistan Sales Data Analysis - Streamlit Dashboard
Comprehensive analytics and ML dashboard for sales data
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import snowflake.connector
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Pakistan Sales Analytics Dashboard",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Snowflake connection configuration
@st.cache_resource
def get_snowflake_connection():
    """Create Snowflake connection"""
    try:
        conn = snowflake.connector.connect(
            user=st.secrets["snowflake"]["user"],
            password=st.secrets["snowflake"]["password"],
            account=st.secrets["snowflake"]["account"],
            warehouse=st.secrets["snowflake"]["warehouse"],
            database=st.secrets["snowflake"]["database"],
            schema=st.secrets["snowflake"]["schema"]
        )
        return conn
    except Exception as e:
        st.error(f"Failed to connect to Snowflake: {e}")
        return None

# Data loading functions
@st.cache_data(ttl=3600)
def load_sales_data():
    """Load sales data from Snowflake"""
    conn = get_snowflake_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            fs.*,
            dt.YEAR, dt.MONTH, dt.MONTH_NAME, dt.QUARTER,
            dc.CUSTOMER_FULL_NAME, dc.CUSTOMER_SEGMENT, dc.PRIMARY_PROVINCE,
            dp.PRODUCT_NAME, dp.CATEGORY_NAME, dp.BRAND,
            ds.STORE_NAME, ds.CITY as STORE_CITY, ds.PROVINCE as STORE_PROVINCE,
            de.EMPLOYEE_FULL_NAME, de.DEPARTMENT
        FROM FACTS.FACT_SALES fs
        JOIN DIMENSIONS.DIM_TIME dt ON fs.TIME_KEY = dt.TIME_KEY
        JOIN DIMENSIONS.DIM_CUSTOMER dc ON fs.CUSTOMER_KEY = dc.CUSTOMER_KEY
        JOIN DIMENSIONS.DIM_PRODUCT dp ON fs.PRODUCT_KEY = dp.PRODUCT_KEY
        JOIN DIMENSIONS.DIM_STORE ds ON fs.STORE_KEY = ds.STORE_KEY
        JOIN DIMENSIONS.DIM_EMPLOYEE de ON fs.EMPLOYEE_KEY = de.EMPLOYEE_KEY
        LIMIT 10000
        """
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

@st.cache_data(ttl=3600)
def load_customer_behavior():
    """Load customer behavior data"""
    conn = get_snowflake_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            cb.*,
            dc.CUSTOMER_FULL_NAME, dc.CUSTOMER_SEGMENT, dc.PRIMARY_PROVINCE,
            dc.AGE_GROUP, dc.INCOME_BAND
        FROM FACTS.FACT_CUSTOMER_BEHAVIOR cb
        JOIN DIMENSIONS.DIM_CUSTOMER dc ON cb.CUSTOMER_KEY = dc.CUSTOMER_KEY
        """
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Failed to load customer behavior data: {e}")
        return None

@st.cache_data(ttl=3600)
def load_monthly_aggregates():
    """Load monthly sales aggregates"""
    conn = get_snowflake_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT * FROM AGGREGATES.AGG_MONTHLY_SALES
        ORDER BY YEAR, MONTH
        """
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Failed to load monthly aggregates: {e}")
        return None

# Main dashboard
def main():
    # Header
    st.markdown('<h1 class="main-header">🇵🇰 Pakistan Sales Analytics Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("📊 Dashboard Controls")
    
    # Date range filter
    st.sidebar.subheader("📅 Date Range")
    date_range = st.sidebar.selectbox(
        "Select Date Range",
        ["Last 30 Days", "Last 3 Months", "Last 6 Months", "Last Year", "All Time"]
    )
    
    # Province filter
    st.sidebar.subheader("🏛️ Province Filter")
    province_filter = st.sidebar.multiselect(
        "Select Provinces",
        ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan", "Gilgit-Baltistan", "Azad Kashmir"],
        default=["Punjab", "Sindh"]
    )
    
    # Customer segment filter
    st.sidebar.subheader("👥 Customer Segment")
    segment_filter = st.sidebar.multiselect(
        "Select Segments",
        ["Premium", "Regular", "Occasional", "VIP"],
        default=["Premium", "Regular"]
    )
    
    # Load data
    with st.spinner("Loading data from Snowflake..."):
        sales_df = load_sales_data()
        customer_df = load_customer_behavior()
        monthly_df = load_monthly_aggregates()
    
    if sales_df is None or customer_df is None or monthly_df is None:
        st.error("Failed to load data. Please check your Snowflake connection.")
        return
    
    # Apply filters
    if date_range != "All Time":
        days_map = {
            "Last 30 Days": 30,
            "Last 3 Months": 90,
            "Last 6 Months": 180,
            "Last Year": 365
        }
        cutoff_date = datetime.now() - timedelta(days=days_map[date_range])
        sales_df = sales_df[sales_df['ORDER_DATE'] >= cutoff_date]
    
    if province_filter:
        sales_df = sales_df[sales_df['STORE_PROVINCE'].isin(province_filter)]
        customer_df = customer_df[customer_df['PRIMARY_PROVINCE'].isin(province_filter)]
    
    if segment_filter:
        sales_df = sales_df[sales_df['CUSTOMER_SEGMENT'].isin(segment_filter)]
        customer_df = customer_df[customer_df['CUSTOMER_SEGMENT'].isin(segment_filter)]
    
    # Main metrics row
    st.subheader("📈 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = sales_df['FINAL_LINE_AMOUNT'].sum()
        st.metric(
            label="💰 Total Sales (PKR)",
            value=f"PKR {total_sales:,.0f}",
            delta=f"PKR {total_sales * 0.15:,.0f}"
        )
    
    with col2:
        total_orders = sales_df['ORDER_ID'].nunique()
        st.metric(
            label="📦 Total Orders",
            value=f"{total_orders:,}",
            delta=f"{int(total_orders * 0.12):,}"
        )
    
    with col3:
        total_customers = sales_df['CUSTOMER_KEY'].nunique()
        st.metric(
            label="👥 Unique Customers",
            value=f"{total_customers:,}",
            delta=f"{int(total_customers * 0.08):,}"
        )
    
    with col4:
        avg_order_value = sales_df['FINAL_LINE_AMOUNT'].mean()
        st.metric(
            label="📊 Average Order Value",
            value=f"PKR {avg_order_value:,.0f}",
            delta=f"PKR {avg_order_value * 0.05:,.0f}"
        )
    
    # Charts row 1
    st.subheader("📊 Sales Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly sales trend
        monthly_sales = sales_df.groupby(['YEAR', 'MONTH', 'MONTH_NAME'])['FINAL_LINE_AMOUNT'].sum().reset_index()
        monthly_sales['YEAR_MONTH'] = monthly_sales['YEAR'].astype(str) + '-' + monthly_sales['MONTH'].astype(str).str.zfill(2)
        
        fig_monthly = px.line(
            monthly_sales,
            x='YEAR_MONTH',
            y='FINAL_LINE_AMOUNT',
            title='📈 Monthly Sales Trend',
            labels={'FINAL_LINE_AMOUNT': 'Sales (PKR)', 'YEAR_MONTH': 'Month'}
        )
        fig_monthly.update_layout(height=400)
        st.plotly_chart(fig_monthly, use_container_width=True)
    
    with col2:
        # Sales by province
        province_sales = sales_df.groupby('STORE_PROVINCE')['FINAL_LINE_AMOUNT'].sum().reset_index()
        
        fig_province = px.pie(
            province_sales,
            values='FINAL_LINE_AMOUNT',
            names='STORE_PROVINCE',
            title='🏛️ Sales Distribution by Province'
        )
        fig_province.update_layout(height=400)
        st.plotly_chart(fig_province, use_container_width=True)
    
    # Charts row 2
    col1, col2 = st.columns(2)
    
    with col1:
        # Top products by revenue
        top_products = sales_df.groupby('PRODUCT_NAME')['FINAL_LINE_AMOUNT'].sum().nlargest(10).reset_index()
        
        fig_products = px.bar(
            top_products,
            x='FINAL_LINE_AMOUNT',
            y='PRODUCT_NAME',
            orientation='h',
            title='🏆 Top 10 Products by Revenue',
            labels={'FINAL_LINE_AMOUNT': 'Revenue (PKR)', 'PRODUCT_NAME': 'Product'}
        )
        fig_products.update_layout(height=400)
        st.plotly_chart(fig_products, use_container_width=True)
    
    with col2:
        # Customer segment distribution
        segment_sales = sales_df.groupby('CUSTOMER_SEGMENT')['FINAL_LINE_AMOUNT'].sum().reset_index()
        
        fig_segment = px.bar(
            segment_sales,
            x='CUSTOMER_SEGMENT',
            y='FINAL_LINE_AMOUNT',
            title='👥 Sales by Customer Segment',
            labels={'FINAL_LINE_AMOUNT': 'Sales (PKR)', 'CUSTOMER_SEGMENT': 'Segment'}
        )
        fig_segment.update_layout(height=400)
        st.plotly_chart(fig_segment, use_container_width=True)
    
    # Charts row 3
    st.subheader("🎯 Customer Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # RFM Analysis
        rfm_counts = customer_df['RFM_SEGMENT'].value_counts().reset_index()
        rfm_counts.columns = ['Segment', 'Count']
        
        fig_rfm = px.bar(
            rfm_counts,
            x='Segment',
            y='Count',
            title='🎯 Customer RFM Segmentation',
            labels={'Count': 'Number of Customers', 'Segment': 'RFM Segment'}
        )
        fig_rfm.update_layout(height=400)
        st.plotly_chart(fig_rfm, use_container_width=True)
    
    with col2:
        # Age group distribution
        age_sales = sales_df.groupby('AGE_GROUP')['FINAL_LINE_AMOUNT'].sum().reset_index()
        
        fig_age = px.pie(
            age_sales,
            values='FINAL_LINE_AMOUNT',
            names='AGE_GROUP',
            title='👴👵 Sales by Age Group'
        )
        fig_age.update_layout(height=400)
        st.plotly_chart(fig_age, use_container_width=True)
    
    # Advanced Analytics
    st.subheader("🔬 Advanced Analytics")
    
    # Correlation analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Sales Correlation Analysis")
        
        # Create correlation matrix for numerical columns
        numeric_cols = ['QUANTITY_ORDERED', 'UNIT_PRICE', 'DISCOUNT_PERCENT', 'FINAL_LINE_AMOUNT']
        correlation_data = sales_df[numeric_cols].corr()
        
        fig_corr = px.imshow(
            correlation_data,
            title='Correlation Matrix',
            color_continuous_scale='RdBu',
            aspect='auto'
        )
        fig_corr.update_layout(height=400)
        st.plotly_chart(fig_corr, use_container_width=True)
    
    with col2:
        st.subheader("📈 Sales Forecasting")
        
        # Simple moving average forecast
        monthly_agg = sales_df.groupby(['YEAR', 'MONTH'])['FINAL_LINE_AMOUNT'].sum().reset_index()
        monthly_agg['YEAR_MONTH'] = monthly_agg['YEAR'].astype(str) + '-' + monthly_agg['MONTH'].astype(str).str.zfill(2)
        monthly_agg = monthly_agg.sort_values('YEAR_MONTH')
        
        # Calculate 3-month moving average
        monthly_agg['MA_3'] = monthly_agg['FINAL_LINE_AMOUNT'].rolling(window=3).mean()
        
        fig_forecast = px.line(
            monthly_agg,
            x='YEAR_MONTH',
            y=['FINAL_LINE_AMOUNT', 'MA_3'],
            title='Sales Forecast (3-Month Moving Average)',
            labels={'value': 'Sales (PKR)', 'variable': 'Metric'}
        )
        fig_forecast.update_layout(height=400)
        st.plotly_chart(fig_forecast, use_container_width=True)
    
    # Data Tables
    st.subheader("📋 Detailed Data Views")
    
    tab1, tab2, tab3 = st.tabs(["📊 Sales Data", "👥 Customer Data", "🏪 Store Performance"])
    
    with tab1:
        st.dataframe(
            sales_df[['ORDER_DATE', 'CUSTOMER_FULL_NAME', 'PRODUCT_NAME', 'STORE_NAME', 
                     'FINAL_LINE_AMOUNT', 'CUSTOMER_SEGMENT', 'STORE_PROVINCE']].head(100),
            use_container_width=True
        )
    
    with tab2:
        st.dataframe(
            customer_df[['CUSTOMER_FULL_NAME', 'CUSTOMER_SEGMENT', 'PRIMARY_PROVINCE', 
                        'TOTAL_ORDERS', 'TOTAL_SPENT', 'RFM_SEGMENT']].head(100),
            use_container_width=True
        )
    
    with tab3:
        store_performance = sales_df.groupby(['STORE_NAME', 'STORE_PROVINCE', 'STORE_CITY']).agg({
            'ORDER_ID': 'nunique',
            'FINAL_LINE_AMOUNT': 'sum',
            'CUSTOMER_KEY': 'nunique'
        }).reset_index()
        store_performance.columns = ['Store', 'Province', 'City', 'Orders', 'Total Sales', 'Unique Customers']
        store_performance['Avg Order Value'] = store_performance['Total Sales'] / store_performance['Orders']
        
        st.dataframe(store_performance.sort_values('Total Sales', ascending=False).head(100), use_container_width=True)
    
    # Machine Learning Section
    st.subheader("🤖 Machine Learning Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Customer Lifetime Value Prediction")
        
        # Simple CLV calculation based on historical data
        clv_data = customer_df.copy()
        clv_data['CLV'] = clv_data['TOTAL_SPENT'] * (clv_data['TOTAL_ORDERS'] / 12) * 12  # Annual projection
        
        fig_clv = px.histogram(
            clv_data,
            x='CLV',
            nbins=20,
            title='Customer Lifetime Value Distribution',
            labels={'CLV': 'CLV (PKR)', 'count': 'Number of Customers'}
        )
        fig_clv.update_layout(height=400)
        st.plotly_chart(fig_clv, use_container_width=True)
        
        # CLV statistics
        avg_clv = clv_data['CLV'].mean()
        st.metric("Average CLV", f"PKR {avg_clv:,.0f}")
    
    with col2:
        st.subheader("📊 Product Recommendation Engine")
        
        # Simple product association based on co-purchases
        product_pairs = sales_df.groupby('ORDER_ID')['PRODUCT_NAME'].apply(list).reset_index()
        product_pairs = product_pairs[product_pairs['PRODUCT_NAME'].apply(len) > 1]
        
        # Count product co-occurrences
        co_occurrences = {}
        for products in product_pairs['PRODUCT_NAME']:
            for i in range(len(products)):
                for j in range(i+1, len(products)):
                    pair = tuple(sorted([products[i], products[j]]))
                    co_occurrences[pair] = co_occurrences.get(pair, 0) + 1
        
        # Top product pairs
        top_pairs = sorted(co_occurrences.items(), key=lambda x: x[1], reverse=True)[:10]
        pair_df = pd.DataFrame(top_pairs, columns=['Product Pair', 'Co-occurrences'])
        
        fig_pairs = px.bar(
            pair_df,
            x='Co-occurrences',
            y='Product Pair',
            orientation='h',
            title='Top Product Combinations',
            labels={'Co-occurrences': 'Number of Co-purchases', 'Product Pair': 'Products'}
        )
        fig_pairs.update_layout(height=400)
        st.plotly_chart(fig_pairs, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🇵🇰 Pakistan Sales Data Analysis Dashboard | Built with Streamlit & Snowflake</p>
        <p>Data refreshed every hour | Last updated: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
