from fmp_wrapper import FmpWrapper
import pandas as pd

fmp = FmpWrapper()

# aapl_profile = fmp.profile("AAPL")
# aapl_quote = fmp.quote(["AAPL"])
# aapl_hist = fmp.price_history("AAPL")
# aapl_fratios = fmp.financial_ratios(["AAPL"])
# aapl_ev = fmp.enterprise_value("AAPL", period="annual")
# keymets = fmp.key_metrics("AAPL", period="quarterly")
# f_growth = fmp.financial_growth("AAPL", period="quarter")
# aapl_rating = fmp.company_ratings("AAPL")
# dis_cf = fmp.discounted_cash_flow('AAPL')
dis_cf_hist = fmp.discounted_cash_flow('AAPL', period="quarter", historical=True)
