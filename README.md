<h1>TaskManagerAPI</h1>

<p>TaskManagerAPI is a web application built with Flask that allows users to manage their tasks. This README provides detailed instructions on how to set up and use the application.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
</ul>

<h2 id="installation">Installation</h2>
<p>Clone the repository:</p>

<pre><code>git clone https://github.com/your-username/TaskManagerAPI.git</code></pre>

<p>Change to the project directory:</p>

<pre><code>cd TaskManagerAPI</code></pre>

<p>Install dependencies:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>Start the application:</p>

<pre><code>python app.py</code></pre>

<p>The application will be accessible at <a href="http://localhost:5000">http://localhost:5000</a>.</p>

<h2 id="usage">Usage</h2>

<p>The TaskManagerAPI provides the following functionalities for managing tasks.</p>

<h3>Sign Up</h3>
<p>Open the web application in your browser. Click on the "Sign Up" link to navigate to the registration page. Fill in the required details (name, email, and password). Click the "Sign Up" button to create a new account.</p>

<h3>Login</h3>
<p>On the homepage, click on the "Login" link. Enter your registered email and password. Click the "Login" button to log into your account.</p>

<h3>Create Task</h3>
<p>After logging in, click on the "Create Task" link. Fill in the task details such as title, description, due date, and status. Click the "Create" button to add the task to your task list.</p>

<h3>Retrieve Task</h3>
<p>Click on the "Retrieve Task" link. Enter the task ID you want to retrieve. Click the "Retrieve" button to fetch the task details.</p>

<h3>Update Task</h3>
<p>Click on the "Update Task" link. Find the task you want to update in the table. Edit the task details directly in the respective table cells. Click the "Submit" button to save the updated task.</p>

<h3>Delete Task</h3>
<p>Click on the "Delete Task" link. Enter the task ID you want to delete. Click the "Delete" button to remove the task from your task list.</p>

<h3>List All Tasks</h3>
<p>Click on the "List All Tasks" link. The table will display all the tasks associated with your account. Use the pagination links at the bottom to navigate through multiple pages of tasks.</p>
