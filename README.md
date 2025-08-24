# Snowflake Sales Data Analysis Project

## 🚀 Project Overview

This comprehensive Snowflake project demonstrates end-to-end sales data analysis capabilities, from data ingestion and staging to advanced analytics and business intelligence. The project showcases Snowflake's powerful features for data warehousing, analytics, and governance.

## 📊 Project Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   Staging      │    │   Production   │
│                 │    │                 │    │                 │
│ • sales_data.csv│───▶│ • Raw Tables   │───▶│ • Fact Tables  │
│ • orders*.csv   │    │ • File Formats │    │ • Dimension    │
│                 │    │ • Stages       │    │ • Views        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Analytics     │
                       │                 │
                       │ • BI Views      │
                       │ • Materialized  │
                       │ • Advanced SQL  │
                       └─────────────────┘
```

## 🏗️ Project Structure

### Database & Schemas
- **Database**: `SNOWFLAKE_SALES_DATA_ANALYSIS_DB`
- **Schemas**:
  - `STAGING`: Raw data ingestion and processing
  - `DEV`: Development and testing
  - `PROD`: Production data and analytics

### Warehouses
- `SNOWFLAKE_SALES_DATA_ANALYSIS_WH`: Main analytics warehouse
- `SALES_ANALYTICS_WH`: Dedicated analytics processing
- `SALES_LOADING_WH`: Data loading operations

## 📁 File Descriptions

### Core SQL Files

#### `ch02.sql` - Data Staging and Loading
- Creates staging infrastructure (stages, file formats, tables)
- Implements data loading procedures with error handling
- Sets up change data capture with streams
- Establishes data quality monitoring

#### `ch03.sql` - Data Transformation and BI
- Creates enriched fact and dimension tables
- Implements business logic and calculated fields
- Builds business intelligence views
- Sets up customer segmentation and product categorization

#### `ch04.sql` - Advanced Analytics
- Implements window functions for trend analysis
- Creates RFM (Recency, Frequency, Monetary) analysis
- Builds product lifecycle analytics
- Sets up geographic and territorial analysis

#### `ch05.sql` - Data Warehousing & Optimization
- Implements table clustering and optimization
- Creates materialized views for performance
- Sets up automated maintenance procedures
- Establishes data retention and archival policies

#### `ch07.sql` - Data Governance & Security
- Implements role-based access control (RBAC)
- Sets up data masking and encryption
- Creates row access policies
- Establishes audit logging and compliance

### Configuration Files

#### `snowflake.toml`
- Connection configurations for different environments
- Warehouse and database settings
- Authentication parameters

#### `db.txt`
- Complete database setup script
- Table creation and data loading
- Initial data population

#### `config.txt`
- Environment-specific configurations
- Connection parameters for development/production

### Data Files

#### `sales_data.csv`
- Main sales dataset with 2,825 records
- Contains order details, customer information, and product data
- Fields: Order details, quantities, prices, customer info, geographic data

## 🔧 Setup and Deployment

### Prerequisites
- Snowflake account with ACCOUNTADMIN privileges
- Snowflake CLI or web interface access
- Python environment (optional, for data processing)

### Quick Start

1. **Connect to Snowflake**
   ```sql
   -- Use the connection from snowflake.toml
   -- Connection: sales_analysis_prod
   ```

2. **Run Database Setup**
   ```sql
   -- Execute db.txt contents
   -- This creates the complete infrastructure
   ```

3. **Execute Chapter Files**
   ```sql
   -- Run in sequence: ch02.sql, ch03.sql, ch04.sql, ch05.sql, ch07.sql
   ```

### Step-by-Step Deployment

#### Phase 1: Infrastructure Setup
```sql
-- Execute db.txt to create database, schemas, and initial tables
-- This sets up the foundation for the entire project
```

#### Phase 2: Data Staging (ch02.sql)
```sql
-- Creates staging tables and data loading procedures
-- Implements error handling and data validation
-- Sets up change data capture
```

#### Phase 3: Data Transformation (ch03.sql)
```sql
-- Creates enriched tables with business logic
-- Implements customer and product hierarchies
-- Builds business intelligence views
```

#### Phase 4: Advanced Analytics (ch04.sql)
```sql
-- Implements advanced SQL analytics
-- Creates RFM analysis and customer segmentation
-- Builds product performance analytics
```

#### Phase 5: Optimization (ch05.sql)
```sql
-- Implements table clustering and optimization
-- Creates materialized views for performance
-- Sets up automated maintenance
```

#### Phase 6: Security & Governance (ch07.sql)
```sql
-- Implements role-based access control
-- Sets up data masking and security policies
-- Establishes compliance and audit procedures
```

## 📊 Key Features

### Data Management
- **Automated Data Loading**: Streamlined CSV ingestion with error handling
- **Data Quality Monitoring**: Comprehensive validation and quality checks
- **Change Data Capture**: Real-time data change tracking with streams
- **Data Retention**: Automated archival and cleanup procedures

### Analytics Capabilities
- **Business Intelligence Views**: Pre-built dashboards and reports
- **Advanced SQL Analytics**: Window functions, aggregations, and calculations
- **Customer Segmentation**: RFM analysis and customer classification
- **Product Analytics**: Performance tracking and lifecycle analysis
- **Geographic Analysis**: Territorial and regional performance insights

### Performance & Optimization
- **Table Clustering**: Optimized data distribution for query performance
- **Materialized Views**: Pre-computed aggregations for fast access
- **Warehouse Management**: Dedicated warehouses for different workloads
- **Query Optimization**: Performance monitoring and tuning

### Security & Governance
- **Role-Based Access Control**: Granular permissions for different user types
- **Data Masking**: Sensitive data protection based on user roles
- **Row Access Policies**: Territory and country-based data access control
- **Audit Logging**: Comprehensive activity tracking and monitoring
- **Data Classification**: Automated tagging and classification

## 👥 User Roles and Permissions

### Sales Analyst Role
- Access to sales data and customer information
- Limited access to sensitive customer details
- Can run analytics and generate reports
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
- Data loading and transformation access

### Data Scientist Role
- Access to production data for analysis
- Can create new tables and views
- Limited access to sensitive information
- Analytics and modeling capabilities

### Read-Only Role
- View-only access to production data
- No modification capabilities
- Basic reporting access
- Restricted to non-sensitive data

## 📈 Analytics and Reporting

### Pre-Built Views
- **Sales Performance Dashboard**: Comprehensive sales metrics
- **Customer Analytics**: Customer behavior and segmentation
- **Product Performance**: Product lifecycle and performance metrics
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
- **Predictive Insights**: Trend analysis and forecasting

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
- **Data Quality Monitoring**: Daily quality checks
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
1. **File Upload**: CSV files uploaded to staging
2. **Data Validation**: Quality checks and validation
3. **Error Handling**: Comprehensive error logging
4. **Data Loading**: Staged data loaded to production

### Processing
1. **Data Enrichment**: Business logic and calculations
2. **Transformation**: Data cleaning and standardization
3. **Aggregation**: Summary tables and materialized views
4. **Quality Assurance**: Continuous quality monitoring

### Delivery
1. **Analytics Views**: Pre-built dashboards and reports
2. **Materialized Views**: Performance-optimized aggregations
3. **Real-time Updates**: Change data capture and streaming
4. **Access Control**: Role-based data access

## 📊 Sample Queries

### Basic Sales Analysis
```sql
-- Total sales by year and month
SELECT YEAR_ID, MONTH_ID, SUM(SALES) as TOTAL_SALES
FROM PROD.SALES_FACT_ENRICHED
GROUP BY YEAR_ID, MONTH_ID
ORDER BY YEAR_ID DESC, MONTH_ID DESC;
```

### Customer Segmentation
```sql
-- Customer RFM analysis
SELECT * FROM PROD.CUSTOMER_RFM_ANALYSIS
WHERE CUSTOMER_SEGMENT = 'Champions'
ORDER BY RFM_TOTAL_SCORE DESC;
```

### Product Performance
```sql
-- Top performing products
SELECT * FROM PROD.PRODUCT_PERFORMANCE_MV
ORDER BY TOTAL_REVENUE DESC
LIMIT 10;
```

### Geographic Analysis
```sql
-- Regional performance
SELECT * FROM PROD.GEOGRAPHIC_PERFORMANCE
ORDER BY TOTAL_REVENUE DESC;
```

## 🛠️ Troubleshooting

### Common Issues
1. **Permission Errors**: Check role assignments and privileges
2. **Performance Issues**: Verify warehouse sizing and clustering
3. **Data Quality**: Review data quality monitoring views
4. **Security Issues**: Check masking policies and access controls

### Monitoring
- Use `PROD.DATA_QUALITY_DASHBOARD` for data quality issues
- Check `PROD.AUDIT_MONITORING` for access and security events
- Monitor `PROD.PERFORMANCE_MONITORING` for performance issues
- Review `PROD.SECURITY_MONITORING` for security alerts

## 📚 Additional Resources

### Documentation
- [Snowflake Documentation](https://docs.snowflake.com/)
- [SQL Reference](https://docs.snowflake.com/en/sql-reference/)
- [Best Practices](https://docs.snowflake.com/en/user-guide/best-practices-overview.html)

### Training
- [Snowflake University](https://learn.snowflake.com/)
- [Hands-on Labs](https://docs.snowflake.com/en/user-guide/labs.html)
- [Certification](https://www.snowflake.com/certifications/)

## 🤝 Contributing

This project is designed as a comprehensive example of Snowflake capabilities. To contribute:

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
