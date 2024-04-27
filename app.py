import streamlit as st
import wikipedia as wp


def getWikiSearchSuggestions(query):
    try:
        page = wp.search(query,results = 5)
        suggestions = [str(p.title) for p in page]
        return suggestions
    except:
        return ["Nothing Found"]

def main():
    st.title("WikiQuest")
    st.header("Your WikiPedia Guide") # Header

    st.markdown("***") # HR

    st.text("")

    st.write("Search For Anything")
    text_search = st.text_input("") # Search Bar

    # Getting Search Suggestions : 
    suggestions = getWikiSearchSuggestions(text_search)

    if suggestions:
        selected_suggestion = st.selectbox("Select",options = suggestions)

    st.header(text_search)
    

if __name__ == "__main__":
    main()