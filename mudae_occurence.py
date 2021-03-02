#!/bin/python3

import json
import operator

exceptions = ["harem", "MYPRIVATESERVER", "TOP 1000", "wishlist", "Dr. Rodney McKay", "Vote"]

def load_json():
    """Loads data.json and gets all embeds messages"""

    file = open("data.json")
    data = json.load(file)
    mudae_messages = []

    messages = data.get("messages")
    if messages is None:
        print("no messages")
        return
    
    for message in messages:
        if message.get("embeds"):
            mudae_messages.append(message)
    return mudae_messages


def get_waifus(mudae_messages):
    """builds occurence dict of all waifus"""

    if mudae_messages is None:
        print("no messages so no waifu")
        return

    global exceptions
    waifu_list = {}
    for message in mudae_messages:
        embed = message["embeds"][0]
        waifu = embed.get("author")
        if not waifu or any(exception in waifu["name"] for exception in exceptions):
            continue
        
        waifu = waifu["name"]
        waifu_exists = waifu_list.get(waifu, False)
        if waifu_exists:
            waifu_list[waifu] += 1
            continue
        waifu_list[waifu] = 1
    
    waifu_list = _sort_dict_by_value(waifu_list)
    return waifu_list 

def get_series(mudae_messages):
    """builds occurence dict of all series"""

    if mudae_messages is None:
        print("no messages so no waifu")
        return
    
    series_list = {}
    for message in mudae_messages:
        embed = message["embeds"][0]
        series = embed.get("description")
        if not series:
            continue
        series = series.replace('\u200b', ' ').strip()

        if any(exception in series for exception in exceptions):
            continue
        series = series.split("\n")[0]
        series_exists = series_list.get(series, False)
        if series_exists:
            series_list[series] += 1
            continue
        series_list[series] = 1
    
    series_list = _sort_dict_by_value(series_list)
    return series_list 



def _sort_dict_by_value(occurence_dict):
    """sorts dict by value"""
    
    sorted_dict = sorted(occurence_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict


def get_best_values_from_list(list, best_occurence):
    """gets highest values from list"""
    
    for waifus in list:
        (waifu, occurence) = waifus
        if occurence >= best_occurence:
            print("{}: {}".format(waifu, occurence))


if __name__ == "__main__":
    mudae = load_json()
    waifu_list = get_waifus(mudae)
    series_list = get_series(mudae)
    print("top tier list waifus")
    get_best_values_from_list(waifu_list, 8)
    print("\n")
    print("top tier series")
    get_best_values_from_list(series_list, 80)


# fun little one liner I had
# index = next((i, waifu_dict) for i, waifu_dict in enumerate(waifu_list) if waifu in waifu_dict, None)
