from mcp.server.fastmcp import FastMCP

mcp = FastMCP("khalid-profile")

PROFILE = {
    "prenom": "Khalid",
    "nom": "debbagh",
    "age": 25,
    "ville": "Fès",
}

@mcp.tool()
def get_khalid_info() -> dict:
    """Retourne les informations personnelles de Khalid:
    nom, prenom, âge, ville."""
    return PROFILE

if __name__ == "__main__":
    mcp.run(transport="stdio")