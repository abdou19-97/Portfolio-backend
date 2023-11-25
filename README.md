# portfolio-web-app
## Overview
This website serves as a showcase for my web development expertise. It's an ongoing portfolio web application I've developed, employing various technologies to create a robust and dynamic platform. The technologies utilized and their roles include:
* Django: A powerful Python framework is known for its simplicity and versatility in backend development. It serves as the backbone, managing data, content, and server-side functionalities.
*	PostgreSQL: A reliable open-source relational database management system used to store and manage the contents of the portfolio, ensuring data integrity and retrieval efficiency.
*	ReactJS: A JavaScript library for building user interfaces, providing a smooth, interactive, and responsive experience for visitors. It plays a pivotal role in shaping the front end and enhancing user interaction.
*	Docker: Leveraged for containerization, Docker encapsulates the web application, allowing for seamless deployment across various operating systems. It ensures consistency and flexibility in deployment environments.
*	Render: This hosting service supports the backend infrastructure, providing reliability and scalability for the web application's core functionalities.
*	Versel: Acts as the hosting service for the front end, ensuring high availability and performance for the user-facing part of the application.
In the following sections, I'll delve deeper into each technology's implementation and its specific contribution to the development of this web application.

## Backend Development

This section details the step-by-step backend development process, accompanied by screenshots showcasing the directory structure and the challenges encountered during the development. Throughout this phase, I utilized VS Code as my primary text editor.
Commencing the Django project, the initial steps involved the following instructions: 
* Installing Django:
In the terminal within the VS code, I executed the following command:

`$ pip install Django`
* Creating the project:
I generated the project using:

`$ django-admin startmyproject server-side`

This command generated a server-side directory in my current directory that looks like the following:

`server-side/

   	 manage.py
     
    	 backend/
      
        __init__.py
        
        settings.py
        
        urls.py
        
        asgi.py
        
        wsgi.py
   `

The outermost server-side directory serves as the encompassing container for the project, while the inner backend directory represents the actual project package, renamed from the default to prevent conflicts.
server-side/manage.py: This file serves as an interface for Django, enabling various functionalities like running the server, creating admin superusers, or generating apps.
backend/__init__.py: An empty file signaling that the directory is a Python package.
backend/settings.py: A crucial configuration file specific to this Python project.
backend/urls.py: This file hosts URL declarations for the project, encompassing routes like admin URLs or API endpoints.
backend/asgi.py and backend/wsgi.py: These files are responsible for serving the Python project via the ASGI and WSGI protocols, respectively.

![backend](https://github.com/abdou19-97/Portfolio-backend/blob/main/backend.png?raw=true)
This is a Visual of what the backend structure looks like.

To create my app directory, I made sure that I was in the same directory where my manage.py is located which is the server-side directory and then I typed the following command:

 `$ python manage.py startapp api`
 
This will create a directory api which will look like this:

![api](https://github.com/abdou19-97/Portfolio-backend/blob/main/api.png?raw=true)

* api/models.py: This file encapsulates the core models for this project, introducing the "Post" and "Comment" classes. Given that this is my initial Django project, I've kept the model structure simple for now. I intend to refine and expand this model in future iterations.
* api/serializer.py: Responsible for the serialization and deserialization processes, this file handles the conversion of model instances, such as "Post" and "Comment," into native Python data types. These converted data types can be seamlessly transformed into formats like JSON or XML.
* api/urls.py: This module focuses on configuring the URLs about comments and posts within the application, establishing the endpoints and routing for handling these specific functionalities.
* api/admin.py: This file plays a pivotal role in integrating the Django admin interface with the project. It allows me to register the application's models—such as "Post" and "Comment"—to be managed via the admin interface. This enables an easy-to-use administrative panel for handling and modifying the data stored in these models.
* api/views.py: Serving as a pivotal component of Django's MVC (Model-View-Controller) architecture, this file houses the views or "controllers" of the application. Here, I define the logic that dictates how data from the models interacts with the user interface. It includes functions responsible for handling HTTP requests, processing data, and rendering appropriate responses. These views form the backbone of the application's functionality, determining how data is presented to the users and how user inputs are processed.
* api/tests.py: Within this file, I've crafted test cases to ensure the functionality and reliability of the application. These tests are crucial as they validate the expected behavior of the different components of the project. They cover various scenarios, including data input, interactions, and processing, helping maintain the integrity and performance of the application.



