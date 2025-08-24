# Pakistan Sales Data Analysis Project

## 🚀 Project Overview

This comprehensive Snowflake project demonstrates a complete **OLTP → OLAP → Data Science** pipeline for Pakistan Sales Data Analysis. The project showcases end-to-end data analytics capabilities, from transactional data management to advanced analytics and machine learning insights.

## 📊 Project Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   OLTP DB      │    │   OLAP DWH      │
│                 │    │                 │    │                 │
│ • CSV Files     │───▶│ • 3NF Normalized│───▶│ • Star Schema   │
│ • Generated     │    │ • Transactional │    │ • Analytical    │
│ • Pakistan Data │    │ • Operational   │    │ • BI Ready      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   ETL Process   │    │   Streamlit     │
                       │   (Python/SQL)  │    │   Dashboard     │
                       │                 │    │   (Analytics+ML)│
                       └─────────────────┘    └─────────────────┘
```

## 🏗️ Project Structure

### Core Components
- **OLTP Database**: `PAKISTAN_SALES_OLTP_DB` - Fully normalized transactional database (3NF)
- **OLAP Data Warehouse**: `PAKISTAN_SALES_OLAP_DB` - Star schema analytical database
- **ETL Pipeline**: Complete data transformation from OLTP to OLAP
- **Streamlit Dashboard**: Interactive analytics and machine learning insights
- **Data Generation**: Python script for realistic Pakistani market data

### Database & Schemas

#### OLTP Database (`PAKISTAN_SALES_OLTP_DB`)
- **STAGING**: Raw data ingestion and validation
- **OLTP**: Operational transactional data (3NF normalized)
- **AUDIT**: Audit and logging information

#### OLAP Database (`PAKISTAN_SALES_OLAP_DB`)
- **DIMENSIONS**: Dimension tables for star schema
- **FACTS**: Fact tables for analytical queries
- **AGGREGATES**: Pre-aggregated data for performance
- **ANALYTICS**: Analytical views and derived metrics

### Warehouses
- `PAKISTAN_OLTP_WH`: OLTP operations (X-SMALL)
- `PAKISTAN_LOADING_WH`: Data loading operations (SMALL)
- `PAKISTAN_OLAP_WH`: OLAP analytical operations (SMALL)
- `PAKISTAN_ETL_WH`: ETL and data processing (MEDIUM)

## 📁 File Descriptions

### Core SQL Files

#### OLTP Setup (`oltp/01_oltp_database_setup.sql`)
- Creates OLTP database with 3NF normalized structure
- Sets up staging infrastructure (stages, file formats)
- Creates operational tables for day-to-day transactions
- Establishes warehouses and security policies

#### OLTP Data Loading (`oltp/02_data_loading_oltp.sql`)
- Implements data loading procedures for CSV files
- Sets up error handling and data validation
- Creates audit logging and monitoring
- Establishes data quality checks

#### OLAP Setup (`olap/03_olap_data_warehouse_setup.sql`)
- Creates OLAP data warehouse with star schema design
- Implements dimension and fact tables
- Sets up pre-aggregated tables for performance
- Establishes analytical views and metrics

#### ETL Process (`olap/04_etl_oltp_to_olap.sql`)
- Implements complete ETL pipeline from OLTP to OLAP
- Creates data transformation and enrichment procedures
- Sets up automated data loading and refresh
- Establishes data quality monitoring

### Python Applications

#### Data Generator (`generate_pakistan_sales_data.py`)
- Generates realistic Pakistani market sales data
- Creates 10,000+ sales records with authentic details
- Includes 2,000 customers, 800 products, 75 stores
- Covers all Pakistani provinces and major cities

#### Streamlit Dashboard (`streamlit_dashboard.py`)
- Interactive web-based analytics dashboard
- Real-time data visualization from Snowflake
- Machine learning insights (CLV prediction, recommendations)
- Advanced filtering and segmentation capabilities

### Configuration Files

#### `snowflake.toml`
- Connection configurations for Snowflake
- Warehouse and database settings
- Authentication parameters

#### `config.txt` & `account.txt`
- Environment-specific configurations
- Connection parameters and account details

#### `requirements.txt` & `streamlit_requirements.txt`
- Python dependencies for data generation and dashboard

## 🔧 Setup and Deployment

### Prerequisites
- Snowflake account with ACCOUNTADMIN privileges
- Python 3.8+ environment
- Snowflake connector for Python
- Streamlit for dashboard deployment

### Quick Start

1. **Generate Sample Data**
   ```bash
   python generate_pakistan_sales_data.py
   ```

2. **Set Up Snowflake Infrastructure**
   ```sql
   -- Execute in sequence:
   -- 1. oltp/01_oltp_database_setup.sql
   -- 2. oltp/02_data_loading_oltp.sql
   -- 3. olap/03_olap_data_warehouse_setup.sql
   -- 4. olap/04_etl_oltp_to_olap.sql
   ```

3. **Deploy Streamlit Dashboard**
   ```bash
   pip install -r streamlit_requirements.txt
   streamlit run streamlit_dashboard.py
   ```

### Step-by-Step Deployment

#### Phase 1: Data Generation
```bash
# Generate realistic Pakistani sales data
python generate_pakistan_sales_data.py
```

#### Phase 2: OLTP Database Setup
```sql
-- Execute oltp/01_oltp_database_setup.sql
-- Creates database, schemas, tables, and warehouses
```

#### Phase 3: Data Loading
```sql
-- Execute oltp/02_data_loading_oltp.sql
-- Loads CSV data into OLTP database
```

#### Phase 4: OLAP Data Warehouse
```sql
-- Execute olap/03_olap_data_warehouse_setup.sql
-- Creates analytical database with star schema
```

#### Phase 5: ETL Implementation
```sql
-- Execute olap/04_etl_oltp_to_olap.sql
-- Implements data transformation pipeline
```

#### Phase 6: Dashboard Deployment
```bash
# Deploy interactive analytics dashboard
streamlit run streamlit_dashboard.py
```

## 📊 Key Features

### Data Management
- **Realistic Data Generation**: Authentic Pakistani market data
- **3NF Normalization**: Proper database design for OLTP
- **Star Schema**: Optimized structure for analytics
- **Automated ETL**: Streamlined data transformation pipeline

### Analytics Capabilities
- **Interactive Dashboard**: Real-time analytics with Streamlit
- **Advanced SQL Analytics**: Window functions and aggregations
- **Customer Segmentation**: RFM analysis and classification
- **Product Analytics**: Performance tracking and lifecycle analysis
- **Geographic Analysis**: Provincial and city-level insights

### Machine Learning
- **Customer Lifetime Value**: Predictive analytics
- **Product Recommendations**: ML-based suggestions
- **Customer Segmentation**: Automated classification
- **Trend Analysis**: Time-series forecasting

### Performance & Optimization
- **Materialized Views**: Pre-computed aggregations
- **Strategic Clustering**: Optimized data distribution
- **Dedicated Warehouses**: Workload-specific resources
- **Query Optimization**: Performance monitoring and tuning

## 👥 User Roles and Permissions

### Sales Analyst Role
- Access to analytical data and reports
- Limited access to sensitive customer details
- Can run analytics and generate insights
- Territory-restricted data access

### Sales Manager Role
- Full access to sales and customer data
- Can modify and update customer information
- Access to all territories and regions
- Performance monitoring capabilities

### Data Engineer Role
- Full access to all schemas and tables
- Can create and modify data structures
- Warehouse management capabilities
- ETL and data transformation access

### Data Scientist Role
- Access to production data for analysis
- Can create new tables and views
- Machine learning model deployment
- Analytics and modeling capabilities

## 📈 Analytics and Reporting

### Pre-Built Views
- **Sales Performance Dashboard**: Comprehensive sales metrics
- **Customer Analytics**: Behavior and segmentation insights
- **Product Performance**: Lifecycle and performance metrics
- **Geographic Performance**: Regional and territorial analysis

### Key Metrics
- **Sales Performance**: Revenue, growth, trends
- **Customer Metrics**: RFM scores, segmentation, behavior
- **Product Analytics**: Performance, lifecycle, profitability
- **Geographic Insights**: Regional performance, market penetration

### Advanced Analytics
- **Time Series Analysis**: Seasonal patterns and trends
- **Customer Segmentation**: RFM analysis and classification
- **Product Lifecycle**: Performance tracking and optimization
- **Predictive Insights**: CLV prediction and forecasting

## 🔒 Security Features

### Data Protection
- **Column-Level Security**: Sensitive data masking
- **Row-Level Security**: Territory-based access control
- **Data Encryption**: End-to-end encryption
- **Access Logging**: Comprehensive audit trails

### Compliance
- **Data Retention**: Automated archival policies
- **Data Classification**: Automated tagging and categorization
- **Audit Logging**: Complete activity tracking
- **Policy Enforcement**: Automated compliance monitoring

## 🚀 Performance Optimization

### Query Performance
- **Table Clustering**: Optimized data distribution
- **Materialized Views**: Pre-computed aggregations
- **Query Optimization**: Performance monitoring and tuning
- **Warehouse Scaling**: Automatic resource management

### Data Management
- **Automated Maintenance**: Regular optimization tasks
- **Data Archival**: Automated retention management
- **Performance Monitoring**: Real-time performance tracking
- **Resource Optimization**: Efficient warehouse utilization

## 📋 Monitoring and Maintenance

### Automated Tasks
- **Data Quality Monitoring**: Continuous quality checks
- **Performance Optimization**: Regular table maintenance
- **Data Retention**: Automated archival procedures
- **Security Monitoring**: Continuous security oversight

### Monitoring Views
- **Performance Metrics**: Query and warehouse performance
- **Data Quality**: Quality scores and metrics
- **Security Events**: Access and security monitoring
- **System Health**: Overall system performance

## 🔄 Data Pipeline

### Ingestion
1. **Data Generation**: Python script creates realistic CSV files
2. **File Upload**: CSV files uploaded to Snowflake staging
3. **Data Validation**: Quality checks and validation
4. **OLTP Loading**: Data loaded into normalized tables

### Processing
1. **ETL Pipeline**: Automated transformation from OLTP to OLAP
2. **Data Enrichment**: Business logic and calculations
3. **Aggregation**: Summary tables and materialized views
4. **Quality Assurance**: Continuous quality monitoring

### Delivery
1. **Analytics Views**: Pre-built dashboards and reports
2. **Materialized Views**: Performance-optimized aggregations
3. **Real-time Updates**: Change data capture and streaming
4. **Interactive Dashboard**: Streamlit-based analytics interface

## 📊 Sample Queries

### Basic Sales Analysis
```sql
-- Total sales by year and month
SELECT YEAR, MONTH_NAME, SUM(SALES_AMOUNT) as TOTAL_SALES
FROM FACTS.FACT_SALES fs
JOIN DIMENSIONS.DIM_TIME dt ON fs.TIME_KEY = dt.TIME_KEY
GROUP BY YEAR, MONTH_NAME
ORDER BY YEAR DESC, MONTH;
```

### Customer Segmentation
```sql
-- Customer RFM analysis
SELECT * FROM ANALYTICS.CUSTOMER_RFM_ANALYSIS
WHERE CUSTOMER_SEGMENT = 'Champions'
ORDER BY RFM_TOTAL_SCORE DESC;
```

### Product Performance
```sql
-- Top performing products by province
SELECT 
    dp.PRODUCT_NAME,
    ds.PROVINCE,
    SUM(fs.SALES_AMOUNT) as TOTAL_REVENUE
FROM FACTS.FACT_SALES fs
JOIN DIMENSIONS.DIM_PRODUCT dp ON fs.PRODUCT_KEY = dp.PRODUCT_KEY
JOIN DIMENSIONS.DIM_STORE ds ON fs.STORE_KEY = ds.STORE_KEY
GROUP BY dp.PRODUCT_NAME, ds.PROVINCE
ORDER BY TOTAL_REVENUE DESC;
```

### Geographic Analysis
```sql
-- Provincial performance analysis
SELECT 
    ds.PROVINCE,
    COUNT(DISTINCT fs.CUSTOMER_KEY) as UNIQUE_CUSTOMERS,
    SUM(fs.SALES_AMOUNT) as TOTAL_REVENUE,
    AVG(fs.SALES_AMOUNT) as AVG_ORDER_VALUE
FROM FACTS.FACT_SALES fs
JOIN DIMENSIONS.DIM_STORE ds ON fs.STORE_KEY = ds.STORE_KEY
GROUP BY ds.PROVINCE
ORDER BY TOTAL_REVENUE DESC;
```

## 🛠️ Troubleshooting

### Common Issues
1. **Permission Errors**: Check role assignments and privileges
2. **Performance Issues**: Verify warehouse sizing and clustering
3. **Data Quality**: Review data quality monitoring views
4. **Connection Issues**: Verify Snowflake credentials and network access

### Monitoring
- Use `ANALYTICS.DATA_QUALITY_DASHBOARD` for data quality issues
- Check `AUDIT.AUDIT_MONITORING` for access and security events
- Monitor `ANALYTICS.PERFORMANCE_MONITORING` for performance issues
- Review `ANALYTICS.SECURITY_MONITORING` for security alerts

## 📚 Additional Resources

### Documentation
- [Snowflake Documentation](https://docs.snowflake.com/)
- [SQL Reference](https://docs.snowflake.com/en/sql-reference/)
- [Best Practices](https://docs.snowflake.com/en/user-guide/best-practices-overview.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Training
- [Snowflake University](https://learn.snowflake.com/)
- [Hands-on Labs](https://docs.snowflake.com/en/user-guide/labs.html)
- [Certification](https://www.snowflake.com/certifications/)

## 🤝 Contributing

This project demonstrates comprehensive Snowflake capabilities for sales data analysis. To contribute:

1. Review the existing structure and patterns
2. Follow the established naming conventions
3. Ensure proper security and governance implementation
4. Test thoroughly before deployment
5. Update documentation for any changes

## 📄 License

This project is provided as-is for educational and demonstration purposes. Please ensure compliance with your organization's data governance and security policies.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Snowflake documentation
3. Consult with your Snowflake administrator
4. Review audit logs and monitoring views

---

**Project Version**: 1.0  
**Last Updated**: December 2024  
**Snowflake Version**: Compatible with all current versions  
**Maintainer**: Data Engineering Team  
**Focus**: Pakistan Sales Data Analysis with OLTP/OLAP Architecture
