<h2>Apache Airflow for building workflows (Ubuntu server)</h2>
<p>Apache Airflow is the workflow management system to <b>create, schedule and monitor</b> workflows.</p>
<h3>Setup on Ubuntu</h3>
<ul>
  <img src="images/airflow-webserver-d.JPG">
  <li>sudo apt install python3-pip</li>
  <li>sudo pip3 install apache-airflow</li>
  <li>airflow initdb</li>
  <li>airflow webserver -p 8080</li>
  <li>airflow webserver -D -->> running airflow in the background</li>
  <li>airflow scheduler -D</li>
  <li>localhost:8080/admin</li>
  <li>ctrl + z -->>  stoping command</li>
</ul>
<h3>Useful commnads</h3>
<ul>
  <li>'cd ..' : moving back one directory.</li>
  <li>'ls -l'</li>
  <li>'sudo apt install vim'</li>
  <li>'vim script.py' <br>
       esc ->> ':qw' : quitting and writing a file
  </li>
</ul>
<h3>Directed Acyclig Graph</h3>
<ul>
  <img src="images/dag.JPG">
</ul>
<h3>Downstream info flow</h3>
<ul>
  <img src="images/downstream.JPG">
</ul>
<h3>DAG files directory</h3>
<ul>
  <img src="images/dag_files_dir.png">
</ul>
<h3>Creating .py files</h3>
<ul>
  <img src="images/new_py_file.JPG">
</ul>


