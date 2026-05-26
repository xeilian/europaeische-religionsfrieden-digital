import requests, urllib.request
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


if __name__ == "__main__":
    modules_to_extract = ["pa000321", "pa000322", "pa000323"]
    text_data = []
    for i in modules_to_extract:
        module_data = fetch_eured_modul_ids(i)
        text_data.extend(module_data)
    print(text_data)
    for i in text_data:
        try:
            urllib.request.urlretrieve(f"https://tueditions.ulb.tu-darmstadt.de/g/{i[2]}", f"a4, find ontology/xml/{i[2]}_{i[0]}_{i[1]}.xml")
        except Exception as e:
            print(f"Error downloading {i[2]}: {e}")
    
    
