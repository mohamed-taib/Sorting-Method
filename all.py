import streamlit as st

# Sidebar for navigation
pages = {
    "Home": "home",
    "Heap Sort": "p2",
    "Insertion Sort": "p3",
    "Selection Sort": "p4",
}

# Sidebar selection
page = st.sidebar.selectbox("Select a Sorting Algorithm", options=list(pages.keys()))

# Display the selected page
if page == "Home":
    import home  # Home page content
elif page == "Heap Sort":
    import p2  # Heap Sort page content
elif page == "Insertion Sort":
    import p3  # Insertion Sort page content
elif page == "Selection Sort":
    import p4  # Selection Sort page content
