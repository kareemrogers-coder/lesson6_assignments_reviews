#Question1

# Product Review Analysis


# Objective: The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.


# Task 1: Keyword Highlighter


# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]


new_reviews= str(python_reviews) ### the list into a string

print("The original python_reviews", new_reviews) ### Print out the original reviews

print("="*50)
print("="*50)

key_word = ["good", "excellent", "bad", "poor", "average"] ####identify the keywords 

for update_reviews in key_word: 
    new_reviews = new_reviews.replace(update_reviews, update_reviews.upper()) # replace all keywords in key_words list into a upper version.

print('''Below are the new Reviews with highlighted keywords:
''',new_reviews)
