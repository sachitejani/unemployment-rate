
# this is the "test/stocks_test.py" file...


from app.stocks import format_usd, fetch_stocks_data
from pandas import DataFrame

def test_usd_formatting():
    # assert 2 + 2 == 4

    assert format_usd(4.5) == "$4.50"
    assert format_usd(4.5555) == "$4.56"
    assert format_usd(46789) == "$46,789.00"

def test_data_fetching():

    result = fetch_stocks_data("NFLX")
    assert isinstance(result, DataFrame)
    assert "timestamp" in result.columns
    assert "adjusted_close" in result.columns
    assert "high" in result.columns
    assert "low" in result.columns

    assert len(result) >=100

