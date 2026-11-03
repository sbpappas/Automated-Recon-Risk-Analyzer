# Security Assessment Report
Generated: 2026-11-02 21:43:00.852903

* Port 3306 (mysql)
Product: MySQL 8.3.0
Risk Level: High

+++ Suggested Next Steps
- Attempt login: mysql -h 127.0.0.1 -u root -p
- Check MySQL info: nmap --script mysql-info -p 3306 127.0.0.1

* Port 5432 (postgresql)
Product: PostgreSQL DB 9.6.0 or later
Risk Level: Low

* Port 8080 (http)
Product: Jetty 12.0.16
Risk Level: Low

+++ Suggested Next Steps
- Run web scanner: nikto -h http://127.0.0.1:8080
- Directory brute force: gobuster dir -u http://127.0.0.1:8080 -w wordlist.txt

* Port 9000 (http)
Product: Apache Tomcat 
Risk Level: Low

+++ Suggested Next Steps
- Run web scanner: nikto -h http://127.0.0.1:9000
- Directory brute force: gobuster dir -u http://127.0.0.1:9000 -w wordlist.txt

* Port 9001 (http)
Product: Elasticsearch REST API 8.14.3
Risk Level: Low

+++ Suggested Next Steps
- Run web scanner: nikto -h http://127.0.0.1:9001
- Directory brute force: gobuster dir -u http://127.0.0.1:9001 -w wordlist.txt

