import pyshorteners

def url_shortener(long_url):
    # Initialize the PyShorteners object
    s = pyshorteners.Shortener()

    # Shorten the URL
    short_url = s.tinyurl.short(long_url)

    return short_url

if __name__ == "__main__":
    # Get the URL from the user
    long_url = input("Enter the URL to shorten: ")

    # Shorten the URL
    shortened_url = url_shortener(long_url)

    # Display the shortened URL
    print(f"Shortened URL: {shortened_url}")
