<p align="center">
<img src="https://github.com/root-tanishq/userefuzz/blob/main/images/userefuzz_icon.png">
</p>
<h1 align="center">

[![PYPI](https://img.shields.io/badge/PYPI-UseReFuzz-orange)](https://pypi.org/project/userefuzz/) 
[![MIT](https://img.shields.io/github/license/root-tanishq/userefuzz)](https://github.com/root-tanishq/userefuzz/blob/main/LICENSE) 
[![Version](https://img.shields.io/badge/Latest--Version-2.0-brightgreen)](#)
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/root_tanishq.svg?style=social&label=Follow%20%40root_tanishq)](https://twitter.com/root_tanishq) <br />
[![Youtube](https://img.shields.io/youtube/channel/subscribers/UC0HLRnmOx3x_hsAGAdG9VaQ?style=social)](https://www.youtube.com/@boyfromfuture69)
[![Github](https://img.shields.io/github/stars/root-tanishq/userefuzz?style=social)](https://github.com/root-tanishq/userefuzz/stargazers)
[![Expy](https://img.shields.io/badge/Author-Tanishq%20Rathore-blue)](https://expy.bio/tanishq)
</h1>

<h3 align="center">

User-Agent , X-Forwarded-For and Referer SQLI Fuzzer made with `python`<br/>
**Works on `linux`, `Windows` and `MacOS` based systems**<br />
</h3>

<h2><b>Legal Disclaimer</h2></b>

Usage of userefuzz for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
<br />

<h2><b>Installation</b></h2><br/>

- pip

```sh
pip install userefuzz
```
> It will be installed by the name `userefuzz.py`


- setup

```sh
git clone https://github.com/root-tanishq/userefuzz
cd userefuzz
python3 setup.py install
```
> It will be installed by the name `userefuzz.py`

<h2><b>Usage</b></h2><br/>

<h3><b>Parsing a list of URLs</b></h2><br/>

```sh
userefuzz -l <URL LIST>
```

![list](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_parse_list.png)<br />

<h3><b>Parsing a URL</b></h2><br/>

```sh
userefuzz -u <URL>
```

![url](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_url.png)<br />

<h3><b>Parsing stdin</b></h2><br/>

```sh
<SOME COMMANDS> | userefuzz
```

![stdin](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_stdin.png)<br />

<h3><b>Verbose Output</b></h2><br/>

```sh
userefuzz <LIST / URL> -v
```

![vb](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_verbose.png)<br />

<h3><b>Multi Processing</b></h2><br/>

```sh
userefuzz <LIST / URL> -w <WORKER COUNT>
```

> 1 Worker Took 23 secs

![w1](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_worker1.png)<br />

> 10 Worker Took 20 secs

![w1](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_worker10.png)<br />

<h3><b>Proxy Interception of Vulnerable Requests</b></h2><br/>

```sh
userefuzz <LIST / URL> -p <YOUR PROXY>
```

![proxy](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_proxy.png)<br />

<h3><b>Custom Message in request</b></h2><br/>

```sh
userefuzz <LIST / URL> -m <MESSAGE>
```

![msg](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_message.png)<br />

<h3><b>Custom Payload with custom sleep</b></h2><br/>

```sh
userefuzz <LIST / URL> -i <CUSTOM SQLI PAYLOAD> -s <SLEEP COUNT IN THE PAYLOAD>
```

![inject](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_inject.png)<br />

<h3><b>Custom Header Injection</b></h2><br/>

```sh
userefuzz <LIST / URL> -ch <CUSTOM HEADER NAME>
```

![ch](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_header.png)<br />

<h3><b>Output</b></h2><br/>

```sh
userefuzz <LIST / URL> -o <OUTPUT FILE NAME WITHOUT EXT>
```

![o1](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_out1.png)<br />

> Output File 

![o1](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_out2.png)<br />

<h3><b>Telegram Notifications of Vulnerable Requests with Telify</b></h2><br/>

> The Tool uses [Telify](https://github.com/root-tanishq/telify) configuration file for sending notification .So inorder to use this feature you need to setup telify

```sh
userefuzz <LIST / URL> -t
```

![t](https://github.com/root-tanishq/userefuzz/blob/main/images/urf2_telify.png)<br />