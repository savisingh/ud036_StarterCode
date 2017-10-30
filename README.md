# Project: Movie Trailer Website - Savneet Singh

This website will display the *movie name*, the *box art* of the movie and when you 
click on the movie it will show the *movie trailer*.

## Required Libraries and Dependencies

- Python
  - Install **Python 2.7.14** at https://www.python.org/downloads/ 
 
## How to Run the Project

- Navigate to the folder you downloaded containing the Python files
- Open the `project_entertainment_centre.py` with IDLE and run the module (F5 key on Mac) 
- A webpage should open displaying the movies

## Code Explained

- `project_media.py` contains the class `Movie()` that stores your favourite movies, 
including movie title, box art URL and a YouTube link to the movie trailer.

- `project_entertainment_centre.py` is a Python class that creates *multiple instances* 
 to represent your favourite movies  
 
- Udacity provides a starter code repository that contains a Python module called
 `fresh_tomatoes.py`
 
- `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your 
list of movies and generate an HTML file including this content, producing a website to
 showcase your favorite movies.
 
 ## Miscellaneous 
 
- Ensure `fresh_tomatoes.py` is in the **same directory** as your `project_media.py` and
 `project_entertainment_centre.py` files

## Potential Issues

- When running the code, I found that the webpage didn't display as I was hoping. 
The number of movies displayed on each row was not equal. 
The display should have shown three movies on each row and should have been uniform.

- To fix this issue, I added the **flexbox model** (flexible box) solution as follows:

` .container {
	display: flex;
	flex-wrap: wrap;
}`

- The flex container gets declared by setting the `display` property, in this case it is 
set to `flex` so is rendered as a block. The Flexbox model doesn't use floats like the block model.

- The `flex-wrap` property is set to `wrap` which ensures the flexible items will wrap if necessary.

- Another way to have solved this problem could have been using a **clearfix** solution; another way to clear floats.





