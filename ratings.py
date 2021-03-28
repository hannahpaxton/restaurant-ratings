"""Restaurant rating lister."""


# put your code here


#open the text file 
restaurant_data = open('scores.txt').readlines()

def create_restaurant_dict(restaurant_data):
    restaurant_ratings = {}
 
    for line in restaurant_data:
        line = line.rstrip()
        full_restaurant_data = line.split(':')
        restaurant = full_restaurant_data[0]
        rating = full_restaurant_data[1]

        #for restaurant, rating in restaurant_data:
        #restaurant_ratings.add(restaurant: rating)
        restaurant_ratings[restaurant] = rating
        print(restaurant + " is rated at " + rating)
    return restaurant_ratings

restaurant_ratings_2 = create_restaurant_dict(restaurant_data)

def user_restaurant_input_dict(restaurant_ratings):
    restaurant_name = input("Please enter restaurant name: ")
    restaurant_score = input("Please enter restaurant score: ")
    restaurant_ratings[restaurant_name] = restaurant_score
    return restaurant_ratings

print(user_restaurant_input_dict(restaurant_ratings_2))