# Train portals 

Automatically logs in through the portal page of different train or train station Wifi connections in Austria and Germany, so you do not have to manually open it in your browser when changing trains. To use it, either assign a custom hotkey to call connect.sh (such as Super+O to go online), or configure your operating system to call connect.sh automatically upon connecting to any new Wifi. Note that you will still be bound by the terms and conditions that would have been displayed on the portal page, so use it at your own responsibility.

## Requirements

* Linux with bash and iwconfig
* Python 3 (python3)
* Requests (python3-requests)

## Implementation

A central connection bash script (connect.sh) checks for the SSID currently connected to, and then calls the same-named Python or bash script, if it exists (converting the SSID to lowercase, and replacing spaces by underscores). Each script handles a specific portal by parsing the portal page and sending the correct login request.

## License

CC-BY-4.0

Forked from [Gabriel Huber](https://github.com/Yepoleb)'s [oebbwlan](https://github.com/Yepoleb/oebbwlan/), also under CC-BY-4.0.
