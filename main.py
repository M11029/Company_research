import streamlit as st
import requests
import json
from openai import OpenAI
import config  # Import the config file containing API keys

# Set page configuration
st.set_page_config(page_title="Company Info App", layout="wide")

def main():
    # Initialize session state if not already set
    if 'step' not in st.session_state:
        st.session_state['step'] = 'welcome'
    
    # Navigation based on current step in session state
    if st.session_state['step'] == 'welcome':
        welcome_screen()
    elif st.session_state['step'] == 'select_companies':
        select_companies()
    elif st.session_state['step'] == 'show_company_details':
        show_company_details()

def welcome_screen():
    st.title("Welcome to the Company Info App")
    
    # Introduction text
    st.write("Please enter a list of company names to get started.")
    
    # Input for company names
    company_input = st.text_area("Enter company names (one per line):")
    
    if st.button("Search Companies"):
        company_names = company_input.strip().split('\n')
        company_names = [name.strip() for name in company_names if name.strip()]
        
        if company_names:
            st.session_state['company_names'] = company_names
            st.session_state['step'] = 'select_companies'
        else:
            st.warning("Please enter at least one company name.")

def select_companies():
    st.title("Select Companies")
    
    if 'company_names' not in st.session_state:
        st.warning("No company names found. Please go back to the main page.")
        return
    
    confirmed_companies = {}
    companies_house_api_key = config.COMPANIES_HOUSE_API_KEY  # Get API key from config
    
    for company_name in st.session_state['company_names']:
        st.subheader(f"Results for '{company_name}'")
        
        # Search Companies House API
        headers = {'Authorization': companies_house_api_key}
        params = {'q': company_name}
        response = requests.get(
            'https://api.company-information.service.gov.uk/search/companies',
            headers=headers,
            params=params
        )
        
        if response.status_code != 200:
            st.error(f"Error fetching data for '{company_name}'. Please check your API key.")
            return
        
        data = response.json()
        items = data.get('items', [])
        
        if not items:
            st.write(f"No results found for '{company_name}'.")
            continue
        
        # Show top 5 results as a dropdown
        options = []
        for item in items[:5]:
            options.append(f"{item.get('title')} (Company Number: {item.get('company_number')})")
        
        selected = st.selectbox(f"Select the correct company for '{company_name}':", options, key=company_name)
        
        # Store the selected company number
        selected_index = options.index(selected)
        selected_company = items[selected_index]
        company_number = selected_company.get('company_number')
        
        confirmed_companies[company_name] = company_number
    
    if st.button("Confirm"):
        st.session_state['confirmed_companies'] = confirmed_companies
        st.session_state['step'] = 'show_company_details'

def show_company_details():
    st.title("Company Details")
    
    if 'confirmed_companies' not in st.session_state:
        st.warning("No confirmed companies found.")
        return
    
    companies_house_api_key = config.COMPANIES_HOUSE_API_KEY
    companies = st.session_state['confirmed_companies']
    
    # Set OpenAI API key from config
    openai_api_key = config.OPENAI_API_KEY
    client = OpenAI(api_key=openai_api_key)
    
    # Get News API key from config
    news_api_key = config.NEWS_API_KEY
    
    tabs = st.tabs(list(companies.keys()))
    
    for idx, company_name in enumerate(companies.keys()):
        with tabs[idx]:
            company_number = companies[company_name]
            # Fetch company details from Companies House API
            headers = {'Authorization': companies_house_api_key}
            response = requests.get(
                f'https://api.company-information.service.gov.uk/company/{company_number}',
                headers=headers
            )
            
            if response.status_code != 200:
                st.error(f"Error fetching details for '{company_name}'.")
                continue
            
            company_data = response.json()
            
            # Display important information
            st.subheader(f"{company_data.get('company_name')} (Company Number: {company_number})")
            important_info = {
                'Company Status': company_data.get('company_status'),
                'Incorporation Date': company_data.get('date_of_creation'),
                'Registered Office Address': company_data.get('registered_office_address')
            }
            
            st.write("**Important Information:**")
            for key, value in important_info.items():
                st.write(f"- {key}: {value}")
            
            # Dropdown to select more information
            additional_info_options = ['SIC Codes', 'Accounts', 'Officers']
            selected_info = st.multiselect("Select additional information to view:", additional_info_options, key=f"info_{company_name}")
            
            if 'SIC Codes' in selected_info:
                sic_codes = company_data.get('sic_codes', [])
                st.write("**SIC Codes:**")
                for code in sic_codes:
                    st.write(f"- {code}")
            
            if 'Accounts' in selected_info:
                accounts = company_data.get('accounts', {})
                st.write("**Accounts:**")
                st.json(accounts)
            
            if 'Officers' in selected_info:
                # Fetch officers
                officers_response = requests.get(
                    f'https://api.company-information.service.gov.uk/company/{company_number}/officers',
                    headers=headers
                )
                if officers_response.status_code == 200:
                    officers_data = officers_response.json()
                    officers = officers_data.get('items', [])
                    st.write("**Officers:**")
                    for officer in officers:
                        st.write(f"- {officer.get('name')} ({officer.get('officer_role')})")
                else:
                    st.write("Could not retrieve officers information.")
            
            # Recent news section
            st.write("**Recent News:**")
            news_params = {
                'q': company_name,
                'apiKey': news_api_key,
                'pageSize': 5,
                'sortBy': 'publishedAt'
            }
            news_response = requests.get('https://newsapi.org/v2/everything', params=news_params)
            if news_response.status_code == 200:
                news_data = news_response.json()
                articles = news_data.get('articles', [])
                if articles:
                    for article in articles:
                        st.write(f"- [{article.get('title')}]({article.get('url')})")
                else:
                    st.write("No recent news found.")
            else:
                st.write("Error fetching news articles.")
            
            # Generate 250-word summary
            st.write("**Summary:**")
            summary_prompt = f"Provide a 250-word summary for the company {company_data.get('company_name')} using the following information.\n\n"
            summary_prompt += f"Company Information:\n{json.dumps(company_data, indent=2)}\n\n"
            summary_prompt += "Recent News Articles:\n"
            if 'articles' in locals() and articles:
                for article in articles:
                    summary_prompt += f"- {article.get('title')}: {article.get('description')}\n"
            else:
                summary_prompt += "No recent news articles available.\n"
            
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes company information."},
                        {"role": "user", "content": summary_prompt}
                    ],
                    max_tokens=400,
                    temperature=0.7
                )
                summary = response.choices[0].message.content.strip()
                st.write(summary)
            except Exception as e:
                st.write("Error generating summary:", e)

if __name__ == "__main__":
    main()