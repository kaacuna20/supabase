import streamlit as st
from supabase import create_client, Client
import os

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# Verifica la autenticación
if 'user' not in st.session_state or st.session_state.user.role != 'authenticated':
    st.error("You must be logged in to view tasks.")
else:
    st.header("Your Tasks")
    
    # Obtener las tareas del usuario
    tasks = supabase.table("tasks").select("*").eq("user_id", st.session_state.user.id).execute()
    
    if tasks.data:
        st.write(tasks.data)
    else:
        st.write("You have no tasks.")
