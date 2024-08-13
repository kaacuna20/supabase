import streamlit as st
from supabase import create_client, Client


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = user.user
        st.success("Sign in successful!")
    except Exception as e:
        st.error(f"Error: {e}")

# Autenticación
if 'user' not in st.session_state or st.session_state.user.role != 'authenticated':
    st.header("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        sign_in(email, password)
        
else:
    st.write(f"Welcome, {st.session_state.user.email}!")
    
    # Crear tarea y subir archivo
    st.header("Create Task")
    task_title = st.text_input("Task Title")
    task_description = st.text_area("Task Description")
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])  # Especifica tipos de archivo permitidos

    if st.button("Create Task"):
        if uploaded_file is not None:
            try:
                # Guardar el archivo temporalmente
                file_path = f"temp_{uploaded_file.name}"
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())

                # Subir el archivo al bucket
                bucket = "tasks"  
                path_on_supastorage = f"{st.session_state.user.id}/{uploaded_file.name}"
                
                with open(file_path, "rb") as f:
                    res = supabase.storage.from_(bucket).upload(file=f, path=path_on_supastorage, file_options={"content-type": uploaded_file.type})

                # Obtener la URL pública del archivo
                file_url = supabase.storage.from_(bucket).get_public_url(path_on_supastorage)
                
                # Crear la tarea en la base de datos con el URL del documento
                new_task = supabase.table("tasks").insert({
                    "title": task_title,
                    "description": task_description,
                    "user_id": st.session_state.user.id,
                    "document_url": file_url
                }).execute()
                
                st.success("Task created successfully with document!")
                st.write(new_task)
                
                # Eliminar el archivo temporal
                import os
                os.remove(file_path)
                
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please upload a file before creating a task.")