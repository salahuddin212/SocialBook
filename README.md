# Social Book

> **Connect. Share. Inspire.** > A sleek and modern social networking platform built to bring communities together through shared moments and visual stories.

---

## 📖 About The Project

**Social Book** is a robust, full-stack social media application designed to facilitate seamless interaction between users. Built with the power of Django, it provides a clean and responsive interface where users can curate their profiles, share image-based posts, and curate a personalized feed by following other creators.

Whether you're looking to build a niche community or a broad social network, Social Book offers the 
### ✨ Key Featuresfoundational architecture for a scalable and interactive platform.


* **🔐 Secure Authentication:** Complete user registration and login system with session management.
* **👤 Dynamic User Profiles:** Fully customizable profiles where users can update their bio, location, and profile pictures.
* **📸 Content Sharing:** Easy-to-use image upload functionality with caption support.
* **❤️ Interactive Feed:** A personalized homepage feed that aggregates posts from followed users. Includes a "Like" system for engagement.
* **🔍 User Discovery:** Integrated search functionality to find and connect with other members of the community.
* **🤝 Social Graph:** Follow/Unfollow system to curate the content you see.

---

## 🛠️ Tech Stack

This project leverages a modern, full-stack architecture:

* **Backend:** Python, Django Web Framework
* **Frontend:** HTML5, CSS3 (Tailwind CSS & UIkit), JavaScript (jQuery)
* **Database:** SQLite (Default for development) / SQL Compatible
* **Media Management:** Django File Storage

---

## 🚀 Installation & Setup

Follow these steps to get a local copy up and running.

### Prerequisites

* Python 3.8+
* pip (Python package manager)

### Step-by-Step Guide

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/socialbook.git
cd socialbook

```


2. **Create and Activate a Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Apply Database Migrations**
Initialize the database schema.
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Create a Superuser (Optional)**
Access the admin panel to manage users and posts.
```bash
python manage.py createsuperuser

```


6. **Run the Development Server**
```bash
python manage.py runserver

```


Visit `http://127.0.0.1:8000/` in your browser to see the app in action.

---

## 🕹️ Usage

1. **Sign Up:** Create a new account on the `/signup` page.
2. **Customize Profile:** Go to "Settings" to add a profile picture, bio, and location.
3. **Post Content:** Click "Upload" to share an image with a caption.
4. **Explore:** Use the search bar to find friends or other users.
5. **Engage:** "Follow" users to see their content on your home feed and "Like" posts that inspire you.

---

## 🗺️ Roadmap

We are constantly improving Social Book. Here are a few features we plan to roll out:

* [ ] **Comment System:** Allow users to discuss posts in a comments section.
* [ ] **Direct Messaging:** Real-time private chat between users.
* [ ] **Notification Center:** Alerts for likes, new followers, and interactions.
* [ ] **User Suggestion:** Suggest to the user new accounts to follow.

---

## 🤝 Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. 
---

*Made with ❤️ by Salahuddin*
