# Student Database Management System

## Student Profile Schema
The system captures and manages core demographic records for each student profile. The standard template data structure is defined below:

* **Name:** `Pranav` — Represents the full name of the student record.
* **Age:** `25` — Represents the chronological age of the individual, managed as a numerical value.
* **Gender:** `M` — Represents the gender identification character code.

---

## System Functionality & Operations
The application executes as an interactive, choice-driven program. Upon execution, the interface prompts the user with three specific structural options:

1. **Option 1: Add a Student into a File**
   * **Behavior:** Initiates an input prompt sequence to capture new student metrics (Name, Age, Gender).
   * **Storage:** Commits and appends the validated data directly into a persistent flat file repository.

2. **Option 2: View the File**
   * **Behavior:** Accesses the backend storage file to read all existing data entries.
   * **Output:** Displays the complete catalog of recorded students sequentially in the user console.

3. **Option 3: Exit**
   * **Behavior:** Terminates all ongoing operational loops.
   * **Outcome:** Safely closes any open file streams and ends the program execution cleanly.