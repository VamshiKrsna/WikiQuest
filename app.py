import streamlit as st
import wikipedia as wp
from streamlit_searchbox import st_searchbox

def getWikiSearchSuggestions(query):
    return wp.search(query) if query else ["Nothing Found"]

def main():
    st.title("WikiQuest")
    st.header("Your WikiPedia Guide") # Header
    st.markdown("***") # HR
    st.text("")
    # Search bar and suggestions : 
    selected_val = st_searchbox(
        getWikiSearchSuggestions,
        key="wiki_searchbox",
        placeholder="Search From Wikipedia"
    )
    if selected_val:
        st.write("Selected Value :",selected_val)

    
if __name__ == "__main__":
    main()