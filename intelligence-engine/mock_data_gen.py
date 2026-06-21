import json
import random
from datetime import datetime, timedelta
import pytz

def generate_series(start_price, days, volatility=0.02, trend=0.001):
    series = []
    current_price = start_price
    now = datetime.now()
    for i in range(days):
        timestamp = (now - timedelta(days=i)).strftime('%Y-%m-%dT%H:%M:%SZ')
        change_pct = 1 + (trend + random.uniform(-volatility, volatility))
        current_price *= change_pct
        series.append({"t": timestamp, "p": round(current_price, 2)})
    return series

def get_market_metadata():
    now = datetime.now()
    return {
        "timestamp": now.strftime('%Y-%m-%d %H:%M:%S'),
        "markets": {
            "ASX": {"location": "Sydney, Australia", "timezone": "AEST"},
            "NASDAQ": {"location": "New York, USA", "timezone": "EST"},
            "FTSE": {"location": "London, UK", "timezone": "GMT"},
            "S&P 500": {"location": "New York, USA", "timezone": "EST"}
        },
        "last_pulse": {
            "utc": now.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "local_context": "Market Open - Sydney"
        }
    }

data = {
    "metadata": get_market_metadata(),
    "asset_intelligence": {
        "target": "LTR.ASX",
        "peers": ["SQM", "ALB"],
        "peer_performance": "Strong (ALB +7.0% on upgrades)",
        "divergence": {
            "status": "Positive Divergence",
            "description": "LTR.ASX and peer sector (Albemarle) showing strength despite downward pressure in Lithium spot prices."
        },
        "current_metrics": {
            "price": 3.50,
            "change_24h": "+1.2%",
            "change_1m": "-2.5%",
            "status": "DIVERGENCE ALERT"
        },
        "historical_data": {
            "target": generate_series(3.50, 365, 0.04, 0.0005),
            "peers": {
                "ALB": generate_series(95.00, 365, 0.03, -0.0002)
            }
        },
        "model_validation": {
            "confidence": 75,
            "win_rate": 68,
            "rmse": 0.12
        }
    },
    "commodity_intelligence": {
        "lithium": {
            "spot_price_cny": 167250,
            "daily_change_pct": -1.33,
            "monthly_change_pct": -10.32,
            "trend": "Bearish (Supply Glut)",
            "signals": ["Supply/Demand: Monthly decline suggests inventory glut", "Geopolitical: Ongoing monitoring of trade/subsidy trends"]
        }
    },
    "market_intelligence": {
        "macro_sentiment": {
            "nasdaq": "+1.02%",
            "sp500": "-0.94%",
            "asx200": "+0.54%",
            "status": "Contagion/Gap"
        }
    }
}

with open("mock_data.json", "w") as f:
    json.dump(data, f, indent=2)
