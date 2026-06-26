import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(page_title="Real Estate Market Analytics", layout="wide")

# Colors from specification
PRIMARY_COLOR = '#1F4E79'
ACCENT_COLOR = '#5B9BD5'
SUCCESS_COLOR = '#70AD47'
WARNING_COLOR = '#FFC000'

@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, '../data/raw/real_estate_dataset.csv')
    return pd.read_csv(data_path)

df = load_data()

# Sidebar
st.sidebar.title("Filters")
selected_property_type = st.sidebar.multiselect("Property Type", options=df['property_type'].unique(), default=df['property_type'].unique())
selected_year = st.sidebar.slider("Year Sold", int(df['year_sold'].min()), int(df['year_sold'].max()), (int(df['year_sold'].min()), int(df['year_sold'].max())))

# Filter data
filtered_df = df[(df['property_type'].isin(selected_property_type)) & (df['year_sold'].between(selected_year[0], selected_year[1]))]

# Tabs for pages
tabs = st.tabs(["Executive Overview", "Property Insights", "Market Trends", "Geographic Analysis"])

# --- Page 1: Executive Overview ---
with tabs[0]:
    st.header("Executive Overview")
    
    # KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Properties Sold", f"{len(filtered_df)}")
    col2.metric("Total Revenue", f"${filtered_df['price'].sum()/1e6:.1f}M")
    col3.metric("Avg Property Price", f"${filtered_df['price'].mean()/1e3:.0f}K")
    col4.metric("Median Price", f"${filtered_df['price'].median()/1e3:.0f}K")
    col5.metric("Avg Days on Market", f"{filtered_df['days_on_market'].mean():.0f}")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    
    # 1. Revenue Trend
    rev_trend = filtered_df.groupby('year_sold')['price'].sum().reset_index()
    fig_rev = px.line(rev_trend, x='year_sold', y='price', title="Revenue Trend", markers=True, color_discrete_sequence=[PRIMARY_COLOR])
    c1.plotly_chart(fig_rev, use_container_width=True)
    
    # 2. Sales by Property Type
    fig_sales = px.bar(filtered_df['property_type'].value_counts().reset_index(), x='property_type', y='count', title="Sales by Property Type", color_discrete_sequence=[ACCENT_COLOR])
    c2.plotly_chart(fig_sales, use_container_width=True)
    
    # 3. Distribution
    fig_dist = px.pie(filtered_df, names='property_type', title="Property Type Distribution", hole=0.4, color_discrete_sequence=[PRIMARY_COLOR, ACCENT_COLOR, SUCCESS_COLOR, WARNING_COLOR])
    st.plotly_chart(fig_dist, use_container_width=True)

# --- Page 2: Property Insights ---
with tabs[1]:
    st.header("Property Insights")
    
    c1, c2 = st.columns(2)
    
    # 1. Avg Price by Property Type
    avg_price_type = filtered_df.groupby('property_type')['price'].mean().reset_index()
    fig_avg = px.bar(avg_price_type, x='property_type', y='price', title="Avg Price by Property Type", color_discrete_sequence=[SUCCESS_COLOR])
    c1.plotly_chart(fig_avg, use_container_width=True)
    
    # 2. Bedrooms vs Price
    fig_bed = px.box(filtered_df, x='bedrooms', y='price', title="Bedrooms vs Price", color_discrete_sequence=[ACCENT_COLOR])
    c2.plotly_chart(fig_bed, use_container_width=True)
    
    c3, c4 = st.columns(2)
    
    # 3. Bathrooms vs Price
    fig_bath = px.box(filtered_df, x='bathrooms', y='price', title="Bathrooms vs Price", color_discrete_sequence=[PRIMARY_COLOR])
    c3.plotly_chart(fig_bath, use_container_width=True)
    
    # 4. Area vs Price
    fig_scatter = px.scatter(filtered_df, x='area_sqft', y='price', color='property_type', title="Area vs Price Scatter Plot", hover_data=['location_score'])
    c4.plotly_chart(fig_scatter, use_container_width=True)

# --- Page 3: Market Trends ---
with tabs[2]:
    st.header("Market Trends")
    
    # 1. Sales Trend
    sales_trend = filtered_df.groupby('year_sold').size().reset_index(name='count')
    fig1 = px.line(sales_trend, x='year_sold', y='count', title="Sales Trend Over Time", markers=True)
    st.plotly_chart(fig1, use_container_width=True)
    
    # 2. Avg Price Trend
    price_trend = filtered_df.groupby('year_sold')['price'].mean().reset_index()
    fig2 = px.line(price_trend, x='year_sold', y='price', title="Average Price Trend", markers=True, color_discrete_sequence=[SUCCESS_COLOR])
    st.plotly_chart(fig2, use_container_width=True)
    
    # 3. Days on Market Trend
    dom_trend = filtered_df.groupby('year_sold')['days_on_market'].mean().reset_index()
    fig3 = px.line(dom_trend, x='year_sold', y='days_on_market', title="Days on Market Trend", markers=True, color_discrete_sequence=[WARNING_COLOR])
    st.plotly_chart(fig3, use_container_width=True)

# --- Page 4: Geographic Analysis ---
with tabs[3]:
    st.header("Geographic Analysis")
    
    c1, c2 = st.columns(2)
    
    # 1. Location Score vs Price
    fig_loc = px.scatter(filtered_df, x='location_score', y='price', trendline="ols", title="Location Score vs Price")
    c1.plotly_chart(fig_loc, use_container_width=True)
    
    # 2. Revenue by Region
    rev_region = filtered_df.groupby('region')['price'].sum().reset_index()
    fig_reg = px.bar(rev_region, x='region', y='price', title="Revenue by Region", color_discrete_sequence=[ACCENT_COLOR])
    c2.plotly_chart(fig_reg, use_container_width=True)
    
    # 3. Avg Price by Region
    avg_reg = filtered_df.groupby('region')['price'].mean().reset_index()
    fig_avg_reg = px.bar(avg_reg, x='region', y='price', title="Average Price by Region", color_discrete_sequence=[SUCCESS_COLOR])
    st.plotly_chart(fig_avg_reg, use_container_width=True)
