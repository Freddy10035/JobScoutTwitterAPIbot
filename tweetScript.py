import os
import time
import requests
from dotenv import load_dotenv
from tweepy import Client

load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# API endpoint for retrieving job data
job_api_endpoint = 'http://localhost/all-jobs-api/api/v1/jobs/'

# Bearer token for API authentication
bearer_token = os.getenv("ALL_JOBS_API_BEARER_TOKEN")

# Set the authorization header
job_headers = {'Authorization': f'Bearer {bearer_token}'}

# Fetch job data from the API with authentication
job_response = requests.get(job_api_endpoint, headers=job_headers)
jobs = job_response.json()
# print(jobs)

# Limit the number of tweets
tweet_limit = 30
tweet_count = 0


# Function to shorten URLs using the TinyURL API
def shorten_url(url):
    tiny_url_api_token = os.getenv("TINY_URL_API_TOKEN")
    tiny_url_endpoint = "https://api.tinyurl.com/create"
    tiny_url_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {tiny_url_api_token}"
    }
    tiny_url_payload = {
        "url": url
    }

    tiny_url_response = requests.post(tiny_url_endpoint, headers=tiny_url_headers, json=tiny_url_payload)
    tiny_url_response_json = tiny_url_response.json()
    shortened_url = tiny_url_response_json['data']['tiny_url']
    # print(shortened_url)  # Print the response for debugging purposes
    return shortened_url  # Replace with the correct short URL retrieval logic


# Define the categories you want to post jobs for
categories_to_post = ["Accounting, Auditing & Finance", "Software & Data",
                      "Engineering & Technology", "Marketing & Communications",
                      "Creative & Design", "Research, Teaching & Training"]

# Define the maximum number of jobs per category
max_jobs_per_category = 5

# Initialize a dictionary to store the count of jobs posted for each category
jobs_per_category = {category: 0 for category in categories_to_post}

# Loop through each job and post it to Twitter
for job in jobs['data']:
    job_title = job['job_title']
    company_name = job['company_name']
    job_location = job['job_location']
    job_function = job['job_function']
    min_qualifications = job['min_qualifications']
    job_salary = job['job_salary']
    experience_length = job['experience_length']
    job_link = job['job_link']

    # Check if the job's category is in the categories_to_post list
    if job_function in categories_to_post:

        # Check if the maximum number of jobs per category has been reached
        if jobs_per_category[job_function] >= max_jobs_per_category:
            continue

        # Shorten the job link
        short_job_link = shorten_url(job_link)

        # Construct the tweet message
        tweet = f"🌟 Job Alert: {job_title}\n\n🏢 {company_name} is hiring!\n\n📍 Location: {job_location}\n🔧 Category: {job_function}\n🎓 Qualifications: {min_qualifications}\n💰 Salary: {job_salary}\n⏳ Experience: {experience_length}\n\n🔗 Apply here: {short_job_link}"

        # Check if the tweet exceeds the character limit
        if len(tweet) > 280:
            print("Tweet is too long and cannot be posted as a single tweet.")
            continue

        # Post the tweet
        try:
            client.create_tweet(text=tweet)
            print("Tweet posted successfully:\n", tweet)
            tweet_count += 1
            time.sleep(5)
        except Exception as e:
            print("An error occurred while posting the tweet:", str(e))

        # Check if the tweet limit has been reached
        if tweet_count >= tweet_limit:
            break

print(f'{tweet_count} tweets posted successfully!')
