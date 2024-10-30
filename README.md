# Learning Management System (LMS)

## Overview
This Learning Management System (LMS) project is designed to manage students, instructors, and courses. It provides functionality for creating, updating, and deleting records for each of these entities, along with a detailed view for each. The application uses Django as the backend framework and Bootstrap for the frontend.

## Features
- **Student Management**
  - List of students with the ability to view details, update information, and delete records.
  - Each student can be associated with multiple courses.

- **Instructor Management**
  - List of instructors with options to view details, update information, and delete records.
  - Instructors can teach multiple courses and have visibility into enrolled students.

- **Course Management**
  - List of courses with details, including enrolled students and associated instructors.
  - Options to update course information and delete records.

## Project Structure
The project is structured as follows:

### Templates
- **Student List (`student_list.html`)**: Displays all students and their enrolled courses.
- **Instructor List (`instructor_list.html`)**: Displays all instructors and the courses they teach.
- **Course List (`course_list.html`)**: Displays all courses, including instructor and student details.
- **Student Update (`student_update.html`)**: Form for updating student information.
- **Instructor Update (`student_update.html`)**: Form for updating instructor information.
- **Course Update (`student_update.html`)**: Form for updating course information.
- **Student Details (`student_details.html`)**: Displays detailed information about a specific student and their courses.
- **Instructor Details (`instructor_details.html`)**: Displays detailed information about a specific instructor and their courses.
- **Course Details (`course_details.html`)**: Displays detailed information about a specific course, including enrolled students.

### CSS and JavaScript
- The project uses Bootstrap 5 for styling and responsive design.

## Technologies Used
- **Django**: Python web framework for building the application.
- **Bootstrap**: CSS framework for responsive design and user interface components.
- **HTML**: Markup language for structuring web pages.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
