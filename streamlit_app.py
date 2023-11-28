import streamlit as st
import urllib.parse
import json
import requests
from bs4 import BeautifulSoup

def generate_link(json_data):
    base_url = "http://api.cache.dweave.net/cache/?"
    
    # Customize the parameters based on your JSON structure
    params = {
        "urlh": json_data["seed_urlh"],
        "crawl_type": json_data["crawl_type"],
        "crawl_time": json_data["crawl_time"],
        "source": json_data["source"],
    }

    # Encode the parameters and concatenate them to the base URL
    link = base_url + urllib.parse.urlencode(params)
    return link

def find_sitemaps(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        sitemaps = [link.get('href') for link in soup.find_all('a', {'href': True}) if 'sitemap' in link.get('href').lower()]
        return sitemaps
    except Exception as e:
        return str(e)

def main():
    st.title("Web Tools")

    # Section 1: Link Generator
    st.header("Link Generator")

    # Add a text area for pasting JSON data
    json_data_str = st.text_area("Paste JSON data here:")

    try:
        # Try to parse the JSON data
        if json_data_str:
            json_data = json.loads(json_data_str)
            # If JSON data is provided, generate and display the link
            if json_data:
                link = generate_link(json_data)
                st.markdown(f"**Generated Link:** {link}")
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please provide valid JSON data.")
        return

    

    # Section 2: Sitemap Finder
    st.header("Sitemap Finder")

    # Explicitly display the text input for entering the website URL
    website_url = st.text_input("Enter website URL:")

    # If URL is provided, find and display sitemaps
    if st.button("Find Sitemaps"):
        if website_url:
            sitemaps = find_sitemaps(website_url)
            if isinstance(sitemaps, list):
                st.markdown("**Found Sitemaps:**")
                for sitemap in sitemaps:
                    st.markdown(f"- {sitemap}")
            else:
                st.error(f"Error finding sitemaps: {sitemaps}")

if __name__ == "__main__":
    main()
