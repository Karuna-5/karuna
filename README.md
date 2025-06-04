# Patient Management System (PAMS)

This project is a basic Django web application that simulates a patient data management module, developed as part of the Associate Software Engineer assignment for ClaimBuddy Technologies.

---

## Project Overview

The application allows users to view a list of patients with their details such as full name, age, gender, insurance provider, and policy number. It uses the **Stisla Admin Dashboard Template** for a clean and professional frontend UI.

---

## Features Implemented

- **Django Project Setup:** Created a Django project with an app named `pams`.
- **Patient Model:** Defined a `Patient` model with fields:
  - Full Name (CharField)
  - Age (IntegerField)
  - Gender (CharField with choices)
  - Insurance Provider (CharField)
  - Policy Number (CharField)
- **Dummy Data:** Added at least 5 dummy patients automatically on app initialization.
- **Patient List View:** Implemented a view and template to display all patients dynamically in a responsive table.
- **Frontend Integration:** Integrated the Stisla Admin Dashboard HTML, CSS, and JS files for a modern and clean UI.
- **Static Files Handling:** Configured static files properly for CSS and JS assets.

---

## How to Run

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
