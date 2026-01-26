# Personal Restaurant Dashboard

A data analytics project that collects real-world restaurant data using the **Google Maps Places API**, stores and analyzes it using **SQL**, and visualizes insights through **Power BI**. 
---

## Project Overview

This project focuses on analyzing vegetarian restaurants within a **5 km radius of my current location**.  
Rather than relying on pre-existing datasets, all data was collected via the use of Google Maps Places API. 

**Key Skills Demonstrated:**
- API-based data collection
- Data cleaning & normalization
- Relational database design (SQL)
- Analytical querying
- Business-focused data visualization
- Data Analysis

---

## Tech Stack

- **Data Collection:** Google Maps Places API
- **Programming Language:** Python
- **Database:**  SQLite
- **Data Analysis:** SQL
- **Visualization:** Power BI

---

##  Dataset Scope

- Restaurants within **5 km of my location**
- Fields collected:
  - Name
  - Rating
  - Total number of reviews
  - Serves vegetarian food
  - Address
  - Price range

---

## Development Roadmap

### Phase 1: Data Collection (In Progress)
- [x] Set up Google Maps Places API
- [x] Fetch nearby restaurants using latitude & longitude
- [x] Handle grid search to collect >20 results
- [X] Save cleaned data to CSV / JSON

---

### Phase 2: Database Design & SQL
- [X] Design relational database schema
  - `restaurants`
  - `locations`
  - `ratings`
- [x] Import API data into SQL database
- [X] Write analytical SQL queries:
  - Average rating by cuisine
  - Restaurant density by area
  - Rating vs. price level
  - Top-rated restaurants by review count

### Phase 4: Visualization (Tableau / Power BI)
- [X] Connect BI tool to SQL database
- [X] Create visualizations:
  - Bar charts (ratings by cuisine)
  - Maps (restaurant distribution)
  - Heatmaps (price vs. rating)
- [X] Build a polished dashboard for presentation

---

### Phase 5: Reporting & Documentation
- [ ] Write a project summary explaining:
  - Data collection process
  - Database structure
  - Key SQL queries
  - Analytical insights
- [ ] Publish dashboard (Power BI Service)
- [ ] Finalize README and repository structure

---

