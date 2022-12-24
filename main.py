import requests
import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the API request URL to fetch a fediverse accounts data by searching for an account.',
                                     epilog="Each account has a unique ID on any server where it is known. So you can not simply replace https://chaos.social/api/v1/accounts/107277650350084474 with https://mastodon.social/api/v1/accounts/107277650350084474")
    parser.add_argument('-s', '--server', help="The address of the server that's API you want to use (e.g. "
                                               "mastodon.social)")
    parser.add_argument('-u', '--user', help="The user that you are searching")
    parser.add_argument('-t', '--token', help="Authorization token")
    args = parser.parse_args()

    if args.server:
        server_for_api_raw = args.server
    else:
        server_for_api_raw = input("Which servers API do you want to use? (e.g. chaos.social)\n>")
    server_for_api_raw.replace("http://", "")
    server_for_api_raw.replace("https://", "")
    server_for_api_raw.replace("/", "")
    server_for_api = f"https://{server_for_api_raw}"
    if args.user:
        q_user = args.user
    else:
        q_user = input("Which user do you want to search?\n>")
    if not args.token:
        response = requests.get(f"{server_for_api}/api/v2/search?q={q_user}&type=accounts")
    else:
        headers = {
            'Authorization': args.token,
        }
        response = requests.get(f"{server_for_api}/api/v2/search?q={q_user}&type=accounts", headers=headers)


    users = json.loads(response.text)["accounts"]
    for idx, user in enumerate(users):
        # Check if user is on the server where the api is used
        if not "@" in user["acct"]:
            username = f"@{user['acct']}@{server_for_api_raw}"
        else:
            username = user['acct']
        print(f"{idx} {user['display_name']} ({username})")
    user_selected_idx = int(input("Select user\n> "))
    print(f"User account URL {server_for_api}/api/v1/accounts/{users[user_selected_idx]['id']}")


