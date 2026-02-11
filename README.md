# 📘 SocialBook

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-darkgreen)](https://www.djangoproject.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **Connect. Share. Inspire.**
> A modern, full-stack social networking platform built to bring communities together through visual storytelling.

---

## 📖 About The Project

**SocialBook** is a robust social media application designed to facilitate seamless interaction between users. Built with the power of **Django**, it provides a clean and responsive interface where users can curate their profiles, share image-based posts, and explore a personalized feed of content from creators they follow.

Whether you're looking to build a niche community or a broad social network, SocialBook offers the foundational architecture for a scalable and interactive platform. It mimics core functionalities of popular platforms like Instagram, offering a familiar user experience.

### ✨ Key Features

* **🔐 Secure Authentication:** Complete user registration, login, and session management system to keep user data safe.
* **👤 Dynamic User Profiles:** Fully customizable profiles where users can update their bio, location, and profile pictures to express their identity.
* **📸 Content Sharing:** Seamless image upload functionality with caption support, allowing users to share moments instantly.
* **❤️ Interactive Engagement:** A "Like" system that drives engagement and allows users to show appreciation for content.
* **📰 Personalized Feed:** A smart homepage feed that aggregates posts only from users you follow, ensuring relevant content.
* **🔍 Advanced Discovery:** Integrated search functionality to find new friends and connect with other members of the community.
* **🤝 Social Graph:** A complete Follow/Unfollow system that lets users curate their network.

---

## 🛠️ Tech Stack

This project leverages a modern, full-stack architecture:

* **Backend:** [Python](https://www.python.org/) & [Django Web Framework](https://www.djangoproject.com/)
* **Frontend:** HTML5, CSS3 ([Tailwind CSS](https://tailwindcss.com/) & [UIkit](https://getuikit.com/)), JavaScript (jQuery)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Media Management:** Pillow (Python Imaging Library)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python installed on your system:
* Python 3.x
* pip (Python package manager)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/socialbook.git](https://github.com/your-username/socialbook.git)
    cd socialbook
    ```

2.  **Create a virtual environment** (Recommended)
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

6.  **Access the application**
    Open your browser and visit `http://127.0.0.1:8000/`.

---

## 🕹️ Usage

1.  **Sign Up:** Create a new account on the `/signup` page.
2.  **Customize Profile:** Go to "Settings" to add a profile picture, bio, and location.
3.  **Post:** Upload an image with a caption to share with your followers.
4.  **Explore:** Use the search bar to find other users and follow them to populate your feed.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**Project Link:** [https://github.com/your-username/socialbook](https://github.com/your-username/socialbook)
