import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64



def generate_visualizations(social_media_usage, online_shopping):

    df = pd.read_csv('data/user_data.csv')
    

    plt.figure(figsize=(10, 6))
    sns.histplot(df['social_media_usage'], bins=10, kde=True, color='blue', label="Others")
    plt.axvline(int(social_media_usage), color='red', label="Your Usage", linestyle="--")
    plt.title('Social Media Usage Comparison')
    plt.xlabel('Social Media Usage (times per day)')
    plt.ylabel('Frequency')
    plt.legend()

    buffer1 = BytesIO()
    plt.savefig(buffer1, format="png")
    plt.close()
    social_media_image = base64.b64encode(buffer1.getvalue()).decode()

 
    plt.figure(figsize=(10, 6))
    sns.histplot(df['online_shopping'], bins=10, kde=True, color='green', label="Others")
    plt.axvline(int(online_shopping), color='red', label="Your Shopping", linestyle="--")
    plt.title('Online Shopping Comparison')
    plt.xlabel('Online Shopping Frequency (times per month)')
    plt.ylabel('Frequency')
    plt.legend()

    buffer2 = BytesIO()
    plt.savefig(buffer2, format="png")
    plt.close()
    shopping_image = base64.b64encode(buffer2.getvalue()).decode()

    return social_media_image, shopping_image
