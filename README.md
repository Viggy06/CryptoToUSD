# CryptoToUSD
A simple web server that convert specific amounts of Bitcoin (BTC), Ethereum (ETH) or Ripple (XRP) into US Dollars (USD) in automated fashion.
Data is taken from CoinGecko APIs
  - https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd  
  - https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd 
  - https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd
This endpoint take two URL parameters (e.g. `/exchange?coin=btc&amount=1.5`)
