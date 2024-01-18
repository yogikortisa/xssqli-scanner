# xssqli-scanner
Basic XSS and SQL Injection scanner in Python. The scope of this Proof-of-Concept (PoC) tool is limited to URLs with GET parameters as input. It has been tested on Python 3.

# Documentation
Step 1: Open terminal and clone the repository:

```
git clone https://github.com/yogikortisa/xssqli-scanner.git
cd xssqli-scanner
```

Step 2: Install the requirement:

```
pip3 install requests
```

Step 2: Run the scanner:

```
python xssqli.py
```

Step 3: Enter the URL with a GET parameter as input, below is the example of PoC:

```
http://testphp.vulnweb.com/listproducts.php?cat=1
```
