import os
from dotenv import load_dotenv
import requests
import csv

load_dotenv('project.env')
places_api_key = os.getenv("PLACES_API_KEY") 
home_lat = float(os.getenv("HOME_LAT")) 
home_lng = float(os.getenv("HOME_LON"))

def get_restaurants_grid(api_key, center_lat, center_lng):
    url = "https://places.googleapis.com/v1/places:searchNearby"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.currentOpeningHours,places.priceRange,places.servesVegetarianFood"
    }

    
    offsets = [-0.015, 0, 0.015] 
    all_restaurants = {} 

    for lat_off in offsets:
        for lng_off in offsets:
            current_lat = center_lat + lat_off
            current_lng = center_lng + lng_off
            
            data = {
                "includedTypes": ["restaurant"],
                "maxResultCount": 20,
                "locationRestriction": {
                    "circle": {
                        "center": {"latitude": current_lat, "longitude": current_lng},
                        "radius": 1500.0 
                    }
                }
            }

            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                places = response.json().get('places', [])
                for p in places:
                    place_id = p.get('id')
                    all_restaurants[place_id] = p 
            else:
                print(f"Error at {current_lat}: {response.text}")

    # Exporting restaurant data to CSV
    csv_filename = "restaurants.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Display Name', 
            'Formatted Address', 
            'Rating', 
            'User Rating Count', 
            'Open Now', 
            'Price Range', 
            'Serves Vegetarian Food'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for p_id, p in all_restaurants.items():
            name = p.get('displayName', {}).get('text', 'N/A')
            address = p.get('formattedAddress', 'N/A')
            rating = p.get('rating', 'N/A')
            reviews = p.get('userRatingCount', 0)
            opening_hours = p.get('currentOpeningHours', {}).get('openNow', 'N/A')
            veggie = p.get('servesVegetarianFood', 'N/A')
            
            p_range = p.get('priceRange', {})
            if p_range:
                start = p_range.get('startPrice', {}).get('units', '')
                end = p_range.get('endPrice', {}).get('units', '')
                currency = p_range.get('startPrice', {}).get('currencyCode', '')
                range_text = f"{currency} {start}-{end}"
            else:
                range_text = "N/A"
            
            writer.writerow({
                'Display Name': name,
                'Formatted Address': address,
                'Rating': rating,
                'User Rating Count': reviews,
                'Open Now': opening_hours,
                'Price Range': range_text,
                'Serves Vegetarian Food': veggie
            })
    
    print(f"\n✅ Successfully exported {len(all_restaurants)} unique restaurants to '{csv_filename}'")
    
    # Displaying results(testing putposes)
    print(f"\nFound {len(all_restaurants)} unique restaurants.\n" + "="*40)
    for p_id, p in all_restaurants.items():
        name = p.get('displayName', {}).get('text', 'N/A')
        rating = p.get('rating', 'N/A')
        reviews = p.get('userRatingCount', 0)
        address = p.get('formattedAddress', 'No address') 
        opening_hours = p.get('currentOpeningHours', {}).get('openNow', 'N/A')
        veggie = "✅ Veggie Options" if p.get('servesVegetarianFood') else "❌ No specific veggie flag"
        p_range = p.get('priceRange', {})
        range_text = ""

        if p_range:
            start = p_range.get('startPrice', {}).get('units', '')
            end = p_range.get('endPrice', {}).get('units', '')
            currency = p_range.get('startPrice', {}).get('currencyCode', '')
            range_text = f"({currency} {start}-{end})"
        else: 
            range_text = "(N/A)"
        
        print(f"🍴 {name} ({rating}⭐ based on {reviews} reviews)")
        print(f"📍 {address}")
        print(f"⏰ Status: {opening_hours} | {veggie}")
        print(f"💲 Price Range: {range_text}")
        print("-" * 40)
        

# Brampton Center Coordinates
get_restaurants_grid(places_api_key, home_lat, home_lng)
