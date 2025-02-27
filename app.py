import streamlit as st
import requests


import os
from dotenv import load_dotenv


load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def fetch_linkedin_profiles(full_name, company_name):
    search_query = f'site:linkedin.com/in "{full_name}" "{company_name}"'
    url = "https://serpapi.com/search"
    
    params = {
        "engine": "google",
        "q": search_query,
        "api_key": 'a876b4ec319bb35b25ad79057c09f613ad5333d58eaaaf1951a3ea8d03cc39d8'
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    links = []
    for result in data.get("organic_results", []):
        link = result.get("link")
        if "linkedin.com/in" in link:
            links.append(link)
    
    return links[:20]  


st.title("LinkedIn Profile Finder")

full_name = st.text_input("Enter Full Name:")
company_name = st.text_input("Enter Company Name:")

if st.button("Find LinkedIn Profiles"):
    if full_name and company_name:
        profiles = fetch_linkedin_profiles(full_name, company_name)
        
        if profiles:
            st.write("### Top LinkedIn Profiles:")
            for link in profiles:
                st.markdown(f"[🔗 {link}]({link})")
        else:
            st.write("No profiles found. Try refining the search.")
    else:
        st.warning("Please enter both full name and company name.")
