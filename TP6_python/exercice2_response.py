HTTP_STATUS = {
    200: "OK",
    201: "Created",
    301: "Moved Permanently",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
}

def format_response(status_code: int, headers: dict, body: str, version: str = "HTTP/1.1") -> str:
    """
    Formate une réponse HTTP.

    :param status_code: Code de statut HTTP (ex: 200, 404)
    :param headers:     Dictionnaire des entêtes HTTP {nom: valeur}
    :param body:        Corps de la réponse (HTML, JSON, etc.)
    :param version:     Version HTTP (défaut : HTTP/1.1)
    :return:            Réponse HTTP formatée sous forme de chaîne
    """
    status_text = HTTP_STATUS.get(status_code, "Unknown")

    # Première ligne
    response = f"{version} {status_code} {status_text}\r\n"

    # Entêtes
    for name, value in headers.items():
        response += f"{name}: {value}\r\n"

    # Ligne vide
    response += "\r\n"

    # Body
    if body:
        response += body

    return response


# --- Tests ---
if __name__ == "__main__":
    # Réponse 200 OK
    headers_200 = {
        "Server": "PythonTPServer",
        "Content-Type": "text/html",
        "Connection": "Closed"
    }
    body_200 = (
        "<!DOCTYPE html>\n"
        "<html>\n<body>\n"
        "<p>Bonjour</p>\n"
        '<p style="font-size:50px;">C\'est notre premier serveur</p>\n'
        "</body>\n</html>"
    )
    print("=== Réponse 200 ===")
    print(format_response(200, headers_200, body_200))

    # Réponse 404
    headers_404 = {
        "Server": "PythonTPServer",
        "Connection": "Closed"
    }
    body_404 = (
        "<html>\n<body>\n"
        "<h1>404 Not Found</h1>\n"
        "</body>\n</html>"
    )
    print("=== Réponse 404 ===")
    print(format_response(404, headers_404, body_404))