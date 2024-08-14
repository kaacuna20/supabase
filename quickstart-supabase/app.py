import streamlit as st

st.title("Supabase Task Manager")

# Agregar la navegación entre páginas
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Create Task", "View Tasks"])

if page == "Create Task":
    import pages.create_task
elif page == "View Tasks":
    import pages.view_tasks
