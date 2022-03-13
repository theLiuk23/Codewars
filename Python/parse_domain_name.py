def domain_name(url:str):
    if url.__contains__("www."):
        return url.split("www.")[1].split(".")[0]
    elif url.__contains__("//"):
        return url.split("//")[1].split(".")[0]
    return url.split(".")[0]


print(domain_name("http://www.google.com/ygtre87"))