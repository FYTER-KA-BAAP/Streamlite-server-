import requests
import json
import time
import threading
import http.server
import socketserver

# Server handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"-- SERVER RUNNING >> RAJ H3R3")

# HTTP server function
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

# Function for spacing lines
def liness():
    print("-" * 60)

# Function to send messages
def send_messages_from_file():
    try:
        with open('convo.txt', 'r') as file:
            convo_id = file.read().strip()

        with open('File.txt', 'r') as file:
            messages = file.readlines()

        with open('lastname.txt', 'r') as file:
            last_name = file.read().strip()

        with open('tokennum.txt', 'r') as file:
            tokens = file.readlines()

        with open('hatersname.txt', 'r') as file:
            haters_name = file.read().strip()

        with open('time.txt', 'r') as file:
            speed = int(file.read().strip())

        num_messages = len(messages)
        num_tokens = len(tokens)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'
        }

        message_index = 1  # Start numbering from 1

        while True:
            for i in range(num_messages):
                token_index = i % num_tokens  # Tokens rotate properly
                access_token = tokens[token_index].strip()
                message = messages[i].strip()

                # Final message format
                final_message = f"{haters_name} {message} {last_name}"

                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                parameters = {'access_token': access_token, 'message': final_message}
                
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    print("\033[1;92m[+] Han Chla Gya Message {} of Convo {} Token {}: {}".format(
                        message_index, convo_id, token_index + 1, final_message))
                else:
                    print("\033[1;91m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                        message_index, convo_id, token_index + 1, final_message))

                liness()
                liness()

                message_index += 1  # Increase normal numbering
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")

    except Exception as e:
        print("[!] An error occurred: {}".format(e))

# Main function
def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    # Start the message sending loop
    send_messages_from_file()

if __name__ == '__main__':
    main()
