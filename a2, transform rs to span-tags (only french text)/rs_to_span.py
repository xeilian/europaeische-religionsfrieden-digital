import requests, os, glob
from bs4 import BeautifulSoup
from pathlib import Path
from lxml import etree


def fetch_french_text_xml() -> list:
    url = "https://exist.ulb.tu-darmstadt.de/2/v/pa000325"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    rows = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if text == "französischer Text":
            href = a.get("href")
            if href:
                rows.append(href)
    out_dir = Path("hege_hiwi/xml/raw")
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in rows:
        xml_file_path = f"https://exist.ulb.tu-darmstadt.de/2/g/{i}"
        r = requests.get(xml_file_path)
        r.raise_for_status()
        out_path = out_dir / f"{i}r.xml"
        with open(out_path, "wb") as f:
            f.write(r.content)


def transform_rs_to_span(xmlfile) -> str:
    output_dir = Path("hege_hiwi/xml/converted")
    output_dir.mkdir(parents=True, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(xmlfile))[0]
    output = os.path.join(output_dir, f"{base_name[:-1]}c.xml")

    try:
        xslt_tree = etree.parse("hege_hiwi/refactor_rs_to_span.xslt")
        transform = etree.XSLT(xslt_tree)
        parser = etree.XMLParser(recover=True)
        tree = etree.parse(xmlfile, parser)
        result = transform(tree)
        with open(output, "wb") as f:
            f.write(etree.tostring(result, encoding="utf-8", xml_declaration=True, pretty_print=True))
        return output
    except Exception as e:
        print(f"Error processing {xmlfile}: {e}")



if __name__ == "__main__":
    fetch_french_text_xml()
    
    for i in glob.glob("hege_hiwi/xml/raw/*.xml"):
        transform_rs_to_span(i)
    
    