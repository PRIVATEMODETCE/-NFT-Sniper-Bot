import streamlit as st

st.set_page_config(
    page_title="NFT Sniper Bot",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("NFT Sniper Bot")
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Manage Patterns", "Transactions", "Settings"]
)

if menu == "Dashboard":
    st.title("📊 Dashboard")
    st.write("Welcome to the NFT Sniper Bot dashboard.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Monitored Markets", "3")
    col2.metric("Active Patterns", "5")
    col3.metric("Successful Purchases", "12")
    
    st.subheader("Floor Price Trends")
    st.line_chart([100, 98, 97, 99, 96]) 

elif menu == "Manage Patterns":
    st.title("🔍 Manage Patterns")
    
    st.subheader("Add New Pattern")
    with st.form("add_pattern_form"):
        pattern = st.text_input("Pattern (Regex)", placeholder="e.g., xxxx abab")
        max_price = st.number_input("Max Price", min_value=0.0, step=0.1)
        submitted = st.form_submit_button("Add Pattern")
        if submitted:
            st.success(f"Pattern '{pattern}' with max price {max_price} added!")
    
    st.subheader("Existing Patterns")
    st.table({
        "Pattern": ["xxxx abab", "1234 xxxx"],
        "Max Price": [90, 85]
    })

elif menu == "Transactions":
    st.title("💳 Transactions")
    st.write("List of recent and pending transactions.")
    st.table({
        "Date": ["2024-12-03", "2024-12-02"],
        "Pattern": ["xxxx abab", "1234 xxxx"],
        "Price": [88, 82],
        "Status": ["Success", "Pending"]
    })

elif menu == "Settings":
    st.title("⚙️ Settings")
    st.subheader("Wallet Configuration")
    st.text_input("Wallet Address", placeholder="Enter your TON wallet address")
    st.text_input("Private Key", placeholder="Enter your private key (encrypted storage)")
    
    st.subheader("Notification Settings")
    st.text_input("Telegram Bot Token")
    st.text_input("Telegram Chat ID")
    st.text_input("Email Address")
    st.button("Save Settings")
