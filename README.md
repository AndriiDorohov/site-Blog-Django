## Blog Project

This project is a Django-based blog platform allowing users to create, publish, and manage articles, manage user profiles, and interact with the content.

[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_01.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_01.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_02.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_02.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_03.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_03.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_04.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_04.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_05.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_05.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_06.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_06.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_07.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_07.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_08.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_08.png)
[![Preview](https://github.com/AndriiDorohov/site-Blog-Django/raw/main/preview/page_09.png)](https://github.com/AndriiDorohov/site-Blog-Django/blob/main/preview/page_09.png)

## Models

The `models.py` file defines the database structure for the project:

### Profile

- One-to-one relationship with the Django `User` model
- Fields: `first_name`, `last_name`, `email`, `telephone`, `bio`, `location`, `birth_date`, `profession`, `education`, social media URLs, `image`

### Article

- Represents individual articles
- Fields: `author`, `title`, `summary`, `full_text`, `category`, `pubdate`, `slug`, `og_image`
- Methods: `get_absolute_url()`, `get_category_url()`, `get_author_url()`, `author_profile()`, `number_of_likes()`

### Comment

- Linked to an `Article` and `User`
- Fields: `article`, `user`, `text`, `created_at`

### SubscribedUsers

- Stores subscribed users for newsletters
- Fields: `name`, `email`, `created_date`

## Views

The `views.py` file contains various views to handle different pages and actions within the application:

- `home_page()`: Renders the home page with paginated articles
- `about_page()`: Renders the about page
- `single_post_page()`: Renders a single post page
- `pages_page()`: Renders the pages page
- `contact_page()`: Renders the contact page
- `article_page()`: Renders an article's detail page
- `category_page()`: Renders articles based on a specific category
- `author_page()`: Renders articles based on an author
- `create_article()`: Allows users to create articles
- `add_comment()`: Handles adding comments to articles
- `article_like()`: Handles article likes
- `registration()`: Handles user registration
- `user_login()`: Handles user login
- `article_search()`: Handles article search functionality
- `ArticleDetailView()`: Detail view for articles
- `profile()`: Renders and updates user profiles
- `profile_view()`: Renders user profiles for public viewing
- `newsletter()`: Handles newsletter functionalities
- `subscribe()`: Handles user subscriptions

## Forms

The `forms.py` file contains various forms used in the project:

- `ArticleForm`: Form for creating and updating articles
- `CommentForm`: Form for adding comments to articles
- `RegistrationForm`: Form for user registration
- `LoginForm`: Form for user login
- `ArticleSearchForm`: Form for article search
- `NewsletterForm`: Form for sending newsletters
- `UserRegisterForm`: Form for user registration with email
- `UserUpdateForm`: Form for updating user details
- `ProfileUpdateForm`: Form for updating user profiles

## Description

This project utilizes:

- **Frontend**: Clean CSS for styling and Vanilla JavaScript for functionality.
- **Backend**: Django framework with SQLite and PostgreSQL databases.

### Features:

- **User Interaction**: Engage by leaving comments, liking articles, registering, and creating user profiles.
- **Subscriptions & Emails**: Subscribe for updates and send newsletters to subscribers.
- **Database Management**: Utilizes SQLite and PostgreSQL for robust data handling.
- **Responsive Design**: Ensures adaptability across various devices.

## Usage

To use this project, ensure you have Django installed. Run the following commands:

```sh
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Visit [localhost:8000](http://localhost:8000) in your browser to access the application.

## Tech Stack

- Django
- Python
- Pillow (PIL)
- Pytz
- Django TinyMCE

## Contributions

Contributions to this project are welcome! Fork the repository, make changes, and submit a pull request.

## Key Features

- **Real-time Markdown Editor**: Edit Markdown content in real-time.
- **Image Upload**: Easily upload and manage images within the editor.
- **User Profiles**: Create and manage user profiles with customizable details.
- **Article Management**: Full-featured article management system with likes and comments.
- **Search Functionality**: Search articles based on titles, categories, or content.
- **Responsive Design**: Ensures seamless browsing across various devices.
- **Adaptive Layout**: Adapts effortlessly to different screen sizes for a consistent experience.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
