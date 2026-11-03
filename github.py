import argparse
import requests
import sys
import json


def main():
    username = fetch_username()
    events = fetch_events(username)
    if not events:
        sys.exit("No recent public activity has been found.")

    # print(json.dumps(events, indent=4))
    display_events(events)



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
        sys.exit("The request timed out.")
    except requests.exceptions.RequestException:
        sys.exit("An issue has been encountered")


def fetch_username():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="enter a github username", type=str)
    args = parser.parse_args()
    return args.username

def display_events(events):
    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
            print(f"Pushed commits to {repo_name}")
            print(event["payload"])
        elif event_type == "WatchEvent":
            print(f"Starred {repo_name}")
            print(event["payload"])
        else:
            print(f"Performed {event_type} in {repo_name}")
            print(event["payload"])


if __name__ == "__main__":
    main()
