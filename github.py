import argparse
import requests
import sys


def main():
    username = fetch_username()
    events = fetch_events(username)
    if not events:
        print("No recent public activity has been found.")

    for event in events:
        print(event["type"])
        print(event["repo"]["name"])
        print(event["created_at"])


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events/public"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as httperror:
        sys.exit(f"HTTP error occurred: {httperror}")
    except requests.exceptions.ConnectionError:
        sys.exit("Unable to establish a connection")
    except requests.exceptions.Timeout:
        sys.exit("The request has timeouted")
    except requests.exceptions.RequestException:
        sys.exit("An issue has been encountered")


def fetch_username():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="enter a github username", type=str)
    args = parser.parse_args()
    return args.username


if __name__ == "__main__":
    main()
