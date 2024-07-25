
# Task 2: Sentiment Tally


# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

###python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
###negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
 

def pos_additions ():
    keywords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    count=0
    for review in python_reviews:
        for word in keywords:
            x = review.count(word)
            count+= x
        #print(x)
    print("Based on the current product reviews, we a have total of ", count, "Postive words")


def neg_additions ():
    keywords = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    count=0
    for review in python_reviews:
        for word in keywords:
            x = review.count(word)
            count+= x
    
    print("Based on the current product reviews, we a have total of ", count, "Negative words")
    

def main():
    flag = True
    while flag:
        commands = input(''' 
Positive and Negative word detector.
Please select your option:                                                 
1- To sum-up all positive words.
2- To sum-up all negative words.
3- Quit.
''')
        print("="*60)
        print("="*60) 

        if commands == "1":
            print("you have selected option 1 ")
            pos_additions()

        elif commands == "2":
            print("you have selected option 2 ")
            neg_additions()

        elif commands == "3":
            flag = False
            print("you have selected option 3 ")
            print("Application closing, Goodbye")

        else:
            print(" incorrect entry, try again.")

main()