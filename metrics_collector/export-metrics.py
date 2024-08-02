import psycopg2
from prometheus_client import Gauge, start_http_server
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define Prometheus metrics
metric_current = Gauge('stock_current_price', 'Current stock price', ['symbol'])
metric_today_open = Gauge('stock_today_open', 'Stock price at market open today', ['symbol'])
metric_today_high = Gauge('stock_today_high', 'Stock highest price today', ['symbol'])
metric_today_low = Gauge('stock_today_low', 'Stock lowest price today', ['symbol'])
metric_weekly_high = Gauge('stock_weekly_high', 'Weekly highest stock price', ['symbol'])
metric_weekly_low = Gauge('stock_weekly_low', 'Weekly lowest stock price', ['symbol'])
metric_monthly_high = Gauge('stock_monthly_high', 'Monthly highest stock price', ['symbol'])
metric_monthly_low = Gauge('stock_monthly_low', 'Monthly lowest stock price', ['symbol'])
metric_yearly_high = Gauge('stock_yearly_high', 'Yearly highest stock price', ['symbol'])
metric_yearly_low = Gauge('stock_yearly_low', 'Yearly lowest stock price', ['symbol'])
metric_today_change = Gauge('stock_today_change', 'Change in stock price today', ['symbol'])
metric_week_change = Gauge('stock_week_change', 'Change in stock price over the week', ['symbol'])
metric_month_change = Gauge('stock_month_change', 'Change in stock price over the month', ['symbol'])
metric_year_change = Gauge('stock_year_change', 'Change in stock price over the year', ['symbol'])

def collect_metrics():
    """Collect metrics from the PostgreSQL database and expose them to Prometheus."""
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect("dbname=first_database user=postgres_user password=1234 host=db port=5432")
        cur = conn.cursor()
        
        # Query to get the stock data
        cur.execute('''
            SELECT "Symbol", "Current", "Today_Open", "Today_High", "Today_Low", 
                   "Weekly_High", "Weekly_Low", "Monthly_High", "Monthly_Low", 
                   "Yearly_High", "Yearly_Low", "Today_Change", "1_Week_Change", 
                   "1_Month_Change", "1_Year_Change"
            FROM company_data_test;
        ''')
        rows = cur.fetchall()
        
        # Update Prometheus metrics
        for row in rows:
            symbol = row[0]
            metric_current.labels(symbol=symbol).set(row[1])
            metric_today_open.labels(symbol=symbol).set(row[2])
            metric_today_high.labels(symbol=symbol).set(row[3])
            metric_today_low.labels(symbol=symbol).set(row[4])
            metric_weekly_high.labels(symbol=symbol).set(row[5])
            metric_weekly_low.labels(symbol=symbol).set(row[6])
            metric_monthly_high.labels(symbol=symbol).set(row[7])
            metric_monthly_low.labels(symbol=symbol).set(row[8])
            metric_yearly_high.labels(symbol=symbol).set(row[9])
            metric_yearly_low.labels(symbol=symbol).set(row[10])
            metric_today_change.labels(symbol=symbol).set(row[11])
            metric_week_change.labels(symbol=symbol).set(row[12])
            metric_month_change.labels(symbol=symbol).set(row[13])
            metric_year_change.labels(symbol=symbol).set(row[14])
        
        # Close the cursor and connection
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"Error collecting metrics: {e}")

if __name__ == '__main__':
    # Start the Prometheus metrics server
    start_http_server(7878)
    logging.info("Prometheus metrics server started on port 7878")

    # Main loop to update metrics periodically
    while True:
        collect_metrics()
        time.sleep(60)  # Collect data every 60 seconds

