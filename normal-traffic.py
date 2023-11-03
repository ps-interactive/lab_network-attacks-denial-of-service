import requests
import random
import time
import sys

# Sample user-agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use it like this: python {} http://example.com".format(sys.argv[0]))
        sys.exit()

    target_url = sys.argv[1]

    while True:
        user_agent = random.choice(USER_AGENTS)
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(target_url, headers=headers)
            print("Requested {} with status code: {}".format(target_url, response.status_code))
        except requests.RequestException as e:
            print(f"Error fetching {target_url}: {str(e)}")

        time.sleep(random.randint(1, 5))  # Sleep between 1 and 5 seconds before making another request
