# Distributed E-Commerce Architecture Backend

A production-ready, distributed e-commerce microservice platform designed for high throughput, asynchronous task execution, and decoupled data layers. Built with a focus on optimized data structures, asynchronous processing, and horizontal scalability.

## 🚀 Key Architectural Features
* **Asynchronous Task Processing**: Integrated with **Celery** to offload heavy operations (order notifications, payment processing, inventory updates) away from the core API request-response lifecycle.
* **Optimized Caching Strategies**: Scalable caching layouts designed to dramatically reduce database read strain for popular product lookups and user sessions.
* **Strict Credential Isolation**: Secure environment management utilizing strict containerized security boundaries (`.gitignore`) to prevent secret leakage in cloud environments.
* **Type-Safe Request Validation**: Powered by **Pydantic** schemas for robust compile-time/runtime data integrity and contract-first API behavior.

---

## 🛠️ Project Directory Layout

```text
distributed-ecommerce/
│
├── app/
│   ├── __init__.py         # App package initialization
│   ├── main.py             # FastAPI core application initialization & startup logic
│   ├── config.py           # Configuration management (Pydantic BaseSettings)
│   ├── database.py         # SQLAlchemy engine setup & session lifecycle hooks
│   ├── models.py           # Core SQL database relational models (Users, Orders, Products)
│   ├── schemas.py          # Pydantic data validation & serialization schemas
│   ├── worker.py           # Celery asynchronous task configuration & worker logic
│   │
│   └── routes/
│       └── orders.py       # Flash-sale safe API endpoints for order management
│
├── frontend/
│   ├── index.html          # Operational dashboard client interface
│   └── style.css           # Dashboard interface styling
│
├── .env                    # Local environment config & secrets (STRICTLY IGNORED)
├── .gitignore              # Specifies intentionally untracked files to exclude
└── requirements.txt        # Python package dependency manifest
```

---

## ⚙️ Installation & Local Setup

### 1. Repository Setup
Clone the repository to your local system:
```bash
git clone https://github.com
cd distributed-ecommerce
```

### 2. Environment Configuration
Create a local `.env` configuration file in the project's root folder. **Do not commit this file to source control.**
```env
DATABASE_URL=postgresql://postgres:your_secure_password@localhost:5432/ecommerce_db
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
ENVIRONMENT=development
```

### 3. Dependency Management
Install the necessary system and framework requirements:
```bash
pip install -r requirements.txt
```

### 4. Running the Ecosystem
To run the complete distributed platform locally, execute the following runtime services in separate terminal sessions:

* **Start the Web API Gateway:**
  ```bash
  uvicorn app.main:app --reload
  ```
* **Start the Distributed Celery Background Worker Engine:**
  ```bash
  celery -A app.worker.celery worker --loglevel=info
  ```. **Data Integrity vs Speed**: Utilizing strict schema parsing via Pydantic to filter malicious or malformed request payloads before                            they hit downstream services.
