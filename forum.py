# -*- coding: utf-8 -*-
import web
import settings
import model
import form
import util
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
  '/', 'index',
  '/page/(.*)', 'index',
  '/add', 'add',
  '/view/(.*)', 'view',
  '/imgredirect', 'imgredirect')

app = web.application(urls, globals(), autoreload=True)

def render(params = {}, partial = False):
    global_vars = dict(settings.GLOBAL_PARAMS.items() + params.items())

    if partial:
        return web.template.render('templates/', globals=global_vars)
    else:
        return web.template.render('templates/', base='layout', globals=global_vars)

class about:
    def GET(self):
        return render({'title': settings.SITE_NAME}).about()

class add:
    def GET(self):
        f = form.post_add_form()
        return render({'title': settings.SITE_NAME}).add(f)

    def POST(self):
        f = form.post_add_form()
        if not f.validates():
            return render({'title': settings.SITE_NAME}).add(f)
        else:
            if not f.d.id:
                post_id = model.new_post(f.d.username, f.d.password, f.d.title, f.d.content)
                if post_id:
                    return web.redirect("/view/%d" % post_id)
                else:
                    return render({'title': settings.SITE_NAME}).failed()

class index:
    def GET(self, page = 1):
        page = int(page)
        html, pages = model.list_post(page)
        return render({'title': settings.SITE_NAME}).list(html, pages, page)

class view:
    def GET(self, post_id):
        post, user = model.view_post(post_id)
        f = form.post_add_form(post_id)
        f.id = post_id
        t = model.list_comment(post_id)
        return render({'title': settings.SITE_NAME, 'make_html': util.make_html}).view(post, user, t, f)

    def POST(self, post_id):
        post, user = model.view_post(post_id)
        f = form.post_add_form()
        t = model.list_comment(post_id)
        if not f.validates():
            return render({'title': settings.SITE_NAME, 'make_html': util.make_html}).view(post, user, t, f)
        else:
            if f.d.id:
                post_id = model.new_comment(f.d.username, f.d.password, f.d.title, f.d.content, f.d.id)
                if post_id:
                    return web.redirect("/view/%d" % post_id)
                else:
                    return render({'title': settings.SITE_NAME}).failed()

class imgredirect:
    def GET(self):
        i = web.input(url='')
        image_url = i.url
        return web.redirect(image_url)

if __name__ == "__main__":
    app.run()
