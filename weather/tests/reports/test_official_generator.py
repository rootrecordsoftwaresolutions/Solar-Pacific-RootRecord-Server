from reports.official_generator import _source_name


def test_nws_sources_group_together():
    assert _source_name("https://api.weather.gov/products/types/AFD/locations/HFO") == "NWS-HFO"
    assert _source_name("https://www.weather.gov/hfo/office_products") == "NWS-HFO"
    assert _source_name("https://forecast.weather.gov/product.php?site=HFO") == "NWS-HFO"


def test_nhc_isolated():
    assert _source_name("https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=7") == "NHC"


def test_noaa_nesdis_isolated():
    assert _source_name("https://www.noaa.gov/") == "NOAA"
    assert _source_name("https://cdn.star.nesdis.noaa.gov/GOES18/ABI/SECTOR/hi/") == "NOAA-NESDIS"
