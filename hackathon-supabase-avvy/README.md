# Olympic Games Venues Paris 2024 - Streamlit Application

This project was developed during a hackathon organized by Avvy-Supabase, where the challenge was to create a final client application related to the Olympic Games within an hour and a half. I chose to build an interactive application using Streamlit, focusing on the venues of the Paris 2024 Olympic Games.

## Project Overview
The application provides a user-friendly interface where users can explore the venues for the Paris 2024 Olympic and Paralympic Games. The dataset used for this project was sourced from the official Paris 2024 data portal and includes detailed information about the competition venues. The application allows users to filter venues by category, sport, and start date, and visualize them on an interactive map.

## Features
- Category Filtering: Users can filter venues by category (Olympic or Paralympic).
- Sport Filtering: Users can narrow down the venues by specific sports.
- Date Filtering: Users can view venues based on the event's start date.
- Interactive Map: A map displays all filtered venues, allowing users to explore their locations with detailed popups.

## Dataset
The dataset used in this project was downloaded from the official Paris 2024 data portal. It contains comprehensive information on the venues for the 2024 Paris Olympic Games, including their names, sports, coordinates, and event dates.

- Dataset Source: [Paris 2024 Competition Venues Dataset](https://data.paris2024.org/explore/dataset/paris-2024-sites-de-competition/export/)

## Setup
To run this application on your local machine, please follow the instructions below:

1. Clone the Repository:
```ini 
    git clone https://github.com/kaacuna20/supabase.git
```

2. Navigate to the Project Directory:
```ini 
    cd hackathon-supabase-avvy
```

3. Install Dependencies:
```ini 
    pip install -r requirements.txt
```

4. Download the Dataset:

Download the dataset from this link and save it as paris-2024-sites-de-competition.csv in the root directory of the project.

5. Run the Application:

Execute the Streamlit application:
```ini 
    streamlit run app.py
```

6. Access the Application:

Once the application is running, you can access it in your web browser at `http://localhost:8501`.

## Dependencies
The required dependencies for this project are listed below and can be found in the `requirements.txt` file:

- `folium`
- `streamlit-folium`
- `streamlit`
- `pandas`

## Conclusion
This project demonstrates the power of quick prototyping using Streamlit for data visualization and interaction. Despite the time constraint of the hackathon, the application provides a comprehensive overview of the Paris 2024 Olympic venues, making it a valuable tool for users interested in the event.