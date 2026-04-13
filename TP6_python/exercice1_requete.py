VALID_METHODS = ["GET", "POST", "PUT", "DELETE", "HEAD"]
HTTP_VERSIONS = {1: "HTTP/1.1", 2: "HTTP/2.0"}

def format_request(method: str, url: str, version: int, headers: dict, body: str) -> str:
    """
    Formate une requête HTTP.

    :param method:  Méthode HTTP (GET, POST, PUT, DELETE, HEAD)
    :param url:     URL cible (ex: /index.html)
    :param version: Version HTTP (1 -> HTTP/1.1, 2 -> HTTP/2.0)
    :param headers: Dictionnaire des entêtes HTTP {nom: valeur}
    :param body:    Corps de la requête
    :return:        Requête HTTP formatée sous forme de chaîne
    """
    if method not in VALID_METHODS:
        raise ValueError(f"Méthode invalide : '{method}'. Doit être parmi {VALID_METHODS}")

    if version not in HTTP_VERSIONS:
        raise ValueError(f"Version invalide : {version}. Doit être 1 (HTTP/1.1) ou 2 (HTTP/2.0)")

    http_version = HTTP_VERSIONS[version]

    # Première ligne
    request = f"{method} {url} {http_version}\r\n"

    # Entêtes
    for name, value in headers.items():
        request += f"{name}: {value}\r\n"

    # Ligne vide séparant les entêtes du body
    request += "\r\n"

    # Body
    if body:
        request += body

    return request


# --- Test ---
if __name__ == "__main__":
    headers = {
        "Host": "localhost:8000",
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html, application/json"
    }

    req = format_request(
        method="GET",
        url="/index.html",
        version=1,
        headers=headers,
        body=""
    )
    print("=== Requête HTTP formatée ===")
    print(repr(req))
    print()
    print(req)