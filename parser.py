import xml.etree.ElementTree as ET

def parse_scan(file):
    tree = ET.parse(file)
    root = tree.getroot()

    results = []

    for host in root.findall("host"):
        for port in host.findall(".//port"):
            state = port.find("state").attrib["state"]
            if state != "open":
                continue

            service = port.find("service")
            port_id = port.attrib["portid"]
            service_name = service.attrib.get("name", "")
            product = service.attrib.get("product", "")
            version = service.attrib.get("version", "")

            results.append({
                "port": port_id,
                "service": service_name,
                "product": product,
                "version": version
            })

    return results
