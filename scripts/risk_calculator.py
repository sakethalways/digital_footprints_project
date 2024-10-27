def calculate_risk(social_media_usage, online_shopping):
    risk_score = 0
    
    # Risk assessment based on social media and online shopping thresholds
    if int(social_media_usage) > 6:
        risk_score += 50
    elif int(social_media_usage) > 3:
        risk_score += 30
    else:
        risk_score += 10

    if int(online_shopping) > 6:
        risk_score += 50
    elif int(online_shopping) > 3:
        risk_score += 30
    else:
        risk_score += 10
    
    # Ensure the risk score caps at 100
    risk_score = min(100, risk_score)
    
    return risk_score