# Personal Restaurant Dashboard

A data analytics project that collects real-world restaurant data using the **Google Maps Places API**, stores and analyzes it using **SQL**, and visualizes insights through **Tableau / Power BI**.  
The goal of this project is to demonstrate an **end-to-end data workflow** suitable for internship and early-career data roles.

---

## Project Overview

This project focuses on analyzing **high-rated restaurants (≥ 4.0 stars)** within a **5 km radius of Brampton, Ontario**.  
Rather than relying on pre-existing datasets, all data is **collected programmatically** via APIs, cleaned, structured, queried, and visualized.

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
- **Database:** PostgreSQL / SQLite
- **Data Analysis:** SQL
- **Visualization:** Tableau or Power BI
- **Version Control:** Git & GitHub

---

##  Dataset Scope

- Restaurants within **5 km of my location**
- Minimum rating: **4.0**
- Fields collected:
  - Name
  - Rating
  - Total number of reviews
  - Cuisine / category
  - Address
  - Latitude & longitude
  - Price level (if available)
  - Delivery/takeout availability (if available)

---

## Development Roadmap

### Phase 1: Data Collection (In Progress)
- [x] Set up Google Maps Places API
- [x] Fetch nearby restaurants using latitude & longitude
- [x] Handle pagination to collect >20 results
- [] Filter restaurants with rating ≥ 4.0
- [ ] Save cleaned data to CSV / JSON

---

### Phase 2: Database Design & SQL
- [ ] Design relational database schema
  - `restaurants`
  - `locations`
  - `ratings`
  - `categories`
- [ ] Import API data into SQL database
- [ ] Normalize data to reduce redundancy
- [ ] Write analytical SQL queries:
  - Average rating by cuisine
  - Restaurant density by area
  - Rating vs. price level
  - Top-rated restaurants by review count

---

### Phase 3: Data Analysis & Insights
- [ ] Validate and clean missing or inconsistent data
- [ ] Identify trends in ratings and cuisine popularity
- [ ] Compare delivery vs. non-delivery ratings
- [ ] Prepare SQL views for visualization tools

---

### Phase 4: Visualization (Tableau / Power BI)
- [ ] Connect BI tool to SQL database
- [ ] Create visualizations:
  - Bar charts (ratings by cuisine)
  - Maps (restaurant distribution)
  - Heatmaps (price vs. rating)
- [ ] Add interactivity (filters, slicers, tooltips)
- [ ] Build a polished dashboard for presentation

---

### Phase 5: Reporting & Documentation
- [ ] Write a project summary explaining:
  - Data collection process
  - Database structure
  - Key SQL queries
  - Analytical insights
- [ ] Publish dashboard (Tableau Public / Power BI Service)
- [ ] Finalize README and repository structure

---

