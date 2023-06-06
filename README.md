


<h1 align="center">Shodan Login Page Finder</h1>

<h2 align="center">BY ANTHRH3X</h2>

<h2>Description</h2>
<p>
  The Shodan Login Page Finder is a powerful and efficient tool designed to assist in the discovery of login pages exposed on the internet. Leveraging the capabilities of the Shodan search engine and the Shodan API, this tool allows you to perform targeted searches based on your query and identifies potential login pages on various commonly used web service ports.
</p>

<h2>How It Works</h2>
<ul>
  <li>
    <strong>Shodan API Integration:</strong> The program integrates seamlessly with the Shodan API, enabling you to leverage its extensive search capabilities to discover relevant targets. You will need to obtain a Shodan API key and provide it in the code.
  </li>
  <li>
    <strong>Search Query:</strong> Upon running the program, you will be prompted to enter your search query. This query allows you to specify the criteria for the targeted search, such as specific services, keywords, or geographical locations.
  </li>
  <li>
    <strong>Login Page Detection:</strong> The program will initiate the search using the provided query and retrieve the results from the Shodan API. It will then analyze the retrieved data to identify potential login pages on the target IPs and ports.
  </li>
  <li>
    <strong>Authentication Testing:</strong> For each potential login page found, the program will attempt to authenticate against it using the provided default testing username and password. It will send HTTP requests to the identified login page URLs, simulating a login attempt.
  </li>
  <li>
    <strong>Multithreaded Execution:</strong> To expedite the authentication process and maximize efficiency, the program utilizes multithreaded execution. This allows multiple authentication attempts to be performed concurrently, resulting in faster processing of the search results.
  </li>
  <li>
    <strong>Results and Saving:</strong> The program will display the authentication status for each IP address, indicating whether the authentication was successful or not. It will also count and display the total number of targets authenticated successfully. Successful login IPs will be saved in a file for further analysis.
  </li>
</ul>

<h2>Dependencies</h2>
<p>
  The Shodan Login Page Finder requires the following dependencies:
</p>
<ul>
  <li>Python (version 3.0 or higher)</li>
  <li>Shodan library</li>
  <li>Concurrent Futures library</li>
  <li>Requests library</li>
</ul>
<p>
  To install the dependencies, you can use the following command:
</p>
<pre><code>pip install shodan futures requests</code></pre>

<h2>Benefits</h2>
<ul>
  <li>
    <strong>Efficient Targeted Search:</strong> Utilize the power of the Shodan search engine and API to perform targeted searches based on your specific criteria. Discover potential login pages exposed on the internet with ease.
  </li>
  <li>
    <strong>Automated Authentication Testing:</strong> Authenticate against the discovered login pages using default testing credentials. Verify the accessibility of the login pages and identify potential security vulnerabilities.
  </li>
  <li>
    <strong>Multithreaded Execution:</strong> With the use of concurrent futures and multithreading, the program performs authentication attempts concurrently, allowing for faster processing of the search results.
  </li>
  <li>
    <strong>Easy Customization:</strong> Modify the default testing username and password to suit your specific needs. Easily customize the program to perform authentication tests with your own credentials.
  </li>
  <li>
    <strong>Save and Analyze Results:</strong> Successful login IPs are saved in a file for further analysis. Examine the results and gain insights into the security posture of the discovered login pages.
  </li>
</ul>

<h2>License</h2>
<p>
  This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.
</p>

<h2>Credits</h2>
<p>
  This project is brought to you by Anthrh3x. It is based on the original concept by Hassan_Zaib.
</p>

<h2>Contact</h2>
<p>
  For any inquiries or suggestions, please reach out to Hassanzaib@protonmail.com.
</p>





<p align="left">
<a href="https://instagram.com/hassan_zaib_ceo" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="hassan_zaib_ceo" height="30" width="40" /></a>
</p>

<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=anthrh3x&" alt="anthrh3x" /></p>
