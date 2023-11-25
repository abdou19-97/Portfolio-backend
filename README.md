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

## Docker
Docker is used to create containers for the Django backend and any other required services (like databases or caching systems). Each container encapsulates the application and its dependencies, ensuring consistency across various environments. There are two main docker files used to achieve this goal.
server-side/Dockerfile: This file is instrumental in crafting a Docker image—a compact, self-contained, and executable package encompassing all essential dependencies to execute the application. In this context, it assembles the necessary components for running Django seamlessly.

![Dockerfile](https://github.com/abdou19-97/Portfolio-backend/blob/main/Dockerfile-sc.png?raw=true)

server-side/docker-compose.yml: docker-compose is a tool that allows defining and running multi-container Docker applications. It uses a YAML file to configure the services required for the entire application stack.

## Frontend Development

This section details the step-by-step frontend development process, accompanied by screenshots showcasing the directory structure during the development.
Commencing the ReactJS project, the initial steps involve the following instructions:
Installing React: In the same directory where the Django project is located and within the terminal I 
executed the following command:

`$npx create-react-app frontend`

This command will create a directory called frontend inside the current folder. Inside the directory, it’ll generate the initial project structure and install the dependencies.

The directory output looks like this:

![frontend](https://github.com/abdou19-97/Portfolio-backend/blob/main/frontend.png?raw=true)

Public/index.html: This file acts as the entry point for the application. It acts as the HTML file that is initially served to the client’s browser when React is loaded.
src folder: This folder contains the source code for the application. It typically contains all the JS files and JSX files, along with other assets such as CSS and images. For more information check out the src folder link on my GitHub portfolio-frontend directory.

Next.config.js: This file configure image optimization and handling for Next.js when dealing with remote images. The screenshot below shows the content of this file.

![next config](https://github.com/abdou19-97/Portfolio-backend/blob/main/next-config-sc.png?raw=true)

Images: The Images property is used to define remote image patterns that Next.js should consider as external images hosted on the specified domain.
remotePatterns: The remotePatterns array contains an object specifying the protocol (https), hostname (appmomentum.onrender.com), port (empty string in this case), and pathname (/**).
This configuration instructs Next.js to optimize and handle images fetched from the specified remote domain (appmomentum.onrender.com) using the defined protocol and pathname.
build folder: This folder is generated when building the React application for production. It contains the optimized and minified version of your React app that is ready for deployment. This folder includes the final bundle of JavaScript files, HTML files, CSS files, and other assets that are needed to run your React application in a production environment.
To generate a build folder I typed the following command:

  `$npm run build`

## Deployment:

	Deployment involves the process of preparing a software application for usage by configuring and making available its code, databases, configuration files, and other related components on a server or hosting environment.
For this project, I opted for two different web hosting services: Render for hosting the Postgres SQL and the backend, and Versel for the frontend built with ReactJS. Initially, I attempted to host the entire project on Render but encountered difficulties in configuring static files. After extensive troubleshooting, I found it more convenient to split the web app across different hosting providers.
In the forthcoming sections, I will provide a detailed walkthrough of how I deployed this project on both Render and Vercel.

## Render:
To begin deploying on Render, I navigated to the Render website and signed up using GitHub to facilitate easy connection with my GitHub repository for the backend.
Initially, I configured PostgreSQL to store the database housing the Post and Comment data. Below are screenshots of the PostgreSQL setup on Render

![PostgresSQL](https://github.com/abdou19-97/Portfolio-backend/blob/main/PostgresSQL-sc-2.png?raw=true)

Following the database setup, the next step involved establishing the database connection

![db-connection](https://github.com/abdou19-97/Portfolio-backend/blob/main/PostgresSQL-sc-3.png?raw=true)

Once the database connection was established, I proceeded to create the web service. The screenshots 
below depict the setup process:

![render](https://github.com/abdou19-97/Portfolio-backend/blob/main/web-service.png?raw=true)

I chose to build and deploy through the Git repository.

![render 2](https://github.com/abdou19-97/Portfolio-backend/blob/main/web-service-sc-2.png?raw=true)

I set the web service name to “appmomentum” and selected docker for deployment.

![render 3](https://github.com/abdou19-97/Portfolio-backend/blob/main/web-service-3.png?raw=true)

Finally, time to deploy:

![deployment](https://github.com/abdou19-97/Portfolio-backend/blob/main/web-service-sc-4.png?raw=true)

## Vercel

Vercel deployment was very fast and straightforward compared to Render. I created an account on Vercel through GitHub to facilitate easy connection with my GitHub repository. 

1.	Adding new project

![Vercel](https://github.com/abdou19-97/Portfolio-backend/blob/main/Vercel-sc.png?raw=true)

2.	Importing the Git repository
![vercel 2](https://github.com/abdou19-97/Portfolio-backend/blob/main/Vercel-sc-2.png?raw=true)

3.	Deploying
![vercel 3](https://github.com/abdou19-97/Portfolio-backend/blob/main/Vercel-sc-3.png?raw=true)

The final step is setting up the communication between Render which hosts the backend and Vercel which hosts the frontend. To do that I navigate to Render dashboard -> to web service (appmomentum in this case), and finally to the environment.

![deployment](https://github.com/abdou19-97/Portfolio-backend/blob/main/Deploy.png?raw=true)

* ALLOWED_HOSTS_DEPLOY: This variable represents the domain name  (.onrender.com) that Django will allow requests to be served from when the application is deployed. It ensures that Django only responds to requests from specified hosts, providing a layer of security against HTTP Host header attacks.
* CORS_ALLOWED_ORIGINS_DEPLOY: CORS This variable manages Cross-Origin Resource Sharing (CORS), enabling web applications from specific origins to access resources hosted on the Django backend when deployed. It defines the permitted origins or domains authorized to initiate cross-origin requests to the Django backend. For instance, it includes  Vercel's (https://portfolio-frontend-rouge-iota.vercel.app) to enable the web application to access the Django backend resources securely.
* CORS_ALLOWED_WHITELIST_DEPLOY: Similar to CORS_ALLOWED_ORIGINS_DEPLOY, this variable contains a whitelist of specific origins or domains that are allowed to access resources on the Django backend when deployed. It's a security measure to control which external sources can interact with the backend.
* CSRF_TRUSTED_ORIGINS_DEPLOY: CSRF (Cross-Site Request Forgery) is an attack where a malicious website can perform actions on another website where the user is authenticated. This variable could specify a list of trusted origins or domains for which Django allows CSRF protection to be disabled or considered safe. It ensures that CSRF protection is only enforced for certain origins or domains.


The link to my website: https://portfolio-frontend-rouge-iota.vercel.app/



