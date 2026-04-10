tea_prices_inr = {
    "Masala Chai": 50,
    "Ginger Chai": 45,
    "Green Tea": 40,
    "Cardamom Chai": 55,
    "Iced Lemon Tea": 60,
    "Iced Peach Tea": 65
}

tea_prices_usd = {tea: price/90 for tea, price in tea_prices_inr.items()}
print(f"Tea prices in USD: {tea_prices_usd}")

