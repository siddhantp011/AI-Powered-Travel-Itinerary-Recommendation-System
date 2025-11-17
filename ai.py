# -------------------------------
# travel_ai.py
# -------------------------------
# Run: pip install streamlit scikit-learn
# Command: streamlit run travel_ai.py
# -------------------------------

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

st.set_page_config(page_title="India Travel AI Itinerary Builder", layout="wide")

# ------------------- Data -------------------
categories = {
    "Adventure": ["Skydiving", "Mountain Hiking", "Zip Lining", "Scuba Diving", "Camping"],
    "Culture": ["Art Museums", "Historical Sites", "Local Food Tour", "Live Theatre Show", "Cultural Workshops"],
    "Nature": ["Beach Day", "Wildlife Safari", "Botanical Garden Visit", "River Cruise", "Waterfall Trek"],
    "Food & Drinks": ["Winery Tour", "Street Food Crawl", "Fine Dining", "Coffee Tasting", "Brewery Tour"],
    "Relaxation": ["Spa Day", "Yoga Retreat", "Beach Resort", "Hot Springs", "Sunset Viewing"]
}

destinations = ["Goa","Rajasthan","Kerala","Himachal Pradesh","Uttarakhand","Ladakh",
                "Mumbai","Delhi","Agra","Varanasi","Kolkata","Tamil Nadu","Karnataka",
                "Andaman & Nicobar","Sikkim","Kashmir"]

# Build activity bank
activity_bank = []
for cat, acts in categories.items():
    for name in acts:
        for dest in random.sample(destinations, 3):
            activity_bank.append({
                "name": name,
                "description": f"{name} is a wonderful activity in {dest}.",
                "category": cat,
                "destination": dest
            })

corpus = [f"{a['name']} {a['description']} {a['category']} {a['destination']}" for a in activity_bank]
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(corpus)

# ------------------- Function -------------------
def recommend_itinerary(destination, interests, days, activities_per_day=3):
    user_text = f"{destination} {' '.join(interests)}"
    user_vec = vectorizer.transform([user_text])
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()
    sorted_indices = similarities.argsort()[::-1]

    filtered = [activity_bank[i] for i in sorted_indices if activity_bank[i]['destination'] == destination]
    itinerary = []

    for d in range(days):
        day_acts = filtered[d*activities_per_day:(d+1)*activities_per_day]
        if not day_acts:
            break
        day_obj = {
            "day": d+1,
            "title": f"Day {d+1} Adventures",
            "activities": []
        }
        for act in day_acts:
            day_obj["activities"].append({
                "time": random.choice(["Morning","Afternoon","Evening"]),
                "activity": act['name'],
                "description": act['description'],
                "duration": f"{random.randint(1,3)} hours",
                "estimatedCost": f"₹{random.randint(500,2000)}"
            })
        itinerary.append(day_obj)

    return {
        "destination": destination,
        "overview": f"A {days}-day trip to {destination} covering your interests: {', '.join(interests)}.",
        "bestTime": "October - March",
        "days": itinerary,
        "tips": ["Carry sunscreen", "Stay hydrated", "Try local food", "Use local transport for convenience"],
        "estimatedTotalCost": f"₹{days*1500} - ₹{days*5000} per person"
    }

# ------------------- Streamlit UI -------------------
st.title("🇮🇳 India Travel AI Itinerary Builder")

# Sidebar inputs
with st.sidebar:
    destination = st.selectbox("Select Destination", [""] + destinations)
    duration = st.number_input("Trip Duration (days)", min_value=1, max_value=30, value=3)
    interests = st.multiselect("Select Interests", sum(categories.values(), []))
    budget = st.selectbox("Budget Level", ["Budget (₹500-1500/day)", "Moderate (₹1500-4000/day)", "Luxury (₹4000+/day)"])
    travel_style = st.selectbox("Travel Style", ["Relaxed", "Balanced", "Action-Packed"])
    generate_btn = st.button("Generate Itinerary")

# Generate itinerary
if generate_btn:
    if not destination or not interests:
        st.error("Please select destination and at least one interest.")
    else:
        itinerary = recommend_itinerary(destination, interests, duration)
        st.subheader(f"Trip Overview for {destination}")
        st.write(itinerary["overview"])
        st.write(f"Best Time to Visit: {itinerary['bestTime']}")
        st.write(f"Estimated Total Cost: {itinerary['estimatedTotalCost']}")

        # Day-wise display
        for day in itinerary["days"]:
            with st.expander(f"Day {day['day']}: {day['title']}"):
                for act in day["activities"]:
                    st.markdown(f"**{act['time']}** - {act['activity']} ({act['duration']}) - {act['estimatedCost']}")
                    st.write(act["description"])

        st.subheader("Travel Tips")
        for tip in itinerary["tips"]:
            st.markdown(f"- {tip}")

# ------------------- End of File -------------------
