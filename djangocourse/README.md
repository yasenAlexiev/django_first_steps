# Django Blog Platform

A modern blog platform built with Django, following the Udemy course "Django 5.0 & Python: The Ultimate Web Development Bootcamp". This project serves as a learning exercise to understand Django's core concepts and modern web development practices.

## 🚀 Features

- User authentication and authorization
- Social authentication (GitHub, Google, Facebook)
- Blog post creation and management
- Rich text editing with EasyMDE
- Responsive design with Tailwind CSS
- Docker containerization
- Internationalization support

## 🛠️ Technologies Used

### Backend
- **Django 5.0** - High-level Python web framework
- **Django Allauth** - Authentication and social account management
- **Poetry** - Python dependency management
- **Docker** - Containerization

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **EasyMDE** - Markdown editor
- **Node.js** - JavaScript runtime for frontend tooling

### Development Tools
- **Docker Compose** - Multi-container Docker applications
- **Git** - Version control
- **Poetry** - Python package management

## 🏗️ Project Structure

```
djangocourse/
├── app/                 # Main application code
├── djangocourse1/      # Project configuration
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── tests/              # Test files
├── locale/             # Translation files
└── Dockerfile          # Docker configuration
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js
- Docker (optional)
- Poetry

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/djangocourse.git
cd djangocourse
```

2. Install Python dependencies:
```bash
poetry install
```

3. Install Node.js dependencies:
```bash
npm install
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

### Docker Setup

1. Build and start containers:
```bash
docker-compose up --build
```

2. Run migrations in Docker:
```bash
docker-compose exec web python manage.py migrate
```

## 📚 Learning Resources

This project is part of the Udemy course "Django 5.0 & Python: The Ultimate Web Development Bootcamp". The course covers:

- Django fundamentals
- Authentication and authorization
- Database models and migrations
- Template system
- Forms and validation
- Static files and media handling
- Deployment strategies

## 🤝 Contributing

This is a learning project, but contributions are welcome! Feel free to:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Udemy Course](https://www.udemy.com/course/django-5-python-web-development/) for providing the learning path
- Django community for their excellent documentation
- All open-source libraries used in this project
