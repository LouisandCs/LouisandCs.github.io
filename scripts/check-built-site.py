"""Check rendered routes and the four requested navigation links."""
from html.parser import HTMLParser
from pathlib import Path

class NavigationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_nav = False
        self.current = None
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav":
            self.in_nav = True
        if self.in_nav and tag == "a" and "nav-link" in attrs.get("class", "").split():
            self.current = [attrs.get("href", ""), ""]

    def handle_data(self, data):
        if self.current is not None:
            self.current[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            href, label = self.current
            self.links.append((href, " ".join(label.replace("(current)", "").split())))
            self.current = None
        if tag == "nav":
            self.in_nav = False

expected = [("/", "Home"), ("/publications/", "Research"), ("/cv/", "CV"), ("/blog/", "Blog")]
for route, _ in expected:
    file = Path("_site") / route.strip("/") / "index.html"
    if not file.is_file():
        raise SystemExit(f"Missing built page: {file}")
    parser = NavigationParser()
    parser.feed(file.read_text(encoding="utf-8"))
    if parser.links != expected:
        raise SystemExit(f"Unexpected navigation on {route}: {parser.links!r}")
    if "example_pdf.pdf" in file.read_text(encoding="utf-8"):
        raise SystemExit(f"Template CV link remains on {route}")
print("Verified all four pages and navigation links.")
