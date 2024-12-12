import pandas as pd
import random

# Generate data for 5000 users
usernames = [f"User_{i}" for i in range(1, 5001)]
social_media_usage = [random.randint(0, 15) for _ in range(5000)]  # Random usage between 0 and 15 times/day
online_shopping = [random.randint(0, 10) for _ in range(5000)]  # Random shopping frequency between 0 and 10 times/month

# Create a DataFrame
large_dataset = pd.DataFrame({
    "username": usernames,
    "social_media_usage": social_media_usage,
    "online_shopping": online_shopping
})

# Save the dataset
large_dataset.to_csv("user_data_large.csv", index=False)
print("Dataset saved as user_data_large.csv")
