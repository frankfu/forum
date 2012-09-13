# -*- coding: utf-8 -*-
import web

def post_add_form(page_id=''):
    return web.form.Form(
        web.form.Textbox("username", web.form.notnull, size=20, description="用户名"),
        web.form.Password("password", description="密码"),
        web.form.Textbox("title", web.form.notnull, size=50, description="标题"),
        web.form.Textarea("content", web.form.notnull, rows=10, cols=70, description="内容"),
        web.form.Hidden('id', value=page_id),
        web.form.Button(u"确定"),
    )
