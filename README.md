# APBank System

A Python-based command-line banking management system developed as a university assignment. It features a comprehensive role-based access control system, handling operations for Super Users, Admins, and Customers. The system relies on local text files for data persistence.

## ✨ Key Features

### 1. Role-Based Access Control
The system separates functionalities into three distinct user roles:

* **Super User**
  * Create new administrator accounts.
  * View all existing administrator profiles.

* **Admin**
  * Create and register new customer accounts.
  * View a list of all customer profiles.
  * Search for specific customer profiles using their Account ID.
  * Modify customer details (Password, Email, Contact Number, Address).
  * Generate and print a Customer's Statement of Account.

* **Customer**
  * **Deposit Funds:** Add money to their account.
  * **Withdraw Funds:** Withdraw money (includes logic to enforce minimum account balances based on account type).
  * **Check Balance:** View current account balance.
  * **Statement of Account:** Generate a filtered report of transactions within a specific date range.
  * **Profile Management:** Update their account password.

### 2. Account Types
* **Savings Account:** Requires a minimum balance of RM 100.
* **Current Account:** Requires a minimum balance of RM 500.

### 3. Data Persistence
All system data is stored locally in text files:
* `admin.txt` - Stores administrator credentials.
* `customer.txt` - Stores customer profiles, details, and current balances.
* `superuser.txt` - Stores superuser credentials.
* `transaction.txt` - Logs all deposits and withdrawals with timestamps.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation & Execution
1. Clone the repository or download the project files.
2. Ensure all text files (`admin.txt`, `customer.txt`, `superuser.txt`, `transaction.txt`) are located in the same directory as the main script.
3. Open a terminal or command prompt.
4. Navigate to the project directory:
   ```bash
   cd path/to/apbank
   ```
5. Run the application:
   ```bash
   python banking-system.py
   ```

## 🛠 Usage
Upon running the script, you will be greeted by the **Main Menu** displaying the current date and time.
Select an option by typing the corresponding number:
1. Super User Login
2. Admin Login
3. Customer Login
4. Exit

*(Note: Appropriate login credentials are required to access each portal.)*

## 📝 Technical Details
- **Language:** Python
- **Libraries Used:** `datetime` (for handling timestamps and date ranges in statements)
- **Data Format:** Comma-separated values within `.txt` files.
