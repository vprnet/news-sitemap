from main import app
from flask import render_template, make_response
from query import get_posts


@app.route('/googlesitemap.xml')
def index():
    posts = get_posts(161419865)

    sitemap_xml = render_template('sitemap.xml', posts=posts)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response
