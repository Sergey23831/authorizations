from aiohttp import web

login = 'sergey.kozyrev02@mail.ru'
password = '8888'
# result = 0
# win = 0
# e = 20
# dig1 = 9
# dig2 = 99


async def handle(request: web.Request) -> web.StreamResponse:
    text = f'''<form method="post" action="/">
        <table>
            <tr>
                <td><label for="loginField">Кто ты?</label></td>
                <td><input id="loginField" type="text" name="login"></td>
            </tr>
            <tr>
                <td><label for="passwordField">Пароль</label></td>
                <td><input id="passwordField" type="password" name="password"></td>
            </tr>
            <tr>
                <td colspan="2" style="text-align: center"><input type="submit" value="Наступи в меня"></td>
            </tr>
        </table>
    </form>'''
    return web.Response(text=text, content_type='text/html')


async def wmnk1(request) -> web.StreamResponse:
    global login
    password
    a = await request.post()
    # print(a)
    x1 = (a["login"])
    x2 = (a["password"])
    print(f"login : {x1}\npassword : {x2}")
    # print(result)

    if (x1 == login):
        if (x2 == password):
            text = f'''<!DOCTYPE html>
                    <html>
                    <h1><h1/>
                    <h1><h1/>
                    <form action="/mnk">
                       <a href="https://www.youtube.com/watch?v=eHqqENg69EA">Go to YouTube</a>
                    </form>
                    </html>'''
        else:
            text = f'''<!DOCTYPE html>
                        <html>
                        <h1><h1/>
                        <form action="/mnk">
                           <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjk3OLhlt_2AhXjlIsKHbUnA9EQFnoECAcQAQ&url=http%3A%2F%2Fgayporka.top%2F&usg=AOvVaw1z03s7x5DN1tMRrMdkLhNd">Go to Nahui</a>
                        </form>
                        </html>'''

    else :
        text = f'''<!DOCTYPE html>
            <html>
            <h1><h1/>
            <form action="/mnk">
               <button class="test"></button>
            </form>
            </html>'''

    return web.Response(text=text, content_type='text/html')

app = web.Application()
app.add_routes(
    [
     # web.static('/', "/static"),
     web.get("/", handle),
     # web.get("/mnk", wmnk),
     web.post("/", wmnk1),
     web.get("/{name}", handle)])

web.run_app(app)