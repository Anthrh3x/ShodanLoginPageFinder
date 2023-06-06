<!DOCTYPE html>
<html>

<head>
  <title>Shodan Login Page Finder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 30px;
    }

    h1 {
      color: #333;
    }

    h2 {
      color: #666;
    }

    p {
      color: #444;
    }

    .badge {
      display: inline-block;
      padding: 5px 10px;
      font-size: 12px;
      font-weight: bold;
      color: #fff;
      background-color: #007bff;
      border-radius: 4px;
    }

    .license-link {
      color: #007bff;
    }
  </style>
</head>

<body>
  <h1>Shodan Login Page Finder</h1>

  <p>
    <span class="badge">License</span>
    <a class="license-link" href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">GNU General Public License v3.0</a>
  </p>

  <h2>Description</h2>
  <p>The Shodan Login Page Finder is a powerful and efficient tool designed to assist in the discovery of login pages
    exposed on the internet. Leveraging the capabilities of the Shodan search engine and the Shodan API, this tool allows
    you to perform targeted searches based on your query and identifies potential login pages on various commonly used
    web service ports.</p>

  <h2>How It Works</h2>
  <ol>
    <li>Shodan API Integration: The program integrates seamlessly with the Shodan API, enabling you to leverage its extensive
      search capabilities to discover relevant targets. You will need to obtain a Shodan API key and provide it in the code.</li>
    <li>Search Query: Upon running the program, you will be prompted to enter your search query. This query allows you to specify
      the criteria for the targeted search, such as specific services, keywords, or geographical locations.</li>
    <li>Login Page Detection: The program will initiate the search using the provided query and retrieve the results from the
      Shodan API. It will then analyze the retrieved data to identify potential login pages on the target IPs and ports.</li>
    <li>Authentication Testing: For each potential login page found, the program will attempt to authenticate against it using
      the provided default testing username and password. It will send HTTP requests to the identified login page URLs, simulating
      a login attempt.</li>
    <li>Multithreaded Execution: To expedite the authentication process and maximize efficiency, the program utilizes multithreaded
      execution. This allows multiple authentication attempts to be performed concurrently, resulting in faster processing of the
      search results.</li>
    <li>Results and Saving: The program will display the authentication status for each IP address, indicating whether the authentication
      was successful or not. It will also count and display the total number of targets authenticated successfully. Successful login
      IPs will be saved in a file for further analysis.</li>
  </ol>

  <h2>Dependencies</h2>
  <p>The Shodan Login Page Finder requires the following dependencies:</p>
  <ul>
    <li>Python (version 3.0 or higher)</li>
    <li>Shodan library</li>
    <li>Concurrent Futures library</li>
    <li>Requests library</
