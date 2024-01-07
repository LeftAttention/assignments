import boto3
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    user_review = event.get('user_review', '')

    if user_review:
        response = comprehend.detect_sentiment(Text=user_review, LanguageCode='en')

        # Extract sentiment result
        sentiment = response.get('Sentiment', 'UNKNOWN')

        logger.info(f"Sentiment of review '{user_review}': {sentiment}")
        return {
            'Sentiment': sentiment,
            'Review': user_review
        }
    else:
        logger.warning("No review text provided.")
        return {
            'Sentiment': 'No Review',
            'Review': None
        }
