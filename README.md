<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/ufz_banner_may_23.png">
</p>
<h1 align="center">

[![PYPI](https://img.shields.io/badge/PYPI-UseReFuzz-orange)](https://pypi.org/project/userefuzz/) 
[![MIT](https://img.shields.io/github/license/root-tanishq/userefuzz)](https://github.com/root-tanishq/userefuzz/blob/main/LICENSE) 
[![Version](https://img.shields.io/badge/Latest--Version-2.2.0-brightgreen)](#)
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/root_tanishq.svg?style=social&label=Follow%20%40root_tanishq)](https://twitter.com/root_tanishq) <br />
[![Youtube](https://img.shields.io/youtube/channel/subscribers/UC0HLRnmOx3x_hsAGAdG9VaQ?style=social)](https://www.youtube.com/@boyfromfuture69)
[![Github](https://img.shields.io/github/stars/root-tanishq/userefuzz?style=social)](https://github.com/root-tanishq/userefuzz/stargazers)
[![Expy](https://img.shields.io/badge/Author-Tanishq%20Rathore-blue)](https://expy.bio/tanishq)
</h1>

<h3 align="center">

User-Agent , X-Forwarded-For and Referer SQLI Fuzzer made with `python`<br/>
**Works on `linux` and `unix` based systems**<br />
</h3>

<table>
<tr>
<td>  

<h3 align="center">

### Legal Disclaimer
</h3>
Usage of userefuzz for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
<br />


</td>
</tr>
</table>

<h1 align="center">

# Installation
</h1>

### pip

```sh
sudo pip install userefuzz
```

### setup

```sh
git clone https://github.com/root-tanishq/userefuzz
cd userefuzz
sudo python3 setup.py install
```

<h1 align="center">

# Usage  
</h1>
<h2 align="center">

## Parsing URLs
</h2>

### Parsing a list of URLs
```sh
$ userefuzz -l <LIST>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_list.png">
</p>

### Parsing a URL
```sh
$ userefuzz -u <URL>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_url.png">
</p>

### Parsing stdin URLs 
```sh
$ <STDIN LIST> | userefuzz
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_stdin.png">

> Use `-v` switch for verbose(includes non-vuln detected URLs) output 

</p>
<h2 align="center">

## Multi Processing
</h2>

> Multi Processing will create more process and will increase the speed of the tool.

```sh
$ userefuzz <LIST / URL> -w <WORKER COUNT>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_workers.png">
</p>

<h2 align="center">

## Proxy Interception And Custom Injection
</h2>

### Proxy interception of vulnerable request
```sh
$ userefuzz <LIST/URL> -p <PROXY>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_proxy.png">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_proxy2.png">
</p>

### Custom message in request
```sh
$ userefuzz <LIST/URL> -m <MESSAGE>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_msg.png">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_msg2.png">
</p>

### Custom payload with custom sleep

> Replace `sleep time` with `$UFZ$` variable for double verification of userefuzz

```sh
$ userefuzz <LIST/URL> -i <CUSTOM SQLI PAYLOAD> -s <SLEEP COUNT IN THE PAYLOAD>
```

### Multi payload with custom sleep

> Replace `sleep time` with `$UFZ$` variable for double verification of userefuzz

```sh
$ userefuzz <LIST/URL> -i <SQLI PAYLOAD FILE> -s <SLEEP COUNT IN THE PAYLOAD>
```

### Custom header injection
```sh
$ userefuzz <LIST/URL> -ch <CUSTOM HEADER NAME>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_finject2.png">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_sch2.png">
</p>

### Multi header injection
> For multiple headers use `|` as shown below.
```sh
$ userefuzz <LIST/URL> -ch <CUSTOM HEADER NAME|OTHER HEADERS> 
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_mch.png">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_mch2.png">
</p>


<h2 align="center">

## Output
</h2>

### Markdown output
```sh
$ userefuzz <LIST/URL> -o <OUTPUT FILE NAME WITHOUT EXT>
```
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_output.png">
</p>



### Output file content
<p align="center">
<img src="https://raw.githubusercontent.com/root-tanishq/userefuzz/main/images/u_2.1_out_md.png">
</p>
