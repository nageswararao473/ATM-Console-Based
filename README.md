# ATM-Console-Based
Here's a more detailed description for your GitHub repository:  

---

# 🏦 ATM System in Python  

This is a simple **ATM (Automated Teller Machine) simulation program** written in Python. It provides basic banking functionalities like withdrawals, deposits, PIN generation, and mini statements for users. The system maintains account details, transaction history, and PIN security for authentication.  

## 📌 Features  

### 1️⃣ **Withdraw Money**  
- Users can withdraw money after entering their account number and correct PIN.  
- The system checks for sufficient funds before processing the withdrawal.  
- Transaction history is updated automatically.  

### 2️⃣ **Deposit Money**  
- Users can deposit money into their account by entering the deposit amount.  
- The account balance is updated accordingly.  
- The deposit transaction is recorded in the mini statement.  

### 3️⃣ **PIN Generation**  
- If an account does not have a PIN, users can create one.  
- The system ensures that the user confirms the PIN before setting it.  
- Once set, the PIN cannot be changed (in this version).  

### 4️⃣ **Mini Statement**  
- Displays user details including **Name, Account Number, Date of Birth, and Balance**.  
- Shows the last **5 transactions**, including deposits and withdrawals.  

### 5️⃣ **Security & Account Verification**  
- PIN authentication is required for withdrawals and viewing mini statements.  
- Transactions are recorded and limited to the last 5 entries per account.  
- Only accounts stored in the system can be accessed.  

## 🛠 How It Works  

1. Run the script in a **Python 3.x environment**.  
2. Choose an option from the **main menu**.  
3. Enter the required details (**Account Number, PIN, Amount, etc.**).  
4. The system processes the request and updates the account details.  
5. Repeat transactions or exit when done.  

## 🔗 Technologies Used  
- **Python** (Core logic and functionality)  
- **Dictionaries** for storing account details and transactions  
- **Conditional Statements & Loops** for user interaction  

## 🚀 Future Enhancements  
This is a basic version of an ATM system. Future improvements may include:  
- Adding more **banking operations** (e.g., fund transfer, account creation).  
- Implementing a **database** for persistent storage instead of dictionaries.  
- Allowing users to change their **PIN** securely.  
- Improving the **user interface** with a GUI (Tkinter or PyQt).  

## 📌 How to Run  
1. Install Python 3.x if not already installed.  
2. Download or clone this repository.  
3. Run the script using:  
   ```sh
   python atm_system.py
   ```  
4. Follow the on-screen instructions to perform ATM transactions.  

---

This description provides a complete overview of your ATM system, making it suitable for GitHub. Let me know if you need any modifications! 🚀💻
