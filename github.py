import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="enter a github username", type=str)
    args = parser.parse_args()

    username = args.username

    
if __name__ == "__main__":
    main()