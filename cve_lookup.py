def lookup_cves(product, version):

    cve_db = {
        "apache": {
            "2.2": [
                "CVE-2017-5638 - Apache Struts RCE",
                "CVE-2019-0211 - Apache privilege escalation"
            ]
        },

        "openssh": {
            "7": [
                "CVE-2018-15473 - Username enumeration"
            ]
        },

        "vsftpd": {
            "2.3.4": [
                "CVE-2011-2523 - Backdoor command execution"
            ]
        },

        "mysql": {
            "5": [
                "CVE-2016-6662 - MySQL remote root code execution"
            ]
        }
    }

    product = product.lower()

    results = []

    if product in cve_db:
        for vuln_version in cve_db[product]:
            if version.startswith(vuln_version):
                results.extend(cve_db[product][vuln_version])

    return results
