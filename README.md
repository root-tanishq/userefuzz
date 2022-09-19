<p align="center">
<img src="https://github.com/root-tanishq/userefuzz/blob/main/images/logo.png" width=20%>
</p>
<h1 align="center">
<b>UseReFuzz</b>
</h1>

User-Agent , X-Forwarded-For and Referer SQLI Fuzzer made with `python`<br/>
**Works on `linux`, `Windows` and `MacOS` based systems**
<h3><b>Installation</b></h3><br/>

```sh
sudo pip3 install userefuzz
```

```sh
git clone https://github.com/root_tanishq/userefuzz
cd userefuzz
python3 setup.py install
```
<h3><b>Usage</b></h3><br/>

- **Parsing A List of URLS**

```sh
userefuzz -l <URL LIST>
```
![list](https://github.com/root-tanishq/userefuzz/blob/main/images/parse_a_list.png)<br />

- **Setup proxy for vulnerable requests**

```sh
userefuzz -l <URL LIST> -p 'http://127.1:8080'
```
![proxy](https://github.com/root-tanishq/userefuzz/blob/main/images/proxy_setup.png)<br />

![burp_proxy](https://github.com/root-tanishq/userefuzz/blob/main/images/proxy_setup_burp.png)<br />

- **Custom Message**

> Custom messages can be send with header for ease of sorting requerts in burpsuite

```sh
userefuzz -l <URL LIST> -p 'http://127.1:8080' -m '<Custom Message Here>'
```

![message](https://github.com/root-tanishq/userefuzz/blob/main/images/custom_message.png)<br />

![burp_message](https://github.com/root-tanishq/userefuzz/blob/main/images/custom_message_burp.png)<br />

- **Custom Payload Injection**

```sh
userefuzz -l <URL LIST> -i '<CUSTOM SQLI PAYLOAD>' -s <SLEEP ACCORDING TO PAYLOAD>
```

![inject](https://github.com/root-tanishq/userefuzz/blob/main/images/custom_inject.png)<br />

<h3><b>Follow</b></h3>
If this tool helped you or you like my work<br/>

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/root_tanishq.svg?style=social&label=Follow%20%40root_tanishq)](https://twitter.com/root_tanishq)