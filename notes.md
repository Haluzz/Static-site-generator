Next use Python's built-in HTTP server to serve the contents of the public directory:

cd public
python3 -m http.server 8888

Open your browser and paste in the URL of your server, (http://localhost:8888 if you used port 8888 as suggested) into the address bar. 



You can kill your server with Ctrl+C and restart it:

# from inside the public directory
python3 -m http.server 8888



chmod +x main.sh