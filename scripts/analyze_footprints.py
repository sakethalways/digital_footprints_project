import pandas as pd

def analyze_footprints(social_media_usage, online_shopping):

    df = pd.read_csv('data/user_data_large.csv') 
    

    avg_social_media = df['social_media_usage'].mean()
    avg_online_shopping = df['online_shopping'].mean()
    
    analysis_result = {
        'social_media_usage': social_media_usage,
        'avg_social_media_usage': avg_social_media,
        'online_shopping': online_shopping,
        'avg_online_shopping': avg_online_shopping
    }
    
    return analysis_result
