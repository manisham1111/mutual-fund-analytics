import pandas as pd
from sqlalchemy import create_engine

# Create database connection
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# Load cleaned files
fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
nav_history = pd.read_csv("data/processed/02_nav_history_clean.csv")
aum = pd.read_csv("data/processed/03_aum_by_fund_house_clean.csv")
sip = pd.read_csv("data/processed/04_monthly_sip_inflows_clean.csv")
category = pd.read_csv("data/processed/05_category_inflows_clean.csv")
folio = pd.read_csv("data/processed/06_industry_folio_counts_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
holdings = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")
benchmark = pd.read_csv("data/processed/10_benchmark_indices_clean.csv")

# Load into SQLite
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_history.to_sql("fact_nav", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
category.to_sql("fact_category_inflow", engine, if_exists="replace", index=False)
folio.to_sql("fact_folio_counts", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
holdings.to_sql("fact_portfolio_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark_indices", engine, if_exists="replace", index=False)

print("✅ All 10 tables loaded successfully into SQLite!")