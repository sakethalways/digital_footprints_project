from flask import Flask, render_template, request
from scripts.analyze_footprints import analyze_footprints
from scripts.risk_calculator import calculate_risk
from scripts.visualizer import generate_visualizations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Get user input from the form
    username = request.form['username']
    social_media_usage = request.form['social_media']
    online_shopping = request.form['online_shopping']
    
    # Analyze footprints and calculate risk score
    analysis_result = analyze_footprints(social_media_usage, online_shopping)
    risk_score = calculate_risk(social_media_usage, online_shopping)
    
    # Generate visualizations as base64 strings
    social_media_image, shopping_image = generate_visualizations(social_media_usage, online_shopping)
    
    # Determine recommendations based on risk score
    if risk_score < 30:
        risk_message = "Low risk. Your online activity is fairly minimal."
        recommendations = ["You're doing great! Just keep an eye on your privacy settings from time to time."]
    elif 30 <= risk_score <= 50:
        risk_message = "Moderate risk. Consider being more cautious with your online activity."
        recommendations = [
            "Review privacy settings on all social media platforms.",
            "Avoid oversharing personal information online."
        ]
    elif 50 < risk_score <= 80:
        risk_message = "High risk. Your digital footprint may be exposing too much personal data."
        recommendations = [
            "Limit social media usage and review your account security settings.",
            "Be cautious with online shopping; use trusted sites and secure payment options.",
            "Consider using browser privacy extensions to reduce tracking."
        ]
    else:
        risk_message = "Severe risk. Your online activity is very high, posing significant privacy risks."
        recommendations = [
            "Limit social media and online shopping activities significantly.",
            "Review your digital footprint and remove any sensitive information.",
            "Consider consulting online privacy resources to secure your digital presence."
        ]

    # Render results.html with the analysis, risk score, and images
    return render_template('results.html', 
                           analysis=analysis_result, 
                           risk=risk_score, 
                           risk_message=risk_message,
                           recommendations=recommendations, 
                           social_media_image=social_media_image, 
                           shopping_image=shopping_image)

if __name__ == '__main__':
    app.run(debug=True)
