### Getting Started

Follow these steps to set up and run the project locally.

#### 1. Installation

First, install the required dependencies by running the following command in your terminal (Command Prompt):

```bash
pip install -r requirements.txt
```

#### 2. Database Configuration

Update the database settings in `settings.py` according to your requirements. Then, apply the migrations by executing the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 3. Run the Server

Finally, start the development server by running the following command:

```
python manage.py runserver
```

Now, you're ready to use the application locally!

---
