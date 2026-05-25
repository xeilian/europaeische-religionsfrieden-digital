import requests, os
from bs4 import BeautifulSoup


def fetch_eured_modul_ids(module_id) -> dict:
    url = f"https://exist.ulb.tu-darmstadt.de/2/v/{module_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = []
    for li in soup.find_all("li"):
        btn = li.find("button", class_="wdbNav level")
        if not btn:
            continue
        titel = btn.get_text(strip=True)
        data_lvl = btn.get("data-lvl")
        if data_lvl == module_id:
            continue
        else:
            for a in li.find_all("a"):
                text = a.get_text(strip=True)
                label = text.lower()
                if label in ["einleitung", "lat. dipl. text", "zdt. dipl. text", "original", "prager frieden (dipl)", "wolfenbütteler vertrag (dipl)", "lateinischer text", "tschechischer text", "personenregister"]:
                    continue
                else:
                    href = a["href"]
                    if href.startswith("pa000008"):
                        rows.append([titel, text, href])
    return rows


def extract_text(href):
    url = f"https://exist.ulb.tu-darmstadt.de/2/v/{href}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    text_lines = []
    line_spans = soup.find_all("span", class_="lineNumber")
    for i in line_spans:
        text_fragments = []
        line_nr = i.get_text(strip=True)
        for sibling in i.next_siblings:
            if isinstance(sibling, type(i)) and sibling.name == "span" and "lineNumber" in sibling.get("class", []):
                break
            if sibling.name == "br":
                text_fragments.append(" ")
            else:
                raw = sibling.get_text(separator=" ", strip=True)
                text_fragments.append(" ".join(raw.split()))
        line_text = " ".join(text_fragments)
        line_text = " ".join(line_text.split())
        text_lines.append(f"{line_nr}: {line_text}")
    return text_lines


def save_to_csv(titel, text, href, text_lines):
    path = "hege_hiwi/a4/texts"
    os.makedirs(path, exist_ok=True)
    with open(f"hege_hiwi/a4/texts/{href}_{titel}_{text}.txt", mode="w", encoding="utf-8") as txt_file:
        txt_file.write("\n".join(text_lines))    


if __name__ == "__main__":
    modules_to_extract = ["pa000322"] #"pa000322", "pa000321", 
    text_data = []
    for i in modules_to_extract:
        module_data = fetch_eured_modul_ids(i)
        text_data.extend(module_data)
    for i in text_data:
        text_lines = extract_text(i[2])
        save_to_csv(i[0], i[1], i[2], text_lines)


    
    
