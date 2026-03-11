# Security Assessment Report
Generated: 2026-03-10 00:22:45.306514

## Port 3000 (ppp)
Product:  
Risk Level: High

### Detected Vulnerabilities
- fingerprint-strings: 
  GetRequest: 
    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    Feature-Policy: payment 'self'
    X-Recruiting: /#/jobs
    Accept-Ranges: bytes
    Cache-Control: public, max-age=0
    Last-Modified: Tue, 03 Mar 2026 02:59:03 GMT
    ETag: W/"1252f-19cb1a28249"
    Content-Type: text/html; charset=UTF-8
    Content-Length: 75055
    Vary: Accept-Encoding
    Date: Tue, 10 Mar 2026 03:26:01 GMT
    Connection: close
    <!--
    Copyright (c) 2014-2026 Bjoern Kimminich & the OWASP Juice Shop contributors.
    SPDX-License-Identifier: MIT
    <!doctype html>
    <html lang="en" data-beasties-container>
    <head>
    <meta charset="utf-8">
    <title>OWASP Juice Shop</title>
    <meta name="description" content="Probably the most modern and sophisticated insecure web application">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link id="favicon" rel="icon"
  HTTPOptions, RTSPRequest: 
    HTTP/1.1 204 No Content
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Methods: GET,HEAD,PUT,PATCH,POST,DELETE
    Vary: Access-Control-Request-Headers
    Content-Length: 0
    Date: Tue, 10 Mar 2026 03:26:01 GMT
    Connection: close
  Help, NCP: 
    HTTP/1.1 400 Bad Request
    Connection: close

## Port 3306 (mysql)
Product: MySQL 8.3.0
Risk Level: High

### Detected Vulnerabilities
- vulners: 
  cpe:/a:mysql:mysql:8.3.0: 
    	NODEJS:602	0.0	https://vulners.com/nodejs/NODEJS:602

## Port 5000 (rtsp)
Product:  
Risk Level: High

### Detected Vulnerabilities
- fingerprint-strings: 
  FourOhFourRequest: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785254
  GetRequest: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95780111
  HTTPOptions: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785250
  RTSPRequest: 
    RTSP/1.0 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95780119
  SIPOptions: 
    RTSP/1.0 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    CSeq: 42 OPTIONS
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785259

## Port 5432 (postgresql)
Product: PostgreSQL DB 9.6.0 or later
Risk Level: Low

## Port 7000 (rtsp)
Product:  
Risk Level: High

### Detected Vulnerabilities
- fingerprint-strings: 
  FourOhFourRequest: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785115
  GetRequest: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785107
  HTTPOptions: 
    HTTP/1.1 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785112
  RTSPRequest: 
    RTSP/1.0 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95780103
  SIPOptions: 
    RTSP/1.0 403 Forbidden
    Content-Length: 0
    Server: AirTunes/935.7.1
    CSeq: 42 OPTIONS
    X-Apple-ProcessingTime: 0
    X-Apple-RequestReceivedTimestamp: 95785250

## Port 8888 (tcpwrapped)
Product:  
Risk Level: Low

## Port 9000 (http)
Product: Apache Tomcat 
Risk Level: High

### Detected Vulnerabilities
- http-stored-xss: Couldn't find any stored XSS vulnerabilities.
- http-phpmyadmin-dir-traversal: 
  VULNERABLE:
  phpMyAdmin grab_globals.lib.php subform Parameter Traversal Local File Inclusion
    State: UNKNOWN (unable to test)
    IDs:  CVE:CVE-2005-3299
      PHP file inclusion vulnerability in grab_globals.lib.php in phpMyAdmin 2.6.4 and 2.6.4-pl1 allows remote attackers to include local files via the $__redirect parameter, possibly involving the subform array.
      
    Disclosure date: 2005-10-nil
    Extra information:
      ../../../../../etc/passwd :
  <!doctype html>
  <html lang="en">
    <head>
      <script type="module" crossorigin src="/js/polyfills-DCHatQ4c.js"></script>
  
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
      <link rel="icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="application-name" content="SonarQube" />
      <meta name="msapplication-TileColor" content="#FFFFFF" />
      <meta name="msapplication-TileImage" content="/mstile-512x512.png" />
      <title>SonarQube</title>
      <script>
        window.__assetsPath = function (filename) {
          return '/' + filename;
        };
      </script>
      <script type="module" crossorigin src="/js/main-HauAlxg8.js"></script>
      <link rel="modulepreload" crossorigin href="/js/vendor-BBa_E1n6.js">
      <link rel="modulepreload" crossorigin href="/js/lodash-s22JGpjx.js">
      <link rel="modulepreload" crossorigin href="/js/echoes-B7PIEOOz.js">
      <link rel="modulepreload" crossorigin href="/js/highlightjs-BVGoGOkc.js">
      <link rel="modulepreload" crossorigin href="/js/datefns-C62rL--z.js">
      <link rel="stylesheet" crossorigin href="/css/echoes-BVXoFVuc.css">
      <link rel="stylesheet" crossorigin href="/css/main-sinZSPt8.css">
    </head>
  
    <body>
      <div
        id="content"
        data-base-url=""
        data-server-status="UP"
        data-instance="SonarQube"
        data-official="true"
      >
        <div class="global-loading">
          <i class="global-loading-spinner"></i>
          <span aria-live="polite" class="global-loading-text">Loading...</span>
        </div>
      </div>
    </body>
  </html>
  
    References:
      http://www.exploit-db.com/exploits/1244/
      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3299

- http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
- http-dombased-xss: Couldn't find any DOM based XSS.
- http-csrf: Couldn't find any CSRF vulnerabilities.
- http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)

## Port 9001 (elasticsearch)
Product: Elastic elasticsearch 8.14.3
Risk Level: High

### Detected Vulnerabilities
- http-stored-xss: Couldn't find any stored XSS vulnerabilities.
- ssl-ccs-injection: No reply from server (TIMEOUT)
- http-csrf: Couldn't find any CSRF vulnerabilities.
- vulners: 
  cpe:/a:elasticsearch:elasticsearch:8.14.3: 
    	VERACODE:86905	7.5	https://vulners.com/veracode/VERACODE:86905
    	OSV:BIT-ELASTICSEARCH-2024-52981	7.5	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2024-52981
    	OSV:BIT-ELASTICSEARCH-2024-52979	7.5	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2024-52979
    	VERACODE:157409	7.4	https://vulners.com/veracode/VERACODE:157409
    	OSV:BIT-ELASTICSEARCH-2025-37731	7.4	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2025-37731
    	VERACODE:86904	6.5	https://vulners.com/veracode/VERACODE:86904
    	OSV:BIT-ELASTICSEARCH-2025-68384	6.5	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2025-68384
    	OSV:BIT-ELASTICSEARCH-2024-52980	6.5	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2024-52980
    	VERACODE:149013	5.7	https://vulners.com/veracode/VERACODE:149013
    	OSV:BIT-ELASTICSEARCH-2025-37727	5.7	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2025-37727
    	OSV:BIT-ELASTICSEARCH-2025-68390	4.9	https://vulners.com/osv/OSV:BIT-ELASTICSEARCH-2025-68390
- http-dombased-xss: Couldn't find any DOM based XSS.
- http-aspnet-debug: ERROR: Script execution failed (use -d to debug)

