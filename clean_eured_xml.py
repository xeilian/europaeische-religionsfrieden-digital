import requests, os, re
from pathlib import Path
from lxml import etree


def fetch_eured_xml(id, out_dir, path) -> list:
    url = f"{path}/g/{id}"
    r = requests.get(url)
    r.raise_for_status()
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    os.makedirs("raw", exist_ok=True)
    file_path = out_dir / f"{id}_raw.xml"
    with open(file_path, "wb") as f:
        f.write(r.content)


def clean_text(tree: etree._ElementTree) -> None:
    root = tree.getroot()
    text = root.find(".//tei:text", namespaces=NS)
    if text is None:
        raise ValueError("No <text> element found in the XML.")
    
    paragraphs = text.xpath(".//tei:p", namespaces=NS)
    for p in paragraphs:
        raw = "".join(p.itertext())
        clean = re.sub(r"\s+", " ", raw).strip()
        for child in list(p):
            p.remove(child)
        p.text = clean


def main(eured_id, in_dir, out_dir) -> Path:
    in_path = Path(in_dir) / f"{eured_id}_raw.xml"
    tree = etree.parse(in_path)
    clean_text(tree)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_path = out_dir / f"{eured_id}_converted.xml"
    tree.write(raw_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    return raw_path


if __name__ == "__main__":
    NS = {"tei": "http://www.tei-c.org/ns/1.0"}
    TEI = "{http://www.tei-c.org/ns/1.0}"
    path = "https://exist.ulb.tu-darmstadt.de/2"
    eured_id = "pa000008-0415"
    fetch_eured_xml(eured_id, "data/raw", path)
    main(eured_id, "data/raw", "data/converted")

