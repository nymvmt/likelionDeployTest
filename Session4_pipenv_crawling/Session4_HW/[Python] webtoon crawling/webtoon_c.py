def extract_info(WT_list):
    result = []

    for WT in WT_list:
        title = WT.find("dt").find("a")["title"]
        author = WT.find("dd",{"class": "desc"}).find("a").string
        rate = WT.find("div", {"class": "rating_type"}).find("strong").text

        WT_info = {
            'title': title,
            'author': author,
            'rate': rate
        }

        result.append(WT_info)
    return result