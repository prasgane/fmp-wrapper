# Financial Modeling Prep API Wrapper
This project provides a python wrapper for the [Financial Modeling Prep API](https://financialmodelingprep.com/developer/docs).

## Installation

In a shell, execute `pip install fmp-wrapper`.

Optionally, you can clone this project by running `git clone https://github.com/cccdenhart/fmp-wrapper`.

## Usage

Only a select number of features from the API are implemented here as of now. They are described below.

If you want any additional features implemented, feel free to open an issue.

Data is returned as a [Pandas](https://pandas.pydata.org/) dataframe by default. The wrapper can also be configured to simply return raw json data.

### Examples
**Import wrapper**

```
from fmp_wrapper import FmpWrapper
fmp = FmpWrapper()
# OR fmp = FmpWrapper(as_pandas=False) for raw data returns
```

**Stock Profile**

```
aapl_profile = fmp.profile("AAPL")
```

**Stock Quotes**

```
aapl_quote = fmp.quote(["AAPL", "MSFT"])
```

**Financial Reports**

```
aapl_income = fmp.financials("AAPL", "income")  # default period is annual
appl_balance = fmp.financials("AAPL", "balance", period="annual")
aapl_cash_flow = fmp.financials("AAPL", "cash", period="quarter")
```

**Price History**

```
aapl_all_prices = fmp.price_history("AAPL")
```



