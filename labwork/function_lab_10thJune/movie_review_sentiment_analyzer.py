# Movie Review Sentiment Analyzer 
"""
Problem Statement 
Movie reviews are stored as follows: 
reviews = [     
"excellent movie",     
"average story",     
"excellent acting",     
"poor direction",     
"excellent visuals",     
"poor screenplay",     
"good music",     
"excellent climax",     
"average performance",     
"good cinematography" ] 
Requirements Create the following functions: 
    1. count_sentiments(reviews) 
    Counts: 
        • Excellent  
        • Good  
        • Average  
        • Poor reviews  
    2. most_common_word(reviews) 
    Returns the most frequently occurring word. 
    3. longest_review(reviews) 
    Returns the review containing the maximum number of characters. 
    4. reviews_with_keyword(reviews, keyword) 
    Displays all reviews containing a given keyword.
"""
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# ==========================================
# Function to count sentiments
# ==========================================
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    return excellent, good, average, poor


# ==========================================
# Function to find the most common word
# ==========================================
def most_common_word(reviews):
    words = []

    for review in reviews:
        words.extend(review.split())

    common_word = ""
    max_count = 0

    for word in words:
        count = words.count(word)

        if count > max_count:
            max_count = count
            common_word = word

    return common_word


# ==========================================
# Function to find the longest review
# ==========================================
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# ==========================================
# Function to display reviews with keyword
# ==========================================
def reviews_with_keyword(reviews, keyword):
    print(f"Reviews containing '{keyword}':")

    for review in reviews:
        if keyword in review:
            print(review)


# ==========================================
# Main function to execute the requirements
# ==========================================
if __name__ == "__main__":

    excellent, good, average, poor = count_sentiments(reviews)

    print(f"Excellent Reviews: {excellent}")
    print(f"Good Reviews: {good}")
    print(f"Average Reviews: {average}")
    print(f"Poor Reviews: {poor}")

    print("\nMost Common Word:")
    print(most_common_word(reviews))

    print("\nLongest Review:")
    print(longest_review(reviews))

    print()
    reviews_with_keyword(reviews, "excellent")