# Day 62 – Coffee & WiFi Website 

##  Project Overview
A Flask web application that allows users to discover cafes based on their coffee quality, WiFi availability, and power outlet access.

Users can also add new cafes through a form, making it easy to build a collection of laptop-friendly cafes.

##  What You'll Build
A Coffee & WiFi website where users can:
- View a list of available cafes.
- Add new cafes to the collection.
- See cafe details, including location, opening hours, and ratings.
- Rate coffee, WiFi, and power outlet availability.

## 🚀 Features
- **Home Page:** Introduces the Coffee & WiFi website.
- **Add Cafe:** Allows users to submit new cafe information.
- **All Cafes:** Displays cafe information from a CSV file.
- **Form Validation:** Ensures required fields are completed and URLs are valid.
- **CSV Storage:** Saves cafe information for future display.
- **Bootstrap Styling:** Provides a clean and responsive interface.

##  Concepts Practised
- Flask routes and HTTP methods (GET and POST).
- WTForms and form validation.
- Flask-Bootstrap.
- SelectField and URLField.
- Reading and writing CSV files with Python.
- Jinja templating and template inheritance.
- HTML tables and Bootstrap styling.

##  Project Flow
1. Users visit the homepage.
2. They can navigate to the cafe collection.
3. They can open the Add Cafe page.
4. They submit cafe details through a form.
5. Flask validates the submitted information.
6. Valid cafe details are saved to `cafe-data.csv`.
7. The All Cafes page displays the saved cafe information.

## ️ Technologies Used
- Python
- Flask
- Flask-WTF
- WTForms
- Flask-Bootstrap
- HTML
- CSS
- CSV

##  How to Run
1. Clone or download the repository.
2. Open the project folder.
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python main.py
   ```

5. Open the local development URL shown in your terminal.

---

**100 Days of Python – Day 62 Complete!** 

Another step forward in my Python and web development journey.