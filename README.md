# 🚛 CargoSync  
### Modular Fleet & Logistics Management System  
> Replacing manual logbooks with a centralized, rule-based digital fleet command center.

---

## 🏆 Hackathon Submission

**Theme:** Smart Logistics | Operational Efficiency | Digital Transformation  

### ❓ Problem Statement

Small and mid-scale logistics companies still rely on:

- ❌ Manual logbooks  
- ❌ Excel sheets  
- ❌ WhatsApp-based dispatching  
- ❌ No compliance validation  
- ❌ No real-time cost analytics  

This leads to:

- Poor fleet utilization  
- Unsafe dispatching  
- Fuel & maintenance overspending  
- Lack of driver monitoring  
- No operational intelligence  

---

## 💡 Solution — CargoSync

CargoSync is a **modular fleet management platform** that digitizes:

- 🚚 Fleet lifecycle management  
- 📦 Trip dispatch workflow  
- 🔧 Maintenance logs  
- ⛽ Fuel & expense tracking  
- 👤 Driver compliance  
- 📊 Operational analytics  

---

# 🎯 Objective

To build a centralized logistics operating system that:

- Optimizes fleet utilization
- Prevents unsafe trip creation
- Tracks operational costs per vehicle
- Monitors driver compliance
- Generates ROI-based fleet analytics

---

# 👥 Target Users

| Role | Responsibilities |
|------|------------------|
| Fleet Manager | Vehicle health & asset lifecycle |
| Dispatcher | Assign trips & validate cargo |
| Safety Officer | Monitor driver compliance |
| Financial Analyst | Track fuel spend & ROI |

---

# 🖥️ Core System Modules

---

## 1️⃣ Authentication & Role-Based Access

- Secure Email/Password login
- Role-Based Access Control (RBAC)
- Protected dashboard routes

---

## 2️⃣ Command Center (Main Dashboard)

A real-time fleet overview panel.

### 📊 Key Performance Indicators (KPIs)

- 🚚 Active Fleet (Vehicles On Trip)
- 🔧 Maintenance Alerts (Vehicles In Shop)
- 📦 Pending Cargo
- 📈 Utilization Rate (% assigned vs idle)

### 🎛 Filters

- Vehicle Type (Truck / Van / Bike)
- Status
- Region

---

## 3️⃣ Vehicle Registry (Asset Management)

CRUD system for physical fleet assets.

### Data Points

- Model / Name
- License Plate (Unique ID)
- Max Load Capacity (kg/tons)
- Odometer Reading
- Status (Available / In Shop / Retired)

---

## 4️⃣ Trip Dispatcher & Management

### Trip Lifecycle

Draft → Dispatched → Completed → Cancelled

### 🔐 Smart Validation Rule

If Cargo Weight > Vehicle Max Capacity → Block Trip Creation

### Automated State Updates

- On Dispatch → Vehicle & Driver = "On Trip"
- On Completion → Status = "Available"

---

## 5️⃣ Maintenance & Service Logs

Preventative and reactive fleet health tracking.

### ⚙ Smart Logic

- Adding vehicle to Service Log automatically sets:
  Status → In Shop
- Vehicle becomes unavailable for dispatch
- Prevents accidental assignment

---

## 6️⃣ Fuel & Expense Logging

Track financial performance per vehicle.

### Captured Data

- Fuel Liters
- Cost
- Date
- Vehicle ID

### 🧮 Automated Calculation

Total Operational Cost = Fuel + Maintenance

---

## 7️⃣ Driver Performance & Safety Profiles

Compliance and performance monitoring.

### Features

- 📅 License Expiry Tracking (Blocks assignment if expired)
- 📈 Trip Completion Rate
- 🛡 Safety Score
- 🟢 Status Toggle (On Duty / Off Duty / Suspended)

---

## 8️⃣ Operational Analytics & Reports

Data-driven decision making.

### 📊 Metrics

- Fuel Efficiency (km / L)
- Vehicle ROI  
  ROI = (Revenue - (Fuel + Maintenance)) / Acquisition Cost
- Cost-per-km
- Utilization Trends

### 📤 Export Options

- CSV Export
- PDF Reports
- Monthly Financial Audit Sheets

---

# 🔁 System Workflow Example

1. Add Vehicle "Van-05" (500kg capacity) → Status: Available  
2. Add Driver "Alex" → License Verified  
3. Assign 450kg load → Validation Pass  
4. Dispatch → Status: On Trip  
5. Trip Completed → Status: Available  
6. Log Oil Change → Status: In Shop  
7. Analytics auto-updates cost-per-km  

---

# 🛠 Tech Stack

## Frontend
- React.js / Next.js
- Tailwind CSS
- Framer Motion
- Modular Dashboard Components

## Backend
- Node.js
- Express.js
- REST APIs
- Real-time state logic

## Database
- MongoDB / PostgreSQL
- Relational linking:
  - Trips → Vehicle ID
  - Expenses → Vehicle ID
  - Driver → Assigned Trips

## Dev Tools
- Git & GitHub
- Postman
- Figma / Excalidraw (System Design)

---

# 🚀 Why CargoSync Stands Out

- Real-world logistics problem
- Rule-based validation engine
- Smart status automation
- Modular scalable architecture
- Financial + Operational + Compliance tracking in one system
- Ready to scale into SaaS

---

# 🌍 Future Enhancements

- Live GPS tracking
- AI-based predictive maintenance
- Driver behavior analytics
- Multi-warehouse support
- Blockchain-based shipment verification
- Dedicated mobile app for drivers

---

# 📦 Repository Structure

/client  
/server  
/models  
/controllers  
/routes  
/utils  

---

# 👨‍💻 Team CargoSync

Built with precision for operational excellence.

---

# 📜 License

Built for hackathon submission and educational purposes.
