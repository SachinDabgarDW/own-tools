import streamlit as st
import urllib.parse
import json

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

def main():
    st.title("Link Generator")

    # Add a text area for pasting JSON data
    json_data_str = st.text_area("Paste JSON data here:")

    try:
        # Try to parse the JSON data
        json_data = json.loads(json_data_str)
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please provide valid JSON data.")
        return

    # If JSON data is provided, generate and display the link
    if json_data:
        link = generate_link(json_data)
        st.markdown(f"**Generated Link:** {link}")

if __name__ == "__main__":
    main()
