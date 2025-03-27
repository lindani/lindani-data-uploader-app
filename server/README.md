# 🖥️ Server (Flask) - CSV Upload, Processing & Storage

## 📌 Overview
The Server is built with **Flask** and is responsible for:
- Accepting **CSV file uploads** from the frontend.
- Storing the uploaded **CSV files in AWS S3**.
- Processing the **CSV data** and storing it in **MongoDB**.
- Exposing API endpoints to retrieve the stored data.
- Providing pagination and search functionality for the frontend.

---

## 🚀 Features
- **File Upload**: Users can upload CSV files via the API.
- **AWS S3 Integration**: CSV files are stored securely in an AWS S3 bucket.
- **MongoDB Storage**: Processed CSV data is stored in a NoSQL database.
- **Data Retrieval**: API endpoints allow fetching, searching, and paginating stored records.
- **RESTful API**: Provides endpoints for managing uploaded data.

---
## 🔧 Setup & Installation
### **1️⃣ Prerequisites**
Ensure you have installed:
- **Python 3.10+**
- **MongoDB**
- **AWS S3 Credentials**
- **pip3** and **virtualenv**

### **2️⃣ Install & Run the Server**
#### **Step 1: Navigate to the Server Directory**
#### **Step 2: Run `python3 -m venv venv`**
#### **Step 3: Run `source venv/bin/activate`**
#### **Step 4: Run `pip3 install -r requirements.txt`**
#### **Step 5: Run `python3 server.py`**

