

from app.stocks import format_usd

def test_usd_formatting():
    # assert 2 + 2 == 4

    assert format_usd(4.5) == "$4.50"
    assert format_usd(4.5555) == "$4.56"
    assert format_usd(46789) == "$46,789.00"

