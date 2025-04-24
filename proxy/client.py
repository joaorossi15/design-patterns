from proxy import RemoteServiceProxy


if __name__ == "__main__":
    service = RemoteServiceProxy()

    print(service.get_values("John"))  
    print(service.get_values("John"))   
    print(service.get_values("Julia"))
