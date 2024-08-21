**Chat Application**

A real-time chat application built with Django and Django Channels, featuring user authentication, room-based messaging, and an interactive chat interface. This project showcases the implementation of WebSocket-based real-time communication in Django.

**Features**

User Authentication: Secure login and signup functionality.
Real-Time Messaging: WebSocket integration for live chat.
Chat Rooms: Create and join chat rooms.
Active Users List: Display active users in each room.
Profile Pictures: Users can upload avatars.
Responsive Design: User-friendly interface across different devices.

**Installation**

Prerequisites
Python 3.x
Django 4.x
Django Channels
Redis (for Django Channels)

**Steps**
Clone the Repository

git clone https://github.com/yourusername/chat-application.git

cd chat-application

**Create a Virtual Environment**
python -m venv venv

**Activate the Virtual Environment**
Windows

venv\Scripts\activate
macOS/Linux

source venv/bin/activate

**Install Dependencies**

pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory and add the following:


SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Adjust the settings according to your environment.

**Apply Migrations**

python manage.py migrate

**Run Redis Server**

Ensure Redis is running locally. You can install it via Redis website or use a Docker container.

**Run the Development Server**

python manage.py runserver

**Usage**
Create a Room

Navigate to the home page, enter a username and room name, and optionally upload an avatar to create a new chat room.

Join a Room

Enter an existing room by providing the room name and your username.

Send Messages

Use the chat interface to send messages in real-time.

View Active Users

The list of active users in the current room is displayed on the left side.

**Contributing**
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

Fork the Repository

Create a New Branch

git checkout -b feature/your-feature

Commit Your Changes

git commit -m "Add feature"

Push to Your Branch

git push origin feature/your-feature

Open a Pull Request

Describe your changes and submit the pull request.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgements**
Django: A high-level Python Web framework.
Django Channels: Extends Django to handle WebSockets and background tasks.
Redis: In-memory data structure store for managing WebSocket connections.
