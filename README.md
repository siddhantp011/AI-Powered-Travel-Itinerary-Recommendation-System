# AI-Powered-Travel-Itinerary-Recommendation-System
The AI-Powered Travel Itinerary Recommendation System helps travelers generate personalized day-wise holiday plans based on their interests, trip duration, travel style, and destination preferences. It uses Machine Learning (TF-IDF Similarity) to match user interests with activity data and dynamically creates a travel itinerary.

🎯 2. Objective

To build a simple AI itinerary recommendation system that:

Understands traveler interests

Suggests location-specific activities

Automatically organizes them into a day-wise plan

Provides an intuitive interface for user interaction

3. Technologies Used
Category	Technology
Programming Language	Python
Web Framework	Streamlit
Machine Learning Method	TF-IDF + Cosine Similarity
Data Format	JSON
Supporting Libraries	Pandas, NumPy, Scikit-Learn

4. Machine Learning Model
Algorithm

📌 TF-IDF Vectorization
Converts text data (descriptions + categories + names) into numerical vectors representing relevance.

📌 Cosine Similarity
Calculates how closely the user interest matches each activity.

Output Generation

Filter activities based on selected destination

Rank highest similarity first

Select top activities = Days × 3

Arrange as a day-wise itinerary

| Feature                 | Description                              |
| ----------------------- | ---------------------------------------- |
| Interest-Based Search   | Multi-category selection                 |
| Destination Filter      | Only relevant city options recommended   |
| Adaptive Day Planning   | Activities divided per day               |
| UI/UX Simplified Design | Clean layout for user inputs and results |

Sample Output

Input Example
Interest: ❝Beaches, Nightlife❞
Destination: Goa
Days: 2

Generated Itinerary

Day 1:
- Baga Beach: Relax and enjoy water sports
- Tito’s Lane Nightlife: Clubs & parties

Day 2:
- Anjuna Beach: Cliff views and cafés
- Beach shack dining: Sunset meal
