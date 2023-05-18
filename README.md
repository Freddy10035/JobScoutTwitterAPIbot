# Description:

The JobScoutTwitterAPIbot is a Python script that automates the process of posting job openings to Twitter. It fetches job data from a custom API, constructs tweets with relevant job information, and posts them to a Twitter account using the Tweepy library. The bot also includes functionality to shorten URLs using the TinyURL API to fit within Twitter's character limit.

**Features:**
- Retrieves job data from a custom API using authentication.
- Constructs informative tweets with job details including job title, company name, location, job function, qualifications, salary, and experience level.
- Shortens job URLs using the TinyURL API to fit within Twitter's character limit.
- Posts job tweets to a Twitter account using the Tweepy library.
- Handles errors gracefully and displays appropriate error messages.

**Installation:**

1. Clone the repository or download the script files.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the necessary environment variables in a `.env` file or your preferred method. Required variables include:
   - `CONSUMER_KEY`: Twitter API consumer key.
   - `CONSUMER_SECRET`: Twitter API consumer secret.
   - `ACCESS_TOKEN`: Twitter API access token.
   - `ACCESS_TOKEN_SECRET`: Twitter API access token secret.
   - `TINY_URL_API_TOKEN`: Token for accessing the TinyURL API.
   - `ALL_JOBS_API_BEARER_TOKEN`: Bearer token for API authentication.
4. Customize the `job_api_endpoint` variable to point to your desired job data API endpoint.
5. Run the script using `python tweetScript.py`.

**Usage:**

1. Ensure the required environment variables are correctly set with valid credentials.
2. Customize the `job_api_endpoint` variable to point to your desired job data API endpoint.
3. Adjust the `tweet_limit` variable to control the number of tweets to post.
4. Run the script using `python tweetScript.py`.
5. The bot will fetch job data, construct tweets, and post them to the specified Twitter account.

**Contributing:**

Contributions to the JobScoutTwitterAPIbot are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request.

