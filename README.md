# Al-Ahly FC Management System Full Application Documentation

## Overview
This application is designed to manage Al-Ahly FC's operations, including members, teams, subscriptions, expenses, and reporting. It features a modern interface with a red, black, and white sporty theme. Reports are visualized with charts and tables for enhanced analysis.

---

## Features
1. **Members Management**
   - Add, view, edit, and delete members.
   - Track member details like name, email, phone number, and subscription status.

2. **Teams Management**
   - Manage teams and their assigned coaches.
   - View, add, and update team details.

3. **Subscriptions Management**
   - Record and monitor member subscription plans.
   - Plan types: Monthly, Quarterly, and Yearly.

4. **Expenses Management**
   - Track expenses related to teams and operations.
   - Record expense type, amount, and associated team.

5. **Reports**
   - Generate visual reports for operational data.
   - Reports include dynamic charts and tables for analysis.

---

## Installation and Setup
### Prerequisites
- Python 3.9+
- Django 4.x

### Steps
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Al-Ahly-FC
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open `http://127.0.0.1:8000/` in your web browser.

---

## Application Structure
### **Base Template**
- The `base.html` file provides the foundational layout, including the navigation bar and footer.
- The design is responsive and includes the Al-Ahly FC branding.

### **Apps**
1. **Members**
   - **Models:**
     - `Member`: Stores member details.
   - **Views:**
     - CRUD operations for members.
   - **Templates:**
     - Member list and form pages.

2. **Teams**
   - **Models:**
     - `Team`: Stores team names and coaches.
   - **Views:**
     - CRUD operations for teams.
   - **Templates:**
     - Team list and form pages.

3. **Subscriptions**
   - **Models:**
     - `Subscription`: Tracks subscription plans for members.
   - **Views:**
     - CRUD operations for subscriptions.
   - **Templates:**
     - Subscription list and form pages.

4. **Expenses**
   - **Models:**
     - `Expense`: Tracks expenses for teams.
   - **Views:**
     - CRUD operations for expenses.
   - **Templates:**
     - Expense list and form pages.

5. **Reports**
   - **Models:**
     - `ReportData`: Stores data for reports.
   - **Views:**
     - `reports_home`: Fetches data and passes it to the template for rendering charts and tables.
   - **Templates:**
     - Displays a table with columns `Month` and `Num. of Subscriptions`.
     - Visualizes data with a bar chart using Chart.js.

---

## Key Files
1. **`urls.py`**
   - Centralizes all app routes.
2. **`views.py`**
   - Handles the logic for fetching and processing data.
3. **Templates**
   - HTML files for all views.

---

## Reporting Feature
1. **Table**
   - Displays monthly subscription counts.
   - Headers: `Month` and `Num. of Subscriptions`.
2. **Chart**
   - Bar chart visualizing subscription counts.
   - Built with Chart.js.

---

## Usage
### Navigation
- Use the navbar to navigate between `Members`, `Teams`, `Subscriptions`, `Expenses`, and `Reports`.

### Adding Data
1. Navigate to the desired section (e.g., Members).
2. Click `Add` to create new entries.

### Viewing Reports
1. Go to the `Reports` section.
2. View the data table and chart.

---

## Future Enhancements
1. User authentication for restricted access.
2. Export reports to PDF or Excel.
3. Add more interactive visualizations.

---

## Troubleshooting
1. **Static Files Not Loading**
   - Run `python manage.py collectstatic`.
2. **Database Issues**
   - Ensure migrations are applied: `python manage.py migrate`.
3. **Chart Not Displaying**
   - Check the browser console for JavaScript errors.
   - Verify data is available in the `ReportData` model.

---

This documentation covers all aspects of the Al-Ahly FC Management System, including setup, features, and usage. Let me know if further details are required!
